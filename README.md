# DCGAN Anime Face Generator (64x64)

Simple DCGAN model for generating 64x64 anime faces.

<img src="https://www.kaggleusercontent.com/kf/303710638/eyJhbGciOiJkaXIiLCJlbmMiOiJBMTI4Q0JDLUhTMjU2In0..SOVohK5iv9fvXDVm1AMo_Q.USZlGAbymlZ0gsCHm3ENhNipijYa42pR-evHHhnOSCGR9ezCF9HEXLUpVJT-W0aqfju0KTTZ5nsVjtfdC2w6B-j9HIBcjBL8qDBM7cWq19NHuf5Ghkd4cRxAGQK9eeJnakhiQFUW5A_w_BFHVPgX2I0CWNzIWT2e7-qvmoObW00nxehQKokSu9eHD5SnDRDPN5ZWpvr-XAHlONalt4UZ5OHAvXEBOChWxZaNQHt0y58n5dwxS4_nl3-9f8utJOD2t6brf1EDcoL6Rk_M3mJ6UMdEbDU_c2K_3Ote8jUEQBTMHVbU1GL5gQTixY8tiK_Hko9eq92KEPIoqSbk7jWzunTRi-IyZoQxL4Odu8KOFUkft2WJQrVY67QoiKlz2bvI-VklgKOnTVvFI0TbQMDvQQjyu8Pgx4MNheu2voHUmqO1vAetucAdGDgDS0V8XaIGKFEwbvVYsZWVdEx5xGIVmpmP1vePJ7d7ebasmS1lw9yTlAAfCqumOIp3y7ZKtWzJfhuzYkBroKA5l7Mb1Q27CzJEJ5MWK_oVSIh9FSleJTgfjfe8JebG3-pw0iV1Ul44EOQfauW9pIC-L8SJeg3vtTDeAbXz4zDkyyoBY9MPaUaPNBhs3lNwpszGnVJlf6l6I0e2_MEu0xZSlAn35xzbvA.wWPnhgMrExyPQR9BQHCO2A/__results___files/__results___12_2.png" />


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
