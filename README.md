# VIDI  
**Visual Intelligence for Vehicle Damage Inspection**

VIDI merupakan prototipe aplikasi web berbasis *computer vision* yang dikembangkan untuk mendukung proses inspeksi kerusakan kendaraan mobil secara visual. Aplikasi ini menjadi bagian dari penelitian skripsi yang berfokus pada **perbandingan arsitektur deteksi objek berbasis Convolutional Neural Network (CNN) dan Transformer**, dengan studi kasus deteksi kerusakan kendaraan menggunakan **Car Damage Detection Dataset (CarDD)**.

Aplikasi VIDI dirancang sebagai antarmuka interaktif yang dapat digunakan oleh pengguna non-teknis, seperti **teknisi bengkel, petugas asuransi, dan lembaga pembiayaan kendaraan**, untuk melakukan inferensi model deteksi kerusakan kendaraan melalui unggahan citra digital.

---

## 🌐 Demo Aplikasi
🔗 **Website (Streamlit App)**  
> *(isi link deployment Streamlit Cloud setelah deploy berhasil)*  
`https://<your-streamlit-app>.streamlit.app`

---

## 📝 Evaluasi Usability (SUS)
Pengujian usability aplikasi dilakukan menggunakan **System Usability Scale (SUS)** untuk menilai kemudahan penggunaan, konsistensi antarmuka, dan kenyamanan sistem berdasarkan persepsi pengguna.

🔗 **Form Evaluasi SUS**  
https://forms.gle/nXxWEzLSR3G6DWiXA

---

## 🚗 Kelas Kerusakan Kendaraan
Sistem VIDI mendukung enam kelas kerusakan kendaraan mobil, yaitu:

1. *Dent*  
2. *Scratch*  
3. *Crack*  
4. *Glass Shatter*  
5. *Lamp Broken*  
6. *Tire Flat*

---

## ✨ Fitur Utama
- Halaman beranda dengan deskripsi singkat sistem
- Halaman daftar kelas kerusakan kendaraan
- Unggahan **empat citra kendaraan** (depan, belakang, kiri, dan kanan)
- Proses deteksi kerusakan berbasis model *deep learning*
- Visualisasi hasil deteksi berupa *bounding box*, label kelas, dan skor kepercayaan
- Fitur unduhan hasil deteksi dalam format gambar beranotasi (PNG/JPG)

---

## 📁 Struktur Folder
```

WebApp/
├── app.py
├── inference/
│   └── yolov9_infer.py
├── models/
│   └── yolov9c/
│       └── best.pt
├── ui/
│   ├── home.py
│   ├── classes.py
│   └── detect.py
├── utils/
│   ├── validator.py
│   └── io.py
├── assets/
│   ├── classes/
│   ├── scenario_1/
│   ├── scenario_2/
│   └── logo.svg
└── README.md

````

---

## ▶️ Cara Menjalankan Aplikasi (Local)
1. Aktifkan *virtual environment*
2. Masuk ke direktori `WebApp`
3. Jalankan perintah berikut:
```bash
streamlit run app.py
````

---

## 🎓 Konteks Penelitian

Aplikasi ini dikembangkan sebagai bagian dari penelitian skripsi dengan topik:

> **Perbandingan Metode dan Implementasi Deteksi Kerusakan Mobil Berbasis CNN dan Transformer**

Hasil implementasi dan evaluasi usability digunakan sebagai pendukung analisis performa model serta kesiapan sistem untuk penggunaan praktis.

---

## 📌 Catatan

* Aplikasi ini bersifat **prototipe penelitian**
* Model deteksi dioptimalkan untuk citra dengan sudut pandang sesuai dataset CarDD
* Penggunaan di luar konteks penelitian memerlukan penyesuaian lebih lanjut

---

## 👤 Developer

**Arkan Syafiq At’taqy**
Program Studi Teknologi Sains Data
Universitas Airlangga
