import pandas as pd
import numpy as np

np.random.seed(42)

records = 300

hours = np.random.uniform(1, 10, records)
attendance = np.random.uniform(40, 100, records)
previous_score = np.random.uniform(30, 95, records)
sleep = np.random.uniform(4, 10, records)

final_score = (
    0.45 * previous_score
    + 2.5 * hours
    + 0.20 * attendance
    + 1.2 * sleep
    + np.random.normal(0, 3, records)
)

final_score = np.clip(final_score, 0, 100)

data = pd.DataFrame({
    "Hours_Studied": hours.round(1),
    "Attendance": attendance.round(1),
    "Previous_Score": previous_score.round(1),
    "Sleep_Hours": sleep.round(1),
    "Final_Score": final_score.round(1)
})

data.to_csv("dataset/student_data.csv", index=False)

print("300 sample records generated successfully!")
print(data.head())