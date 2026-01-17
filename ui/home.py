# ui/home.py
import streamlit as st

def render_home(go):

    st.html("""
    <div style="
        text-align: justify;
        line-height: 1.7;
        font-size: 1rem;
        width: 100%;
    ">
        <p>
        VIDI merupakan prototipe aplikasi berbasis <i>computer vision</i> yang dirancang
        untuk melakukan deteksi kerusakan mobil secara otomatis dari citra digital.
        </p>

        <p>
        Aplikasi ini memanfaatkan model <i>deep learning</i> berbasis <i>object detection</i>
        untuk mengidentifikasi dan melokalisasi berbagai jenis kerusakan pada bodi mobil,
        seperti penyok, goresan, dan retakan, melalui citra kendaraan, sehingga berpotensi
        membantu teknisi bengkel, petugas asuransi, serta lembaga pembiayaan kendaraan
        dalam proses inspeksi awal berbasis visual.
        </p>

        <p>
        Pengembangan aplikasi ini bertujuan untuk menyediakan antarmuka yang sederhana
        dan mudah digunakan oleh pengguna non-teknis, sekaligus mendukung penelitian
        dan evaluasi kinerja model deteksi kerusakan kendaraan berbasis citra digital.
        </p>
    </div>
    """)
    st.divider()
    st.markdown("### Formulir Evaluasi")
    st.markdown(
        "[https://forms.gle/nXxWEzLSR3G6DWiXA](https://forms.gle/nXxWEzLSR3G6DWiXA)"
    )

    st.divider()

    st.markdown("### Cara Menggunakan Aplikasi")
    st.markdown(
        """
        1. **Daftar Kerusakan**  
           Pengguna dapat melihat enam kelas kerusakan kendaraan yang digunakan
           dalam sistem beserta deskripsi singkatnya.

        2. **Prediksi Kerusakan**  
           Pengguna mengunggah empat citra kendaraan dari sisi depan, belakang,
           kiri, dan kanan dalam format JPG. Sistem akan melakukan deteksi
           kerusakan dan menampilkan hasil berupa *bounding box*, label kelas,
           serta skor kepercayaan.
        """
    )

    st.markdown(
        "Navigasi antarhalaman dapat dilakukan menggunakan tombol di bawah ini."
    )

    st.divider()

    col_left, col_mid, col_right = st.columns([1, 6, 1])

    with col_left:
        st.button("⬅️ Daftar Kerusakan", on_click=go, args=("classes",))

    with col_right:
        st.button("Prediksi Kerusakan ➡️", on_click=go, args=("detect",))
