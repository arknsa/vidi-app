# utils/io.py
import io

def image_to_bytes(image):
    buf = io.BytesIO()
    image.save(
        buf,
        format="JPEG",
        quality=95,
        subsampling=0
    )
    return buf.getvalue()
