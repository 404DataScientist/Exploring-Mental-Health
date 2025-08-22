import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("Exploring-Mental-Health/model.pkl")

st.title("🧠 Mental Health Prediction App")

st.write("Fill in the details below to predict mental health outcome.")

# Input fields
gender = st.selectbox("Gender", ["Male", "Female", "Other"])
status = st.selectbox("Working Professional or Student", ["Student", "Working Professional"])
suicidal = st.selectbox("Have you ever had suicidal thoughts?", ["Yes", "No"])
family_history = st.selectbox("Family History of Mental Illness", ["Yes", "No"])
diet = st.selectbox("Dietary Habits", ["Healthy", "Unhealthy", "Moderate"])
field_study = st.text_input("Field of Study")
prof_field = st.text_input("Professional Field")
sleep_score = st.selectbox("Sleep Score", ["Poor", "Average", "Good"])

academic_pressure = st.slider("Academic Pressure (1-10)", 1, 10, 5)
work_pressure = st.slider("Work Pressure (1-10)", 1, 10, 5)
cgpa = st.number_input("CGPA", min_value=0.0, max_value=10.0, step=0.1)
study_satisfaction = st.slider("Study Satisfaction (1-10)", 1, 10, 5)
job_satisfaction = st.slider("Job Satisfaction (1-10)", 1, 10, 5)

# Prediction button
if st.button("Predict"):
    input_data = {
        "Gender": [gender],
        "Working Professional or Student": [status],
        "Have you ever had suicidal thoughts ?": [suicidal],
        "Family History of Mental Illness": [family_history],
        "Dietary Habits": [diet],
        "FieldOfStudy": [field_study],
        "ProfessionalField": [prof_field],
        "SleepScore": [sleep_score],
        "Academic Pressure": [academic_pressure],
        "Work Pressure": [work_pressure],
        "CGPA": [cgpa],
        "Study Satisfaction": [study_satisfaction],
        "Job Satisfaction": [job_satisfaction]
    }

    features_df = pd.DataFrame(input_data)

    prediction = model.predict(features_df)[0]

    st.success(f"### Prediction: {prediction}")
