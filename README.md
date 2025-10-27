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

## Output
The notebook produces calibrated visibility tables, diagnostic plots, and reconstructed images saved to the `outputs/` directory (create it if missing).