import streamlit as st
import numpy as np
import pandas as pd
import joblib

# =========================
# LOAD MODEL
# =========================
xgb = joblib.load("model_xgb.pkl")
svm = joblib.load("model_svm.pkl")
et = joblib.load("model_et.pkl")

scaler = joblib.load("scaler.pkl")
columns = joblib.load("columns.pkl")

# =========================
# TITLE
# =========================
st.title("🏥 Prediksi Kematian Pasien ICU")
st.write("Menggunakan 3 Model Machine Learning")

st.write("---")

# =========================
# INPUT USER
# =========================
st.subheader("📝 Input Data Pasien")

umur = st.number_input("Umur", value=60)
gender = st.selectbox("Gender", ["Male", "Female"])
bmi = st.number_input("BMI", value=25.0)
glukosa = st.number_input("Glukosa", value=150.0)
detak = st.number_input("Detak Jantung", value=90)
tekanan = st.number_input("Tekanan Darah", value=90)
icu_prob = st.number_input("Prob ICU", value=0.2)

st.write("---")

# =========================
# PREDIKSI
# =========================
if st.button("🔍 Prediksi"):

    gender_val = 1 if gender == "Male" else 0

    data = np.array([[ 
        umur, bmi, 170, gender_val, 0, 0, 2, 3,
        glukosa, icu_prob, icu_prob, tekanan,
        70, 30, 37, detak
    ]])

    # Feature engineering
    risk_mean = (data[:,9] + data[:,10]) / 2
    risk_diff = abs(data[:,9] - data[:,10])
    data = np.hstack((data, risk_mean.reshape(-1,1), risk_diff.reshape(-1,1)))

    df = pd.DataFrame(data, columns=columns)
    data_scaled = scaler.transform(df)

    # =========================
    # MODEL
    # =========================
    models = {
        "XGBoost": xgb,
        "SVM": svm,
        "Extra Trees": et
    }

    st.subheader("📊 Hasil Prediksi Model")

    results = []

    for name, model in models.items():
        pred = model.predict(data_scaled)[0]
        results.append(pred)

        if pred == 1:
            st.markdown(
                f"""
                <div style="
                    padding:15px;
                    border-radius:10px;
                    background-color:#3b0d0d;
                    color:white;
                    margin-bottom:10px;">
                    <b>{name}</b> → 🔴 Meninggal
                </div>
                """,
                unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style="
                    padding:15px;
                    border-radius:10px;
                    background-color:#0d3b1f;
                    color:white;
                    margin-bottom:10px;">
                    <b>{name}</b> → 🟢 Hidup
                </div>
                """,
                unsafe_allow_html=True
            )

    # =========================
    # KESIMPULAN
    # =========================
    st.write("---")
    st.subheader("🧠 Kesimpulan")

    if sum(results) >= 2:
        st.error("Mayoritas model memprediksi: 🔴 MENINGGAL")
    else:
        st.success("Mayoritas model memprediksi: 🟢 HIDUP")
