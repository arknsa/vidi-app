# VIDI
**Visual Intelligence for Vehicle Damage Inspection**

## Deskripsi
VIDI merupakan prototipe aplikasi web berbasis *computer vision* yang dikembangkan
untuk mendukung proses inspeksi kerusakan kendaraan mobil secara visual. Aplikasi ini
merupakan bagian dari penelitian skripsi yang membandingkan pendekatan arsitektur
deteksi objek berbasis **Convolutional Neural Network (CNN)** dan **Transformer**
dalam mendeteksi kerusakan kendaraan mobil menggunakan dataset **Car Damage Detection
Dataset (CarDD)**.

VIDI dirancang sebagai antarmuka interaktif yang memungkinkan pengguna non-teknis,
seperti teknisi bengkel, petugas asuransi, dan lembaga pembiayaan kendaraan, untuk
menjalankan proses inferensi model deteksi kerusakan kendaraan mobil melalui unggahan
citra.

## Fitur Utama
- Halaman beranda dengan deskripsi singkat sistem  
- Halaman daftar kelas kerusakan kendaraan mobil 
- Unggahan empat citra kendaraan mobil (depan, belakang, kiri, dan kanan)  
- Proses deteksi kerusakan berbasis model *deep learning*  
- Visualisasi hasil deteksi berupa *bounding box*, label kelas, dan skor
  kepercayaan  
- Unduhan hasil deteksi dalam format PNG  

## Kelas Kerusakan
Sistem mendukung enam kelas kerusakan kendaraan mobil, yaitu:
1. Dent  
2. Scratch  
3. Crack  
4. Glass Shatter  
5. Lamp Broken  
6. Tire Flat  

## Struktur Folder
WebApp/
├── app.py
├── inference/
│ └── yolov9_infer.py
├── models/
│ └── yolov9c/
│ └── best.pt
├── ui/
│ ├── home.py
│ ├── classes.py
│ └── detect.py
├── utils/
│ ├── validator.py
│ └── io.py
├── assets/
│ └── logo.svg
└── README.md


## Cara Menjalankan Aplikasi
1. Aktifkan virtual environment
2. Masuk ke direktori `WebApp`
3. Jalankan perintah:
   ```bash
   streamlit run app.py
