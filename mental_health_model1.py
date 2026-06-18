import streamlit as st
from PIL import Image
import joblib
import numpy as np

#load model & encoders
model = joblib.load("mental_health.pkl")
scaler = joblib.load("scaler.pkl")
le0=joblib.load('le0.pkl')
le1=joblib.load('le1.pkl')
le2=joblib.load('le2.pkl')
le3=joblib.load('le3.pkl')


st.set_page_config(page_title="Mental Health Prediction")
st.title("Mental Health Disorder Prediction")

# ---------------- FORM ---------------- #

Gender = st.selectbox("Gender", ["Male", "Female", "Other"])
Age = st.number_input("Age", min_value=18, max_value=80)
City = st.selectbox("City", ["Urban", "Rural"])
Education = st.number_input('Enter your Education:',1, 4)
IncomeRate = st.number_input("Income Rate (0–5)", 0, 5)
DepressionScore = st.number_input("Depression Score", 0, 100)
AnxietyScore = st.number_input("Anxiety Score", 0, 100)
StressScore = st.number_input("Stress Score", 0, 100)
SuicideRiskScore = st.number_input("Suicide Risk Score", 0, 100)
TreatmentAccess = st.selectbox("Treatment Access", ["Yes", "No"])

    

# ------------- PREDICTION LOGIC ------------- #
if st.button('Predict'):
        try:
                Gender = le0.transform([Gender])[0]
                City = le1.transform([City])[0]
                Treatment = le2.transform([TreatmentAccess])[0]



                input_data =  np.array([[  
                        Age,Gender,Education,City,IncomeRate,DepressionScore,AnxietyScore,StressScore,SuicideRiskScore,Treatment]])

                scaled_input = scaler.transform(input_data)
                
                prediction = model.predict(scaled_input)[0]

                if prediction == 1:
                        st.write("Diagnosed Mental Health Disorder Detected")
                else:
                        st.write("No Diagnosed Mental Health Disorder")

        except Exception as e:
                st.error(f'Error in prediction: {e}')