import streamlit as st
import joblib
import pandas as pd

# ==================================
# Load Model
# ==================================

model = joblib.load("model-student.pkl")

# ==================================
# Konfigurasi Halaman
# ==================================

st.set_page_config(
    page_title="Prediksi Nilai Akhir Siswa",
    page_icon="🎓",
    layout="centered"
)

st.title("🎓 Prediksi Nilai Akhir Siswa")
st.caption("Dibuat oleh Rakaa.pkl")

st.write("""
Aplikasi ini memprediksi **Nilai Akhir Siswa (G3)** menggunakan algoritma **Random Forest Regressor**.

### Keterangan
- **G1** = Nilai Rata-rata Semester 1
- **G2** = Nilai Rata-rata Semester 2
- **G3** = Prediksi Nilai Akhir

### Kategori Nilai
🏆 **90 - 100** : Sangat Baik (Lulus)

🎉 **80 - 89** : Baik (Lulus)

❌ **0 - 79** : Tidak Lulus
""")

st.divider()

st.subheader("📋 Masukkan Data Siswa")

# ==================================
# INPUT
# ==================================

age = st.slider(
    "Usia",
    15,
    22,
    16
)

medu = st.selectbox(
    "Pendidikan Ibu",
    (
        "Tidak Sekolah",
        "SD",
        "SMP",
        "SMA",
        "Perguruan Tinggi"
    )
)

medu_dict = {
    "Tidak Sekolah": 0,
    "SD": 1,
    "SMP": 2,
    "SMA": 3,
    "Perguruan Tinggi": 4
}

medu = medu_dict[medu]

mjob = st.selectbox(
    "Pekerjaan Ibu",
    (
        "at_home",
        "health",
        "other",
        "services",
        "teacher"
    )
)

mjob_dict = {
    "at_home": 0,
    "health": 1,
    "other": 2,
    "services": 3,
    "teacher": 4
}

mjob = mjob_dict[mjob]

freetime = st.slider(
    "Waktu Luang Setelah Sekolah",
    1,
    5,
    3
)

goout = st.slider(
    "Frekuensi Keluar Bersama Teman",
    1,
    5,
    3
)

walc = st.slider(
    "Konsumsi Alkohol Saat Akhir Pekan",
    0,
    5,
    1
)

health = st.slider(
    "Kondisi Kesehatan",
    1,
    5,
    3
)

absences = st.number_input(
    "Jumlah Ketidakhadiran dalam 2 semester",
    min_value=0,
    value=0
)

g1 = st.slider(
    "Nilai Semester Rata-rata 1 (G1)",
    0,
    100,
    75
)

g2 = st.slider(
    "Nilai Semester Rata-rata 2 (G2)",
    0,
    100,
    75
)

st.divider()

# ==================================
# PREDIKSI
# ==================================

if st.button("🔍 Prediksi Nilai Akhir", use_container_width=True):

    data = pd.DataFrame([[
        age,
        medu,
        mjob,
        freetime,
        goout,
        walc,
        health,
        absences,
        g1,
        g2
    ]], columns=[
        "age",
        "Medu",
        "Mjob",
        "freetime",
        "goout",
        "Walc",
        "health",
        "absences",
        "G1",
        "G2"
    ])

    hasil = model.predict(data)[0]
    hasil = round(hasil)

    # Membatasi hasil prediksi
    hasil = max(0, min(100, hasil))

    st.subheader("📊 Hasil Prediksi")

    st.metric(
        label="Prediksi Nilai Akhir (G3)",
        value=f"{hasil}"
    )

    st.progress(hasil / 100)

    if hasil >= 90:

        st.balloons()

        st.success("""
### 🏆 Predikat : Sangat Baik

✅ **Status : LULUS**

Selamat! Nilai akhir sangat memuaskan.
""")

    elif hasil >= 80:

        st.success("""
### 🎉 Predikat : Baik

✅ **Status : LULUS**

Pertahankan prestasi belajarmu.
""")

    else:

        st.error("""
### ❌ Status : TIDAK LULUS

Nilai akhir masih di bawah standar kelulusan.
""")

        st.warning("""
### 💡 Saran

- Tingkatkan nilai Semester 1 dan Semester 2.
- Kurangi jumlah ketidakhadiran.
- Atur waktu luang dengan baik.
- Kurangi konsumsi alkohol saat akhir pekan.
- Jaga kesehatan agar proses belajar tetap optimal.
""")
