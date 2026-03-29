import torch
import torch.nn as nn
import torchvision.transforms as T
from src.Generator import Generator, nz
from PIL import ImageEnhance, Image

import os
from pathlib import Path

model_path = Path(os.getcwd()) / "model" / "model_checkpoint.pth"

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

netG = Generator().to(device)

checkpoint = torch.load(model_path, weights_only=True, map_location=device)
state_dict = {
    k.replace("module.", ""): v
    for k, v in checkpoint['generator_state_dict'].items()
}

netG.load_state_dict(state_dict)
netG.eval()

def generate_image():
    # img = ImageEnhance.Color(img).enhance(1.5)
    noise = torch.randn(1, nz, 1, 1, device=device)

    with torch.no_grad():
        tensor = netG(noise)

    tensor = tensor.squeeze(0)

    tensor = (tensor + 1) / 2
    tensor = torch.clamp(tensor, 0, 1)

    to_pil = T.ToPILImage()
    img = ImageEnhance.Color(to_pil(tensor)).enhance(1.5)
    img = img.resize((256, 256), Image.BICUBIC)
    return img