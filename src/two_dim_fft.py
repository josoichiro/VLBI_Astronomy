import numpy as np


def image_to_freq(image):
    """Convert a 2D image to its frequency representation using FFT.

    Args:
        image (np.ndarray): 2D array representing the grayscale image.

    Returns:
        np.ndarray: 2D array representing the frequency domain of the image.
    """
    # Perform 2D FFT
    freq_domain = np.fft.fft2(image)
    # Shift the zero frequency component to the center
    freq_domain_shifted = np.fft.fftshift(freq_domain)
    return freq_domain_shifted


def freq_to_image(freq_domain):
    """Convert a frequency representation back to a 2D image using inverse FFT.

    Args:
        freq_domain (np.ndarray): 2D array representing the frequency domain of the image.

    Returns:
        np.ndarray: 2D array representing the reconstructed grayscale image.
    """
    # Shift the zero frequency component back to the original position
    freq_domain_unshifted = np.fft.ifftshift(freq_domain)
    # Perform inverse 2D FFT
    image_reconstructed = np.fft.ifft2(freq_domain_unshifted)
    # Take the real part and convert to uint8
    image_reconstructed_real = np.real(image_reconstructed)
    return np.clip(image_reconstructed_real, 0, 255).astype(np.uint8)
