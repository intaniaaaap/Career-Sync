import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Set Judul Dashboard
st.set_page_config(page_title="CareerSync Analytics", layout="wide")
st.title("📊 Dashboard Analisis Lowongan Kerja CareerSync")
st.write("Menampilkan insight dari 1879 data lowongan kerja bersih.")

# 1. Load Data
@st.cache_data
def load_data():
    return pd.read_csv('glints_cleaned_for_model.csv')

df_raw = load_data()

# --- TAHAP FEATURE ENGINEERING ---
df = df_raw.copy()

# A. Membuat Kolom "Level_Gaji"
def klasifikasi_gaji(gaji):
    if gaji < 5000000:
        return 'Rendah (< 5jt)'
    elif 5000000 <= gaji <= 10000000:
        return 'Menengah (5jt - 10jt)'
    else:
        return 'Tinggi (> 10jt)'

df['Level_Gaji'] = df['Gaji_Rata_Rata'].apply(klasifikasi_gaji)

# B. Menghitung Jumlah Skill per Lowongan
df['Jumlah_Skill'] = df['Skills'].apply(lambda x: len(str(x).split(',')) if pd.notnull(x) else 0)

# C. Pengelompokan Wilayah
jabodetabek = ['Jakarta Selatan', 'Jakarta Barat', 'Jakarta Utara', 'Jakarta Pusat', 'Jakarta Timur', 'Bogor', 'Depok', 'Tangerang', 'Bekasi']
df['Wilayah'] = df['Kota'].apply(lambda x: 'Jabodetabek' if x in jabodetabek else 'Luar Jabodetabek')

# --- TAHAP A/B TESTING (STATISTIK) ---
# Membandingkan gaji Jabodetabek vs Luar Jabodetabek
gaji_jkt = df[df['Wilayah'] == 'Jabodetabek']['Gaji_Rata_Rata'].dropna()
gaji_luar = df[df['Wilayah'] == 'Luar Jabodetabek']['Gaji_Rata_Rata'].dropna()
t_stat, p_val = stats.ttest_ind(gaji_jkt, gaji_luar, equal_var=False)

# 2. Sidebar untuk Filter
st.sidebar.header("Filter Data")
kota_pilihan = st.sidebar.multiselect("Pilih Kota:", 
                                     options=df['Kota'].unique(),
                                     default=df['Kota'].value_counts().head(5).index.tolist())

# Filter data berdasarkan pilihan
df_selection = df[df['Kota'].isin(kota_pilihan)]

# 3. Menampilkan Metrik Utama
col1, col2, col3 = st.columns(3)
col1.metric("Total Lowongan", len(df_selection))
col2.metric("Rata-rata Gaji", f"Rp {df_selection['Gaji_Rata_Rata'].mean():,.0f}")
col3.metric("Top Skill", "Microsoft Excel")

st.divider()

# --- BAGIAN HASIL ANALISIS ---
tab1, tab2, tab3 = st.tabs(["🛠️ Feature Engineering", "🧪 A/B Testing", "📈 Visualisasi"])

with tab1:
    st.subheader("Data Hasil Transformasi")
    st.write("Kolom baru: Level_Gaji, Jumlah_Skill, dan Wilayah.")
    st.dataframe(df_selection[['Judul', 'Kota', 'Level_Gaji', 'Jumlah_Skill', 'Wilayah']].head(10))

with tab2:
    st.subheader("Uji Hipotesis Statistik (T-Test)")
    st.write("Menguji perbedaan rata-rata gaji antara Jabodetabek vs Luar Jabodetabek.")
    
    c1, c2 = st.columns(2)
    with c1:
        st.latex(r"H_0: \mu_{jabodetabek} = \mu_{luar}")
        st.latex(r"H_1: \mu_{jabodetabek} \neq \mu_{luar}")
        st.metric("P-Value", f"{p_val:.5f}")
    
    with c2:
        if p_val < 0.05:
            st.success("✅ **Hasil Signifikan:** Terdapat perbedaan rata-rata gaji yang nyata secara statistik.")
        else:
            st.warning("⚠️ **Hasil Tidak Signifikan:** Tidak ditemukan bukti perbedaan gaji yang nyata.")
            
    # Grafik Distribusi Gaji
    fig_ab, ax_ab = plt.subplots(figsize=(10, 4))
    sns.kdeplot(gaji_jkt, label='Jabodetabek', fill=True, ax=ax_ab)
    sns.kdeplot(gaji_luar, label='Luar Jabodetabek', fill=True, ax=ax_ab)
    plt.title("Perbandingan Distribusi Gaji")
    plt.legend()
    st.pyplot(fig_ab)

with tab3:
    col_l, col_r = st.columns(2)
    with col_l:
        st.subheader("10 Keterampilan Paling Dicari")
        skills_series = df_selection['Skills'].dropna().str.split(',').explode().str.strip()
        top_skills = skills_series.value_counts().head(10)
        fig, ax = plt.subplots()
        sns.barplot(x=top_skills.values, y=top_skills.index, ax=ax, palette='viridis')
        st.pyplot(fig)
    
    with col_r:
        st.subheader("Rentang Gaji per Kota")
        fig2, ax2 = plt.subplots()
        sns.boxplot(data=df_selection, x='Kota', y='Gaji_Rata_Rata', ax=ax2)
        plt.xticks(rotation=45)
        st.pyplot(fig2)

# 5. Data Dictionary Section
st.write("---")
with st.expander("📖 Lihat Kamus Data (Data Dictionary)"):
    data_dict = {
        "Nama Kolom": ["Judul", "Industri", "Tipe", "Kota", "Gaji_Rata_Rata", "Skills", "Level_Gaji", "Jumlah_Skill", "Wilayah"],
        "Deskripsi": [
            "Nama jabatan pekerjaan.", "Sektor industri.", "Jenis kontrak kerja.", "Lokasi penempatan.",
            "Nilai tengah gaji.", "Daftar skill yang diminta.", "Kategori gaji (Rendah/Menengah/Tinggi).",
            "Total jumlah skill.", "Pengelompokan lokasi ekonomi."
        ],
        "Tipe Data": ["Kategorikal", "Kategorikal", "Kategorikal", "Kategorikal", "Numerik", "Teks", "Kategorikal (Baru)", "Numerik (Baru)", "Kategorikal (Baru)"]
    }
    st.table(pd.DataFrame(data_dict))

st.write("© 2026 CareerSync Team - Data Science Division") 