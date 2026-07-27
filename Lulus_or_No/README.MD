# 🎓 Student Final Grade Prediction

Aplikasi Machine Learning untuk memprediksi **Nilai Akhir Siswa (G3)** menggunakan algoritma **Random Forest Regressor** dan dideploy menggunakan **Streamlit**.

---

## 📌 Tentang Project

Project ini bertujuan memprediksi **Nilai Akhir (G3)** seorang siswa berdasarkan beberapa faktor akademik dan non-akademik.

Selain membangun model Machine Learning, project ini juga mencakup proses:

- Exploratory Data Analysis (EDA)
- Data Preprocessing
- Label Encoding
- Feature Selection
- Model Training
- Model Evaluation
- Deployment menggunakan Streamlit

---

## 📂 Dataset

Dataset yang digunakan merupakan **Student Performance Dataset**.

Target yang diprediksi adalah:

- **G3 (Nilai Akhir)**

---

## 🧠 Algoritma

Model yang digunakan:

- Random Forest Regressor

Alasan memilih algoritma ini:

- Mampu menangani hubungan non-linear.
- Tidak memerlukan normalisasi data.
- Cocok untuk data dengan banyak fitur.
- Memiliki performa yang baik pada dataset ini.

---

## 📊 Exploratory Data Analysis

Tahapan EDA yang dilakukan:

- Bar fitur selection
- Bar female or male
- Heatmap Korelasi

---

## 🔧 Data Preprocessing

Tahapan preprocessing:

- Menghapus data yang tidak diperlukan
- Label Encoding untuk fitur kategorikal
- Memisahkan fitur dan target

---

## 🎯 Feature Selection

Project ini membandingkan tiga metode Feature Selection:

- Filter Method
- Embedded Method
- Wrapper Method

Hasil terbaik diperoleh menggunakan **Wrapper Method**.

### Fitur Terpilih

### Fitur Terpilih (Wrapper Method)

| No | Fitur | Deskripsi |
|----|-------|-----------|
|1|Age|Usia siswa|
|2|Mother Education (Medu)|Tingkat pendidikan ibu|
|3|Mother Job (Mjob)|Pekerjaan ibu|
|4|Free Time (freetime)|Waktu luang setelah sekolah|
|5|Go Out (goout)|Frekuensi keluar bersama teman|
|6|Weekend Alcohol Consumption (Walc)|Tingkat konsumsi alkohol pada akhir pekan|
|7|Health|Kondisi kesehatan siswa|
|8|Absences|Jumlah ketidakhadiran|
|9|Semester 1 Score (G1)|Nilai Rata-rata Semester 1|
|10|Semester 2 Score (G2)|Nilai Rata-rata Semester 2|

---

## 📈 Model Evaluation

Model dievaluasi menggunakan:

- MAE (Mean Absolute Error)
- MSE (Mean Squared Error)
- RMSE (Root Mean Squared Error)
- R² Score

---

## 💻 Streamlit App

Aplikasi memungkinkan pengguna memasukkan data siswa kemudian memprediksi:

- Nilai Akhir (G3)
- Status Kelulusan
- Predikat Nilai

Kategori:

| Nilai | Status |
|--------|--------|
|90 - 100|🏆 Sangat Baik|
|80 - 89|🎉 Baik|
|0 - 79|❌ Tidak Lulus|

---

## 🛠️ Library

```text
Python
Pandas
NumPy
Matplotlib
Seaborn
Scikit-Learn
Joblib
Streamlit
```

---

## 📁 Struktur Project

```text
Student-Final-Grade-Prediction/
│
├── app.py
├── model_student.pkl
├── notebook.ipynb
├── student-mat.csv
├── requirements.txt
├── README.md
```

---

## ▶️ Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/anggaraniirma-cmy/Lulus_or_No.git
```

### 2. Masuk ke Folder

```bash
cd Lulus_or_NO
```

### 3. Install Library

```bash
pip install -r requirements.txt
```

### 4. Jalankan Streamlit

```bash
streamlit run app.py
```

---


## 🚀 Hasil Project

Project ini berhasil:

- Melakukan analisis data siswa.
- Memilih fitur terbaik menggunakan Wrapper Method.
- Melatih model Random Forest Regressor.
- Mengevaluasi performa model menggunakan beberapa metrik.
- Mendeploy model menjadi aplikasi web menggunakan Streamlit.

---

## 👨‍💻 Author

**Raka**

SMK Telkom Sidoarjo

AI & Machine Learning Enthusiast

GitHub : https://github.com/anggaraniirma-cmy
