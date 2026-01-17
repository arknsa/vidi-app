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

    rows = [
        CLASSES_SHOWCASE[0:3],
        CLASSES_SHOWCASE[3:6],
    ]

    for row in rows:
        cols = st.columns(3, gap="large")

        for col, item in zip(cols, row):
            with col:
                st.image(
                    item["img"],
                    use_container_width=True
                )
                st.markdown(
                    f"**{item['name']}**",
                )
                st.caption(item["desc"])

    st.divider()

    col_left, col_mid, col_right = st.columns([1, 6, 1])

    with col_left:
        st.button(
            "⬅️ Prediksi Kerusakan",
            on_click=go,
            args=("detect",),
            width="stretch"
        )

    with col_right:
        st.button(
            "Beranda ➡️",
            on_click=go,
            args=("home",),
            width="stretch"
        )
