import streamlit as st
import pickle
import numpy as np

# # Fungsi untuk memuat model dari file pickle
def load_model():
    try:
        with open('model_RF_v2.pkl', 'rb') as file:
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
st.title('SapuJagad V1 Socket : 89 ')
st.subheader('Aplikasi prediksi curah hujan daerah Wamena, Cengkareng, Termindung')

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
        # Masukkan variabel input ke dalam list
        input_data = [suhu_titik_embun, kelembapan, suhu, evaporasi, result_value ]
        hasil_prediksi = predict(model, input_data)
        if hasil_prediksi < 5 :
            st.subheader("Hujan sangat ringan")
            st.success(f'Hasil prediksi:  {hasil_prediksi}')
        elif 5 <= hasil_prediksi <= 20:
            st.subheader("Hujan ringan")
            st.success(f'Hasil prediksi:  {hasil_prediksi}')
        elif 20 <= hasil_prediksi <= 50 : 
            st.subheader("Hujan sedang")
            st.success(f'Hasil prediksi:  {hasil_prediksi}')
        elif 51 <= hasil_prediksi <= 100 : 
            st.subheader("Hujan lebat")
        else : 
            st.subheader("Hujan sangat lebat")           
            st.success(f'Hasil prediksi: {hasil_prediksi}')

        st.header("Prediski wilayah lain")
        for other_district, value in district_values.items():
            if other_district != district:
                input_data_2 = [suhu_titik_embun, kelembapan, suhu, evaporasi, value ]
                # Lakukan prediksi
                hasil_prediksi_2 = predict(model,input_data_2)
                if hasil_prediksi_2 < 5 :
                    st.subheader(f"Hujan sangat ringan kota {other_district}")
                    st.success(f'Hasil prediksi  {hasil_prediksi_2}')
                elif 5 <= hasil_prediksi <= 20 or 5 <= hasil_prediksi_2 <= 20 :
                    st.subheader(f"Hujan ringan kota {other_district}")
                    st.success(f'Hasil prediksi  {hasil_prediksi_2}')
                elif 20 <= hasil_prediksi <= 50 or 20 <= hasil_prediksi_2 <= 50: 
                    st.subheader(f"Hujan sedang kota {other_district}")
                    st.success(f'Hasil prediksi  {hasil_prediksi_2}')
                elif 51 <= hasil_prediksi <= 100 : 
                    st.subheader(f"Hujan lebat kota {other_district}")
                    st.success(f'Hasil prediksi  {hasil_prediksi_2}')
                else : 
                    st.subheader(f"Hujan sangat lebat kota {other_district}")           
                    st.success(f'Hasil prediksi  {hasil_prediksi_2}')
else :
    st.text("belum ada library")        
