# DCGAN Anime Face Generator (64x64)

Simple DCGAN model for generating 64x64 anime faces.

<img src="https://github.com/rijulpaul/anime-face-dcgan/blob/main/results.png?raw=true" />


  <a href="https://www.kaggle.com/code/rijulpaul/anime-faces-using-dcgan-with-spectral-norm" target="_blank">
    <img alt="Kaggle Notebook" src="https://img.shields.io/badge/Kaggle-Notebook-blue?logo=kaggle" />
  </a>
  <span>&nbsp</span>
  <a href="https://www.kaggle.com/datasets/splcher/animefacedataset" target="_blank">
    <img alt="Kaggle Dataset" src="https://img.shields.io/badge/Kaggle-Dataset-blue?logo=kaggle" />
  </a>
  <span>&nbsp</span>
  <a href="https://huggingface.co/spaces/rijulpaul/anime-face-dcgan" target="_blank">
    <img alt="Hugging Face Space" src="https://img.shields.io/badge/%F0%9F%A4%97%20Hugging%20Face-Space-ffc107?color=ffc107&logoColor=white" />
  </a>
  <span>&nbsp</span>
  <a href="https://github.com/rijulpaul/anime-face-dcgan" target="_blank">
    <img alt="Hugging Face" src="https://img.shields.io/badge/Github-Repo-black?logo=github" />
  </a>
  
## Contents

* `model/` – trained generator and discriminator
* `notebook/` – training notebook
* `app.py` – Gradio app for sampling images

## Overview

This project uses a Deep Convolutional GAN (DCGAN) to generate anime-style faces at 64x64 resolution. The model is trained on a dataset of anime images and learns to produce new samples from random noise.

## Setup

```bash
git clone https://github.com/rijulpaul/anime-face-dcgan
cd anime-face-dcgan
```
#### Create and activate a virtual environment (recommended)
**Linux/MacOS**
```bash
python3 -m venv .venv
source .venv/bin/activate
```
**Windows**
```bash
python -m venv .venv
.venv\Scripts\activate
```
#### Install dependencies
```python
pip install --upgrade pip
pip install -r requirements.txt
```

## Usage
```bash
python app.py
```

### Run Notebook
#### On Kaggle
Add the [splcher/animefacedataset](https://www.kaggle.com/datasets/splcher/animefacedataset) dataset as input and run.
#### On local setup
Download the [splcher/animefacedataset](https://www.kaggle.com/datasets/splcher/animefacedataset) dataset and change the path to dataset in notebook.

### Run Gradio App

```bash
python app.py
```
