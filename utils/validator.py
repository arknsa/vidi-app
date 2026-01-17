# utils/validator.py
MAX_SIZE_MB = 25

ALLOWED_EXT = (".jpg", ".jpeg")

def validate_image(file):
    if file is None:
        return False, "Berkas belum diunggah"
    if not file.name.lower().endswith(ALLOWED_EXT):
        return False, "Format file harus JPG atau JPEG"
    if file.size > MAX_SIZE_MB * 1024 * 1024:
        return False, "Ukuran file melebihi batas"
    return True, "OK"
