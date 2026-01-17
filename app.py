import streamlit as st
import base64
from ui.home import render_home
from ui.classes import render_classes
from ui.detect import render_detect

# ======================================================
# PAGE CONFIG
# ======================================================
st.set_page_config(
    page_title="VIDI – Visual Intelligence for Damage Inspection",
    page_icon="🔍",
    layout="wide"
)

st.html("""
<style>
/* ===============================
   FIX LAYOUT WIDTH (NITIQ-STYLE)
   =============================== */

.main .block-container {
    max-width: 1100px;   /* 🔑 kunci utama */
    padding-left: 2rem;
    padding-right: 2rem;
    margin: auto;
}
</style>
""")

st.html("""
<style>
/* ===============================
   GLOBAL TYPOGRAPHY (NITIQ-STYLE)
   =============================== */

/* Body text */
html, body, p, span, li {
    font-size: 16px !important;
    line-height: 1.7 !important;
}

/* Section titles (###) */
h3 {
    font-size: 22px !important;
    font-weight: 600 !important;
    margin-bottom: 12px !important;
}

/* Card titles (class name) */
strong {
    font-size: 18px !important;
    font-weight: 600 !important;
}

/* Caption / description */
.stCaption {
    font-size: 15px !important;
    line-height: 1.6 !important;
    opacity: 0.85;
}

/* Button text */
button {
    font-size: 15px !important;
}
</style>
""")

# ======================================================
# HEADER LOGO + JUDUL (DIPERTAHANKAN)
# ======================================================
def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

logo_base64 = img_to_base64("assets/logo.png")

st.html(f"""
<div style="
    display:flex;
    flex-direction:column;
    align-items:center;
    text-align:center;
    width:100%;
    margin-top:32px;
    margin-bottom:24px;
">

    <img src="data:image/png;base64,{logo_base64}"
         style="width:240px; max-width:80%; height:auto; margin-bottom:12px;" />

    <h2 style="margin:0; font-weight:600;">VIDI</h2>

    <p style="margin-top:6px; opacity:0.75;">
        Visual Intelligence for Car Damage Detection
    </p>

</div>
""")

# ======================================================
# ROUTING (NITIQ-STYLE, TANPA UBAH UI)
# ======================================================
if "page" not in st.session_state:
    st.session_state.page = "home"

def go(page: str):
    st.session_state.page = page

if st.session_state.page == "home":
    render_home(go)
elif st.session_state.page == "classes":
    render_classes(go)
elif st.session_state.page == "detect":
    render_detect(go)
else:
    st.error("Halaman tidak ditemukan")
