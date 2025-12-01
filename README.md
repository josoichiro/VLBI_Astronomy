# VLBI Example Notebook

This repository contains `vlbi_example.ipynb`, a walkthrough of Very Long Baseline Interferometry (VLBI) concepts and data processing workflows.

## Contents
- **Introduction**: Overview of VLBI and the observational setup.
- **Data Preparation**: Loading visibility datasets and metadata.
- **Calibration**: Applying delay, phase, and amplitude calibration steps.
- **Imaging**: Synthesizing sky images from calibrated visibilities.
- **Analysis**: Measuring flux densities and assessing image quality.

## Requirements
- Python 3.10+
- JupyterLab or Jupyter Notebook
- Recommended packages: `numpy`, `scipy`, `astropy`, `matplotlib`, `radio_beam`, `casatools`

Install dependencies with:

```bash
pip install -r requirements.txt
```

(or install the listed packages directly).

## Running the Notebook
```bash
jupyter lab vlbi_example.ipynb
```
Follow the sequential cells; each section builds on the previous one.

## 2D FFT Utility
Use `src/2d_fft.py` to generate synthetic 2D patterns (uniform field, Gaussian spot,
checkerboard, random noise) and inspect their Fourier spectra.

```bash
uv run python src/2d_fft.py --dataset gaussian --size 256 --sigma 0.15
```

- `--dataset`: one of `uniform`, `gaussian`, `checkerboard`, or `random`.
- `--size`: grid width/height (square array).
- `--sigma`: Gaussian width (ignored for other datasets).
- `--save path.png` (optional): write the spatial/frequency plot to disk.
- `--no-show` (optional): skip opening a Matplotlib window.

## Output
The notebook produces calibrated visibility tables, diagnostic plots, and reconstructed images saved to the `outputs/` directory (create it if missing).
