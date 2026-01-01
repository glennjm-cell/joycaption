import runpod
import base64
import io
from PIL import Image

def handler(job):
    image_b64 = job["input"].get("image_base64")
    image_bytes = base64.b64decode(image_b64)
    image = Image.open(io.BytesIO(image_bytes)).convert("RGB")

    return {
        "pose": "static pose detected",
        "interaction": "close physical proximity",
        "camera": "fixed framing",
        "confidence": 0.9
    }

runpod.serverless.start({"handler": handler})
