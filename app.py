import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# Step 1: Load Dataset
data = pd.read_csv("dataset/student_data.csv")

# Step 2: Select Input and Output
X = data[["Hours_Studied", "Attendance",
          "Previous_Score", "Sleep_Hours"]]

y = data["Final_Score"]

# Step 3: Split Dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 4: Create Model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Step 5: Train Model
model.fit(X_train, y_train)

# Step 6: Make Prediction
predictions = model.predict(X_test)

# Step 7: Evaluate Model
print("Model Training Successful!")
print("Mean Absolute Error:", mean_absolute_error(y_test, predictions))
print("R2 Score:", r2_score(y_test, predictions))

# Step 8: Predict New Student Performance
new_student = pd.DataFrame([{
    "Hours_Studied": 6,
    "Attendance": 80,
    "Previous_Score": 65,
    "Sleep_Hours": 7
}])

result = model.predict(new_student)

print("\nPredicted Student Score:", round(result[0], 2))