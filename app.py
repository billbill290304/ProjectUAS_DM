import streamlit as st
import numpy as np
import joblib

# Load model dan encoder
model = joblib.load("svm_model_kerala.joblib")
encoder = joblib.load("label_encoder_kerala.joblib")

st.set_page_config(page_title="Prediksi Curah Hujan", layout="centered")
st.title("☁️ Prediksi Kemungkinan Banjir")

st.markdown("Masukkan data curah hujan (dalam mm) untuk setiap bulan.")

# Input bulan
jan = st.number_input("Januari", value=0.0)
feb = st.number_input("Februari", value=0.0)
mar = st.number_input("Maret", value=0.0)
apr = st.number_input("April", value=0.0)
may = st.number_input("Mei", value=0.0)
jun = st.number_input("Juni", value=0.0)
jul = st.number_input("Juli", value=0.0)
aug = st.number_input("Agustus", value=0.0)
sep = st.number_input("September", value=0.0)
oct = st.number_input("Oktober", value=0.0)
nov = st.number_input("November", value=0.0)
dec = st.number_input("Desember", value=0.0)

# Tombol "Tambah" untuk menjumlahkan curah hujan
col1, col2 = st.columns([3, 1])

with col1:
    st.markdown("### 🌧️ Total Curah Hujan Tahunan:")

with col2:
    if st.button("Tambah"):
        total = jan + feb + mar + apr + may + jun + jul + aug + sep + oct + nov + dec
        st.session_state['annual'] = total

# Tampilkan hasil penjumlahan jika sudah ditekan
if 'annual' in st.session_state:
    st.markdown(f"### **{st.session_state['annual']:.2f} mm**")

# Tombol prediksi
if st.button("Prediksi"):
    if 'annual' not in st.session_state:
        st.warning("Silakan tekan tombol Tambah dulu untuk menghitung total curah hujan.")
    else:
        data = np.array([[jan, feb, mar, apr, may, jun, jul, aug, sep, oct, nov, dec, st.session_state['annual']]])
        hasil_prediksi = model.predict(data)
        hasil_label = encoder.inverse_transform(hasil_prediksi)
        st.success(f"✅ Hasil Prediksi: **{hasil_label[0]}**")
