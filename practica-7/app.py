import gradio as gr
from transformers import pipeline

clasificador = pipeline("image-classification", model="google/mobilenet_v2_1.0_224")


def clasificar(imagen):
    if imagen is None:
        return {}
    resultados = clasificador(imagen, top_k=3)
    return {r["label"]: r["score"] for r in resultados}


demo = gr.Interface(
    fn=clasificar,
    inputs=gr.Image(type="pil"),
    outputs=gr.Label(num_top_classes=3),
    title="¿Qué hay en la foto?",
    description="MobileNetV2 (14 MB) corriendo en mi computadora. Conoce 1,000 categorías de ImageNet, con nombres en inglés.",
    examples=["ejemplos/carro.jpg", "ejemplos/mi-foto.jpg"],
)

if __name__ == "__main__":
    demo.launch()
