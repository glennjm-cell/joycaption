import runpod
import base64
import io
from PIL import Image

# -------------------------------------------------
# JOYCAPTION HANDLER (SAFE, FAST, TESTABLE)
# -------------------------------------------------

def handler(job):
    job_input = job.get("input", {})

    # -------------------------------------------------
    # FAST HEALTH CHECK / TEST
    # -------------------------------------------------
    if job_input.get("ping") is True:
        return {
            "status": "ok",
            "message": "joycaption endpoint alive"
        }

    # -------------------------------------------------
    # VALIDATE INPUT
    # -------------------------------------------------
    image_b64 = job_input.get("image_base64")

    if not image_b64:
        return {
            "error": "image_base64 missing"
        }

    # -------------------------------------------------
    # HANDLE DATA URL OR RAW BASE64
    # -------------------------------------------------
    if "," in image_b64:
        image_b64 = image_b64.split(",", 1)[1]

    try:
        image_bytes = base64.b64decode(image_b64)
    except Exception as e:
        return {
            "error": "invalid base64",
            "details": str(e)
        }

    # -------------------------------------------------
    # LOAD IMAGE (PIL)
    # -------------------------------------------------
    try:
        image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        width, height = image.size
    except Exception as e:
        return {
            "error": "image decode failed",
            "details": str(e)
        }

    # -------------------------------------------------
    # PLACEHOLDER CAPTION LOGIC (FAST)
    # -------------------------------------------------
    # This is intentionally lightweight.
    # You will replace this later with BLIP / LLaVA.
    # -------------------------------------------------

    result = {
        "subject": "adult person",
        "pose": "static pose detected",
        "interaction": "close physical proximity",
        "camera": "fixed framing",
        "image_width": width,
        "image_height": height,
        "confidence": 0.9
    }

    return result


# -------------------------------------------------
# RUNPOD SERVERLESS START
# -------------------------------------------------
runpod.serverless.start({
    "handler": handler
})
