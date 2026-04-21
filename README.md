## 🤖 Model Inference (GUI)

Model diimplementasikan dalam bentuk GUI interaktif untuk mensimulasikan prediksi kondisi pasien ICU berdasarkan beberapa fitur klinis seperti umur, gender, BMI, kadar glukosa, detak jantung, tekanan darah, dan probabilitas ICU. Pengguna dapat memilih algoritma yang digunakan, yaitu XGBoost, SVM, dan Extra Trees.

<p align="center">
  <img src="https://github.com/user-attachments/assets/d1af25ad-2a5f-4505-aeec-57b14acf6758" width="30%">
  <img src="https://github.com/user-attachments/assets/ea9a3430-9ec3-41ab-8b2c-3fef0c3be328" width="30%">
  <img src="https://github.com/user-attachments/assets/e834eb83-f8bf-40dc-9dc0-ca64ec5e1bae" width="30%">
</p>

<p align="center">
  🔴 XGBoost (Meninggal) &nbsp;&nbsp;
  🔴 SVM (Meninggal) &nbsp;&nbsp;
  🟢 Extra Trees (Hidup)
</p>

Hasil menunjukkan bahwa dua model memprediksi pasien meninggal, sedangkan satu model memprediksi hidup. Perbedaan ini terjadi karena setiap algoritma memiliki cara belajar dan pengambilan keputusan yang berbeda terhadap data.

**Catatan:** GUI dibuat menggunakan *ipywidgets*, sehingga hanya dapat dijalankan di Google Colab atau Jupyter Notebook. Output hasil eksekusi (seperti tampilan GUI dan hasil prediksi) tidak ikut tersimpan atau ditampilkan di GitHub, sehingga hanya ditampilkan dalam bentuk screenshot
