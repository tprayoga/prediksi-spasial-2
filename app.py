import streamlit as st
import pickle
import numpy as np

# # Fungsi untuk memuat model dari file pickle
def load_model():
    try:
        with open('model_RF.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f'Error loading model: {e}')
        return None

# Fungsi untuk melakukan prediksi
def predict(model, input_data):
    input_array = np.array(input_data).reshape(1, -1)
    prediction = model.predict(input_array)
    return prediction[0]

# Tampilkan judul aplikasi
st.title('SapuJagad V1 Socket : 89')
st.title('Aplikasi Prediksi Curah Hujan')

# Memuat model
model = load_model()

# 'suhutitikembun','suhu','evaporasi','kelembapan','district'
# Memasukkan variabel input dari pengguna
suhu_titik_embun = st.slider('Suhu Titik Embun', min_value=-10.0, max_value=30.0, value=15.0)
kelembapan = st.slider('Kelembapan', min_value=0, max_value=100, value=50)
suhu = st.slider('Suhu',min_value=-10.0, max_value=30.0, value=15.0)
evaporasi = st.slider('Evaporasi',min_value=-10.0, max_value=30.0, value=15.0)

if model is not None:
# Tombol untuk melakukan prediksi
    if st.button('Prediksi'):
        # Masukkan variabel input ke dalam list
        input_data = [suhu_titik_embun, kelembapan, suhu, evaporasi ]  # Tambahkan variabel input lainnya sesuai kebutuhan
        # Lakukan prediksi
        hasil_prediksi = predict(model, input_data)
        # Tampilkan hasil prediksi
        st.success(f'Hasil prediksi: {hasil_prediksi}')
else :
    st.text("belum ada library")        
