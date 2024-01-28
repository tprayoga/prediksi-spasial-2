import streamlit as st
import pandas as pd
import joblib

# Load the models
loaded_model_cengkareng = joblib.load("model_V1.sav")
loaded_model_temindung_wamena = joblib.load("model_V2.sav")

# Streamlit App
st.title("Curah Hujan Spasial")

# Input for Cengkareng Model
cengkareng_input = st.number_input("Curah Hujan Cengkareng", min_value=0.0, max_value=1000.0, value=0.0, step=1.0)

# Make prediction using Cengkareng Model
input_cengkareng = pd.DataFrame([[cengkareng_input]], columns=['cengkareng'], dtype=float)
prediction_cengkareng = loaded_model_cengkareng.predict(input_cengkareng)[0]

# Display result for Cengkareng Model
st.write("Curah Hujan Temindung:", prediction_cengkareng[0])
st.write("Curah Hujan Wamena:", prediction_cengkareng[1])

# Input for Temindung-Wamena Model
temindung_input = st.number_input("Curah Hujan Temindung", min_value=0.0, max_value=1000.0, value=0.0, step=1.0)
wamena_input = st.number_input("Curah Hujan Wamena", min_value=0.0, max_value=1000.0, value=0.0, step=1.0)

# Make prediction using Temindung-Wamena Model
input_temindung_wamena = pd.DataFrame([[temindung_input, wamena_input]], columns=['Temindung', 'Wamena'], dtype=float)
prediction_temindung_wamena = loaded_model_temindung_wamena.predict(input_temindung_wamena)[0]

# Display result for Temindung-Wamena Model
st.write("Curah Hujan Cengkareng:", prediction_temindung_wamena)

