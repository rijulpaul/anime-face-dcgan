import gradio as gr
from src.generate import generate_image

def download_image(img):
    path = "anime-face.png"
    img.save(path)
    return path

with gr.Blocks() as app:
    gr.Markdown("## DCGAN Image Generator")

    with gr.Row():
        # LEFT: Image
        with gr.Column(scale=3):
            img = gr.Image(type="pil",label="Generated Image")

        # RIGHT: Buttons
        with gr.Column(scale=1):
            btn = gr.Button("Generate")
            download_btn = gr.Button("Download")
            file = gr.File()

    btn.click(
        fn=generate_image,
        outputs=img
    )

    download_btn.click(
        fn=download_image,
        inputs=img,
        outputs=file
    )

app.launch()