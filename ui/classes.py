# ui/classes.py
import streamlit as st
import base64

def img_to_base64(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode()

CLASSES_SHOWCASE = [
    {
        "name": "Dent",
        "img": "assets/classes/dent.jpg",
        "desc": (
            "Dent merupakan kerusakan berupa penyok pada bodi kendaraan yang umumnya "
            "disebabkan oleh benturan atau tabrakan."
        )
    },
    {
        "name": "Scratch",
        "img": "assets/classes/scratch.jpg",
        "desc": (
            "Scratch adalah kerusakan berupa goresan pada permukaan bodi kendaraan."
        )
    },
    {
        "name": "Crack",
        "img": "assets/classes/crack.jpg",
        "desc": (
            "Crack merupakan kerusakan berupa retakan akibat benturan yang cukup kuat."
        )
    },
    {
        "name": "Glass Shatter",
        "img": "assets/classes/glass_shatter.jpg",
        "desc": (
            "Glass shatter mengacu pada kondisi pecah atau retaknya kaca kendaraan."
        )
    },
    {
        "name": "Lamp Broken",
        "img": "assets/classes/lamp_broken.jpg",
        "desc": (
            "Lamp broken adalah kerusakan pada lampu kendaraan yang mengurangi fungsi pencahayaan."
        )
    },
    {
        "name": "Tire Flat",
        "img": "assets/classes/tire_flat.jpg",
        "desc": (
            "Tire flat merupakan kondisi ban kehilangan tekanan udara secara signifikan."
        )
    },
]

def render_classes(go):

    st.markdown("## Daftar Kerusakan Kendaraan")

    # ===============================
    # RESPONSIVE CSS (KHUSUS CLASSES)
    # ===============================
    st.html("""
    <style>

    /* Aktifkan scroll KHUSUS halaman ini */
    html, body {
        overflow-y: auto !important;
    }

    .card-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 20px;
        margin-top: 20px;
    }

    /* Tablet */
    @media (max-width: 1024px) {
        .card-grid {
            grid-template-columns: repeat(2, 1fr);
        }
    }

    /* Mobile */
    @media (max-width: 640px) {
        .card-grid {
            grid-template-columns: 1fr;
        }
    }

    .card {
        border-radius: 14px;
        overflow: hidden;
        background: #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        display: flex;
        flex-direction: column;
    }

    .card img {
        width: 100%;
        height: auto;          /* 🔑 PENTING */
        object-fit: cover;
    }

    .card-body {
        padding: 16px;
    }

    .card-title {
        font-size: 18px;
        font-weight: 600;
        font-style: italic;
        margin-bottom: 6px;
    }

    .card-desc {
        font-size: 15px;
        line-height: 1.6;
        opacity: 0.85;
        text-align: justify;
    }

    </style>
    """)

    cards_html = '<div class="card-grid">'

    for item in CLASSES_SHOWCASE:
        cards_html += f"""
        <div class="card">
            <img src="data:image/jpeg;base64,{img_to_base64(item['img'])}">
            <div class="card-body">
                <div class="card-title">{item['name']}</div>
                <div class="card-desc">{item['desc']}</div>
            </div>
        </div>
        """

    cards_html += "</div>"

    st.html(cards_html)

    st.divider()

    col_left, col_mid, col_right = st.columns([1, 6, 1])

    with col_left:
        st.button("⬅️ Prediksi Kerusakan", on_click=go, args=("detect",), use_container_width=True)

    with col_right:
        st.button("Beranda ➡️", on_click=go, args=("home",), use_container_width=True)
