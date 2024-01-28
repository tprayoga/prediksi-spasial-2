import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Fungsi untuk memuat model dari file pickle
def load_model():
    try:
        with open('model_RF_v2.pkl', 'rb') as file:
            model = pickle.load(file)
        return model
    except Exception as e:
        st.error(f'Error loading model: {e}')
        return None

# Tampilkan judul aplikasi
st.title('SapuJagad POC BMKG ')
st.subheader(' Prediksi curah hujan daerah Wamena, Cengkareng, Termindung')

# Memuat model
model = load_model()

# Memasukkan variabel input dari pengguna
suhu_titik_embun = st.slider('Suhu Titik Embun', min_value=0.00, max_value=100.0, value=15.0)
kelembapan = st.slider('Kelembapan', min_value=0, max_value=100, value=50)
suhu = st.slider('Suhu',min_value=-10.0, max_value=30.0, value=15.0)
evaporasi = st.slider('Evaporasi',min_value=0.00, max_value=30.0, value=15.0)
districts = ("Wamena", "Cengkareng", "Termindung")
district_values = {district: index for index, district in enumerate(districts)}
district = st.selectbox(
    "Select District?",
    districts,
    index=district_values["Wamena"], 
    placeholder="Select district..."
)
result_value = district_values[district]
st.write(f"The corresponding value for {district} is: {result_value}")

if model is not None:
    # Tombol untuk melakukan prediksi
    if st.button('Prediksi'):
        # Masukkan variabel input ke dalam dictionary
        input_df = pd.DataFrame({
        'suhutitikembun': [suhu_titik_embun],
        'suhu': [suhu],
        'evaporasi': [evaporasi],
        'kelembapan': [kelembapan],
        'district': result_value 
        })
        prediction = model.predict(input_df)
        hasil_prediksi =  prediction[0]

        if hasil_prediksi < 5:
            st.subheader(f"Hujan sangat ringan di daerah {district}")
        elif 5 <= hasil_prediksi <= 20:
            st.subheader(f"Hujan ringan di daerah {district}")
        elif 20 <= hasil_prediksi <= 50: 
            st.subheader(f"Hujan sedang di daerah {district}")
        elif 51 <= hasil_prediksi <= 100: 
            st.subheader(f"Hujan lebat di daerah {district}")
        else: 
            st.subheader("Hujan sangat lebat")
        st.success(f'Hasil prediksi:  {hasil_prediksi}')

        st.header("Prediksi wilayah lain :")
        for other_district, value in district_values.items():
            if other_district != district:
                input_df_2 = pd.DataFrame({
                'suhutitikembun': [suhu_titik_embun],
                'suhu': [suhu],
                'evaporasi': [evaporasi],
                'kelembapan': [kelembapan],
                'district': value 
                })
                st.text(value)
                prediction_2 = model.predict(input_df_2)
                hasil_prediksi_2 =  prediction_2[0]
                # Lakukan prediksi
                if hasil_prediksi_2 < 5:
                    st.subheader(f"Hujan sangat ringan kota {other_district}")
                elif 5 <= hasil_prediksi_2 <= 20:
                    st.subheader(f"Hujan ringan kota {other_district}")
                elif 20 <= hasil_prediksi_2 <= 50: 
                    st.subheader(f"Hujan sedang kota {other_district}")
                elif 51 <= hasil_prediksi_2 <= 100: 
                    st.subheader(f"Hujan lebat kota {other_district}")
                else: 
                    st.subheader(f"Hujan sangat lebat kota {other_district}")
                    
                st.success(f'Hasil prediksi  {hasil_prediksi_2}')
else:
    st.text("Belum ada library")

