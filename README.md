Student Performance Prediction Using Machine Learning

1. Project Overview

Student Performance Prediction is a machine learning-based project that predicts a student's expected final exam score using academic and lifestyle-related inputs.

2. Objectives

- Predict student performance using machine learning.
- Understand the role of study hours and attendance.
- Provide an interactive prediction interface.

3. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Streamlit
- VS Code

4. Input Features

- Hours Studied
- Attendance Percentage
- Previous Exam Score
- Sleep Hours

5. Machine Learning Algorithm

Random Forest Regression is used to train the model and predict student scores.

6. Model Evaluation

- Mean Absolute Error (MAE): 3.10
- R² Score: 0.869

These results were obtained using a synthetic sample dataset and should not be interpreted as real-world performance.

7. How to Run the Project

Install the required libraries:

python -m pip install pandas numpy scikit-learn streamlit

Run the prediction interface:

python -m streamlit run webapp.py

Run model evaluation:

python app.py

8. Dataset

The project uses 300 synthetically generated sample records for demonstration and model training.

9. Developer

Developed as an individual academic machine learning project.