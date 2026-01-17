# inference/yolov9_infer.py
import sys
import subprocess
import os
# Guard environment
os.environ["OMP_NUM_THREADS"] = "1"

# ===============================
# BARU IMPORT LIB ML
# ===============================

import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image

# ===============================
# BARU IMPORT LIB LAIN
# ===============================

import torch
import numpy as np
from ultralytics import YOLO
from PIL import Image


# ===============================
# Konfigurasi Model
# ===============================
MODEL_PATH = "models/yolov9c/best.pt"
CONF_THRES = 0.25
IOU_THRES = 0.5

# Load model sekali (cache global)
model = YOLO(MODEL_PATH)

# Nama kelas sesuai CarDD
CLASS_NAMES = [
    "Dent",
    "Scratch",
    "Crack",
    "Glass Shatter",
    "Lamp Broken",
    "Tire Flat"
]

def run_inference(image: Image.Image, side: str):
    """
    Menjalankan inference YOLOv9 pada satu citra kendaraan.
    Output:
    - image_annotated (PIL Image)
    - metadata (dict)
    """

    # Convert PIL → numpy (RGB)
    img_np = np.array(image)

    # Inference
    results = model.predict(
        source=img_np,
        conf=CONF_THRES,
        iou=IOU_THRES,
        verbose=False
    )

    result = results[0]
    annotated_img = Image.fromarray(result.plot())

    # Ambil ringkasan prediksi (jika ada)
    if result.boxes is not None and len(result.boxes) > 0:
        confs = result.boxes.conf.cpu().numpy()
        clss = result.boxes.cls.cpu().numpy().astype(int)

        top_idx = int(np.argmax(confs))
        label = CLASS_NAMES[clss[top_idx]]
        confidence = float(confs[top_idx])
    else:
        label = "No Damage Detected"
        confidence = 0.0

    return annotated_img, {
        "side": side,
        "label": label,
        "confidence": confidence
    }
