"""Unit tests for src/2d_fft.py."""

from __future__ import annotations

import importlib.util
from pathlib import Path

import numpy as np
import pytest

MODULE_PATH = Path(__file__).resolve().parents[1] / "src" / "two_dim_fft.py"
spec = importlib.util.spec_from_file_location("fft_module", MODULE_PATH)
_module = importlib.util.module_from_spec(spec)
assert spec and spec.loader  # pragma: no cover - importlib internals
spec.loader.exec_module(_module)  # type: ignore[union-attr]

image_to_freq = _module.image_to_freq
freq_to_image = _module.freq_to_image


def test_roundtrip_identity() -> None:
    """image_to_freq followed by freq_to_image should reconstruct the image."""

    image = np.array(
        [[0, 10, 20, 30], [40, 50, 60, 70], [80, 90, 100, 110], [120, 130, 140, 150]],
        dtype=np.float64,
    )

    spectrum = image_to_freq(image)
    reconstructed = freq_to_image(spectrum)

    assert reconstructed.dtype == np.uint8
    np.testing.assert_array_equal(reconstructed, image.astype(np.uint8))


def test_dc_component_centered() -> None:
    """Uniform images should produce a single DC component at the center."""

    size = 4
    field = np.ones((size, size), dtype=np.float64)
    spectrum = image_to_freq(field)

    center = (size // 2, size // 2)
    assert spectrum.shape == field.shape
    assert spectrum[center].real == pytest.approx(size * size)
    assert spectrum[center].imag == pytest.approx(0)
    # Every other coefficient should be (near) zero for a constant input.
    mask = np.ones_like(spectrum, dtype=bool)
    mask[center] = False
    assert np.allclose(spectrum[mask], 0)


def test_freq_to_image_clips_values() -> None:
    """freq_to_image should clip the reconstructed image to [0, 255]."""

    image = np.array([[300.0, -20.0], [128.0, 64.0]])
    spectrum = np.fft.fftshift(np.fft.fft2(image))

    reconstructed = freq_to_image(spectrum)

    expected = np.clip(image, 0, 255).astype(np.uint8)
    np.testing.assert_array_equal(reconstructed, expected)


if __name__ == "__main__":
    pytest.main([__file__])
