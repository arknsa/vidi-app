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
# Main Renderer
# ======================================================
def render_detect(go):

    # ==================================================
    # Header
    # ==================================================
    st.markdown("## Prediksi Kerusakan Kendaraan")
    st.caption(
        "Unggah citra kendaraan dari empat sisi untuk mendeteksi jenis kerusakan "
        "secara otomatis menggunakan model *computer vision*."
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
        if st.button("🧪 Contoh 1 — Kerusakan Ringan", width="stretch"):
            st.session_state.scenario_images = load_scenario("scenario_1")
            st.session_state.inference_results = None

    with col_ex2:
        if st.button("🧪 Contoh 2 — Kerusakan Lebih Jelas", width="stretch"):
            st.session_state.scenario_images = load_scenario("scenario_2")
            st.session_state.inference_results = None

    st.caption(
        "Gambar contoh disediakan agar pengguna dapat memahami alur kerja sistem "
        "tanpa perlu menyiapkan foto kendaraan sendiri."
    )

    st.divider()

    # ==================================================
    # Image Input Helper
    # ==================================================
    def image_input(label: str, key: str):
        # From example set
        if key in st.session_state.scenario_images:
            img = st.session_state.scenario_images[key]
            st.image(
                img,
                caption=label,
                 width="stretch"
            )
            return img

        # Manual upload
        file = st.file_uploader(
            label,
            type=["jpg", "jpeg"],
            key=f"upload_{key}",
        )
        if file:
            return Image.open(file).convert("RGB")

        return None

    # ==================================================
    # Image Inputs (2 x 2 Grid)
    # ==================================================
    st.markdown("### Unggah Citra Kendaraan")

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
    valid = all(img is not None for img in images.values())

    if not valid:
        for side, img in images.items():
            if img is None:
                st.warning(f"{side}: gambar belum tersedia")

    # ==================================================
    # Action Buttons (SEJAJAR & KONSISTEN)
    # ==================================================
    st.markdown("### Aksi")

    col_left, col_center, col_right = st.columns([1, 6, 1])

    with col_left:
        detect_clicked = st.button(
            "🚀 Deteksi Kerusakan",
            disabled=not valid,
            width="stretch"
        )

    with col_right:
        if st.button(
            "🔄 Ganti Gambar",
            width="stretch"
        ):
            st.session_state.scenario_images = {}
            st.session_state.inference_results = None

            for k in ["Front", "Back", "Left", "Right"]:
                st.session_state.pop(f"upload_{k}", None)

            st.rerun()

    # ==================================================
    # Run Inference (Only Once)
    # ==================================================
    if detect_clicked:
        results = {}
        for side, img in images.items():
            annotated, meta = run_inference(img, side)
            results[side] = (annotated, meta)

        st.session_state.inference_results = results

    # ==================================================
    # Display Results (Persistent)
    # ==================================================
    if st.session_state.inference_results:
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
                st.image(
                    annotated,
                    width="stretch"
                )
                st.caption(
                    f"{meta['label']} | Confidence: {meta['confidence']:.2f}"
                )

                st.download_button(
                    f"⬇️ Unduh Hasil ({side})",
                    data=image_to_bytes(annotated),
                    file_name=f"hasil_{side.lower()}.jpg",
                    mime="image/jpeg",
                )

    st.divider()

    # ==================================================
    # Navigation Buttons (CONSISTENT GRID)
    # ==================================================
    col_nav_left, col_nav_mid, col_nav_right = st.columns([1, 6, 1])

    with col_nav_left:
        st.button("⬅️ Beranda", on_click=go, args=("home",), width="stretch")

    with col_nav_right:
        st.button(
            "Daftar Kerusakan ➡️",
            on_click=go,
            args=("classes",),
            width="stretch"
        )
