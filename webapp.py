import os
import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

# Page Configuration
st.set_page_config(
    page_title="Student Performance Prediction",
    page_icon="🎓",
    layout="centered"
)

# Load Dataset
data_path = "student_data.csv" if os.path.exists("student_data.csv") else "dataset/student_data.csv"
data = pd.read_csv(data_path)

# Train Model
X = data[[
    "Hours_Studied",
    "Attendance",
    "Previous_Score",
    "Sleep_Hours"
]]

y = data["Final_Score"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

# Website Title
st.title("🎓 Student Performance Prediction")
st.write("Machine Learning Based Student Score Prediction System")

st.divider()

# User Input
st.subheader("Enter Student Details")

hours = st.number_input(
    "Daily Study Hours",
    min_value=0.0,
    max_value=24.0,
    value=6.0
)

attendance = st.slider(
    "Attendance Percentage",
    min_value=0,
    max_value=100,
    value=80
)

previous_score = st.number_input(
    "Previous Exam Score",
    min_value=0,
    max_value=100,
    value=65
)

sleep = st.slider(
    "Daily Sleep Hours",
    min_value=0,
    max_value=24,
    value=7
)

# Prediction Button
if st.button("Predict Student Performance"):

    new_student = pd.DataFrame([{
        "Hours_Studied": hours,
        "Attendance": attendance,
        "Previous_Score": previous_score,
        "Sleep_Hours": sleep
    }])

    prediction = model.predict(new_student)

    st.success("Prediction Completed!")

    st.metric(
        "Predicted Student Score",
        f"{prediction[0]:.2f} / 100"
    )

st.divider()

st.caption("Developed using Python, Pandas, Scikit-learn and Streamlit.")
