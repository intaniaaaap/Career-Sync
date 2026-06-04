# 📊 CareerSync Analytics & Data Exploration Dashboard

Selamat datang di repositori komponen **Data Science & Analytics** untuk proyek **CareerSync**. Repositori ini berisi seluruh alur kerja analisis data eksploratif (EDA), rekayasa fitur (*feature engineering*), serta pengembangan dashboard interaktif menggunakan Streamlit untuk memvisualisasikan data lowongan kerja dari platform Glints.

Proyek ini merupakan bagian dari **Capstone Project Coding Camp 2026** dengan detail sebagai berikut:
- **ID Tim**: CC26-PSU278
- **Tema**: Future-Ready Work & Economy
- **Program**: Coding Camp 2026 powered by DBS Foundation

---

## 📌 Deskripsi Proyek & Cakupan Analisis

Tantangan utama yang diselesaikan oleh subsistem ini adalah melakukan *Data Wrangling* dan *Exploratory Data Analysis* (EDA) terhadap **1.879 data lowongan kerja bersih** yang dikikis dari web (web-scraped). Data ini diolah untuk memberikan wawasan mendalam mengenai tren pasar kerja, keterampilan yang paling dicari perusahaan, serta distribusi gaji di berbagai kota besar di Indonesia.

Melalui repositori ini, data mentah ditransformasikan menjadi informasi terstruktur yang siap disajikan kepada pengguna akhir maupun digunakan sebagai basis data untuk pencocokan lowongan oleh tim AI/Machine Learning.

---

## 🛠️ Fitur Utama Dashboard (`app.py`)

Dashboard interaktif dikembangkan menggunakan **Streamlit** dan memiliki beberapa fitur utama:
1. **Pemuatan Data Efisien**: Menggunakan dekorator `@st.cache_data` untuk mengoptimalkan performa aplikasi saat membaca dataset berukuran besar (`glints_cleaned_for_model.csv`).
2. **Rekayasa Fitur Otomatis (*Feature Engineering*)**:
   - **Klasifikasi Level Gaji**: Mengonversi nilai nominal gaji menjadi kategori terstruktur:
     - 🟢 *Rendah* (< Rp5.000.000)
     - 🟡 *Menengah* (Rp5.000.000 - Rp10.000.000)
     - 🔴 *Tinggi* (> Rp10.000.000)
   - **Kalkulasi Intensitas Keterampilan**: Menghitung jumlah keterampilan (`Jumlah_Skill`) unik yang disyaratkan oleh masing-masing lowongan kerja.
3. **Visualisasi Data Interaktif**:
   - **10 Keterampilan Paling Dicari**: Grafik batang horizontal dinamis menggunakan *Seaborn* dan *Matplotlib* yang mengekstrak nilai dari kolom keterampilan terpisah.
   - **Rentang Gaji per Kota**: *Boxplot* distribusi gaji rata-rata untuk melihat kesenjangan pendapatan antar wilayah urban.
4. **Kamus Data Terintegrasi (*Data Dictionary*)**: Fitur dokumentasi interaktif menggunakan `st.expander` untuk memetakan kolom seperti `Judul`, `Industri`, `Tipe`, `Kota`, `Gaji_Rata_Rata`, `Skills`, `Level_Gaji`, dan lainnya.

---

## 📂 Struktur Repositori

Berikut adalah penjelasan fungsi dari setiap file yang ada di dalam repositori ini:

| Nama File | Deskripsi / Fungsi Utama |
| :--- | :--- |
| 📄 **`app.py`** | Script utama aplikasi **Streamlit** yang membangun antarmuka dashboard analisis lowongan kerja interaktif. |
| 📓 **`model.ipynb`** | *Jupyter Notebook* eksperimental yang digunakan untuk tahap awal pembersihan data (*data cleaning*), analisis statistik dasar, dan visualisasi distribusi data lowongan. |
| 📄 **`model.py`** | Refaktor script Python dari Notebook untuk mengotomatisasi pembersihan data, kalkulasi `Gaji_Rata_Rata`, serta pembuatan visualisasi EDA secara lokal. |
| 📊 **`glints_cleaned_for_model.csv`** | Dataset utama hasil kurasi yang berisi **1.879 baris data lowongan kerja** yang sudah bersih dan terstandardisasi. |
| 📋 **`requirements.txt`** | Daftar pustaka (*dependencies*) Python wajib yang diperlukan agar lingkungan lokal Anda dapat menjalankan seluruh kode tanpa hambatan. |

---

## 🚀 Panduan Menjalankan Proyek (Local Installation)

Ikuti langkah-langkah berikut untuk memasang dan menjalankan dashboard analisis di komputer lokal Anda:

### 1. Kloning Repositori
Buka terminal/command prompt Anda dan jalankan perintah berikut:
```bash
git clone [https://github.com/intaniaaaap/Career-Sync.git](https://github.com/intaniaaaap/Career-Sync.git)
cd Career-Sync
