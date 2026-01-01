import runpod
import base64
import io
from PIL import Image

def handler(job):
    job_input = job.get("input", {})

    # Health check
    if job_input.get("ping") is True:
        return {"status": "ok"}

    image_b64 = job_input.get("image_base64")

    # 🔒 Hard stop if missing
    if not image_b64 or not isinstance(image_b64, str):
        return {
            "error": "image_base64 missing or invalid"
        }

    # 🔒 Strip data URL if present
    if "," in image_b64:
        image_b64 = image_b64.split(",", 1)[1]

    try:
        image_bytes = base64.b64decode(image_b64)
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    except Exception as e:
        return {
            "error": "image decode failed",
            "details": str(e)
        }

    return {
        "pose": "static pose detected",
        "interaction": "close physical proximity",
        "camera": "fixed framing",
        "confidence": 0.9
    }

runpod.serverless.start({"handler": handler})
