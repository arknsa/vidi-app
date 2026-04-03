# ui/detect.py
import streamlit as st
from PIL import Image
import os

from inference.yolov9_infer import run_inference
from utils.io import image_to_bytes


# ======================================================
# Helper: Load Example Image Set
# ======================================================
def load_scenario(scenario_name: str):
    base_path = os.path.join("assets", scenario_name)

    return {
        "Front": Image.open(os.path.join(base_path, "front.jpg")).convert("RGB"),
        "Back": Image.open(os.path.join(base_path, "back.jpg")).convert("RGB"),
        "Left": Image.open(os.path.join(base_path, "left.jpg")).convert("RGB"),
        "Right": Image.open(os.path.join(base_path, "right.jpg")).convert("RGB"),
    }


# ======================================================
# Image Input Component (Upload / Camera Mode)
# ======================================================
def image_input(label: str, key: str):

    st.markdown(f"### 📸 {label}")

    # Jika menggunakan contoh skenario
    if key in st.session_state.scenario_images:
        img = st.session_state.scenario_images[key]
        st.image(img, width="stretch")
        return img

    # Mode pilihan sumber gambar
    mode = st.radio(
        "Pilih sumber gambar:",
        ["📁 Unggah dari Galeri", "📷 Ambil Foto Sekarang"],
        horizontal=True,
        key=f"mode_{key}"
    )

    # Upload mode
    if mode == "📁 Unggah dari Galeri":
        file = st.file_uploader(
            "Unggah gambar (.jpg / .jpeg)",
            type=["jpg", "jpeg"],
            key=f"upload_{key}",
        )
        if file:
            return Image.open(file).convert("RGB")

    # Camera mode
    else:
        photo = st.camera_input(
            "Ambil foto menggunakan kamera perangkat",
            key=f"camera_{key}"
        )
        if photo:
            return Image.open(photo).convert("RGB")

    return None


# ======================================================
# Main Renderer
# ======================================================
def render_detect(go):

    # ==================================================
    # Header
    # ==================================================
    st.markdown("## Prediksi Kerusakan Kendaraan")
    st.caption(
        "Unggah atau ambil foto kendaraan dari empat sisi "
        "(depan, belakang, kiri, kanan) untuk melakukan deteksi kerusakan secara otomatis."
    )

    # ==================================================
    # Session State Initialization
    # ==================================================
    if "scenario_images" not in st.session_state:
        st.session_state.scenario_images = {}

    if "inference_results" not in st.session_state:
        st.session_state.inference_results = None

    # ==================================================
    # Quick Example Buttons
    # ==================================================
    st.markdown("### Coba dengan Contoh Gambar")

    col_ex1, col_ex2 = st.columns(2, gap="large")

    with col_ex1:
        if st.button("🧪 Contoh 1 — Kerusakan Ringan", use_container_width=True):
            st.session_state.scenario_images = load_scenario("scenario_1")
            st.session_state.inference_results = None

    with col_ex2:
        if st.button("🧪 Contoh 2 — Kerusakan Lebih Jelas", use_container_width=True):
            st.session_state.scenario_images = load_scenario("scenario_2")
            st.session_state.inference_results = None

    st.divider()

    # ==================================================
    # Image Inputs (2 x 2 Grid)
    # ==================================================
    st.markdown("## Unggah / Ambil Citra Kendaraan")

    row1 = st.columns(2, gap="large")
    row2 = st.columns(2, gap="large")

    with row1[0]:
        front = image_input("Sisi Depan", "Front")

    with row1[1]:
        back = image_input("Sisi Belakang", "Back")

    with row2[0]:
        left = image_input("Sisi Kiri", "Left")

    with row2[1]:
        right = image_input("Sisi Kanan", "Right")

    images = {
        "Front": front,
        "Back": back,
        "Left": left,
        "Right": right,
    }

    # ==================================================
    # Validation
    # ==================================================
    valid = any(img is not None for img in images.values())

    if not valid:
        st.markdown("### Status Kelengkapan Gambar")
        for side, img in images.items():
            if img is None:
                st.warning(f"{side}: gambar belum tersedia")

    # ==================================================
    # Action Buttons
    # ==================================================
    st.markdown("### Aksi")

    col_left, col_center, col_right = st.columns([1, 6, 1])

    with col_left:
        detect_clicked = st.button(
            "🚀 Deteksi Kerusakan",
            disabled=not valid,
            use_container_width=True
        )

    with col_right:
        if st.button(
            "🔄 Ganti Gambar",
            use_container_width=True
        ):
            st.session_state.scenario_images = {}
            st.session_state.inference_results = None

            for k in ["Front", "Back", "Left", "Right"]:
                st.session_state.pop(f"upload_{k}", None)
                st.session_state.pop(f"camera_{k}", None)
                st.session_state.pop(f"mode_{k}", None)

            st.rerun()

    # ==================================================
    # Run Inference
    # ==================================================
    if detect_clicked:
        results = {}

        for side, img in images.items():
            if img is not None:
                annotated, meta = run_inference(img, side)
                results[side] = (annotated, meta)

        st.session_state.inference_results = results

    # ==================================================
    # Display Results
    # ==================================================
    if st.session_state.inference_results:

        st.divider()
        st.markdown("## Hasil Deteksi")

        row1 = st.columns(2, gap="large")
        row2 = st.columns(2, gap="large")

        layout = {
            "Front": row1[0],
            "Back": row1[1],
            "Left": row2[0],
            "Right": row2[1],
        }

        for side, col in layout.items():
            annotated, meta = st.session_state.inference_results[side]

            with col:
                st.markdown(f"### {side}")
                st.image(annotated, width="stretch")

                st.caption(
                    f"Prediksi: {meta['label']} | Confidence: {meta['confidence']:.2f}"
                )

                st.download_button(
                    f"⬇️ Unduh Hasil ({side})",
                    data=image_to_bytes(annotated),
                    file_name=f"hasil_{side.lower()}.jpg",
                    mime="image/jpeg",
                    use_container_width=True
                )

    st.divider()

    # ==================================================
    # Navigation
    # ==================================================
    col_nav_left, col_nav_mid, col_nav_right = st.columns([1, 6, 1])

    with col_nav_left:
        st.button(
            "⬅️ Beranda",
            on_click=go,
            args=("home",),
            use_container_width=True
        )

    with col_nav_right:
        st.button(
            "Daftar Kerusakan ➡️",
            on_click=go,
            args=("classes",),
            use_container_width=True
        )