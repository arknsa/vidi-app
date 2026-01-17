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
            "disebabkan oleh benturan atau tabrakan. Kerusakan ini dapat memengaruhi "
            "estetika kendaraan dan pada tingkat tertentu berdampak pada struktur panel bodi."
        )
    },
    {
        "name": "Scratch",
        "img": "assets/classes/scratch.jpg",
        "desc": (
            "Scratch adalah kerusakan berupa goresan pada permukaan bodi kendaraan. "
            "Goresan dapat bersifat ringan hingga dalam tergantung pada tingkat "
            "penetrasi terhadap lapisan cat dan material bodi."
        )
    },
    {
        "name": "Crack",
        "img": "assets/classes/crack.jpg",
        "desc": (
            "Crack merupakan kerusakan berupa retakan pada bodi atau komponen kendaraan "
            "akibat benturan yang cukup kuat. Kerusakan ini berpotensi menurunkan "
            "kekuatan struktural kendaraan."
        )
    },
    {
        "name": "Glass Shatter",
        "img": "assets/classes/glass_shatter.jpg",
        "desc": (
            "Glass shatter mengacu pada kondisi pecah atau retaknya kaca kendaraan, "
            "seperti kaca depan atau kaca samping. Kerusakan ini sangat berbahaya "
            "karena dapat mengurangi visibilitas dan keselamatan pengemudi."
        )
    },
    {
        "name": "Lamp Broken",
        "img": "assets/classes/lamp_broken.jpg",
        "desc": (
            "Lamp broken adalah kerusakan pada lampu kendaraan baik lampu depan maupun "
            "belakang. Kerusakan ini dapat mengurangi fungsi pencahayaan dan meningkatkan "
            "risiko kecelakaan, terutama pada kondisi malam hari."
        )
    },
    {
        "name": "Tire Flat",
        "img": "assets/classes/tire_flat.jpg",
        "desc": (
            "Tire flat merupakan kondisi di mana ban kendaraan kehilangan tekanan udara "
            "secara signifikan. Kerusakan ini memengaruhi stabilitas dan keselamatan "
            "kendaraan sehingga perlu penanganan segera."
        )
    },
]


def render_classes(go):
    st.markdown("### Daftar Kerusakan Kendaraan")
    st.html("""
    <style>
    .card-grid {
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 24px;
        margin-top: 16px;
    }

    .card {
        border-radius: 12px;
        overflow: hidden;
        background: #ffffff;
        box-shadow: 0 4px 12px rgba(0,0,0,0.06);
        display: flex;
        flex-direction: column;
        height: 100%;
    }

    .card img {
        width: 100%;
        height: 220px;
        object-fit: cover;
    }

    .card-body {
        padding: 16px;
        flex: 1;
    }

    .card-title {
        font-size: 18px;
        font-weight: 600;
        font-style: italic;      /* ✅ NAMA KELAS ITALIC */
        margin-bottom: 8px;
    }

    .card-desc {
        font-size: 15px;
        line-height: 1.6;
        opacity: 0.85;
        text-align: justify;     /* ✅ DESKRIPSI JUSTIFY */
    }
    </style>
    """)


    cards_html = '<div class="card-grid">'

    for item in CLASSES_SHOWCASE:
        cards_html += f"""
        <div class="card">
            <img src="data:image/jpeg;base64,{img_to_base64(item['img'])}" />
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
        st.button("⬅️ Prediksi Kerusakan", on_click=go, args=("detect",))

    with col_right:
        st.button("Beranda ➡️", on_click=go, args=("home",))


