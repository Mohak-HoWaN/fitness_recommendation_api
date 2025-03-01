import pandas as pd
import joblib
from sklearn.neighbors import NearestNeighbors
from sklearn.ensemble import RandomForestRegressor
from data_preprocess import preprocess_data

# Load dataset
df, label_encoders, scaler = preprocess_data()

# 🔹 Content-Based Filtering (Workout Recommendations)
workout_features = df[["BMI", "Activity Level", "Fitness Goal", "Step Count"]]
knn_model = NearestNeighbors(n_neighbors=5, metric='cosine')
knn_model.fit(workout_features)

# 🔹 Regression Model (Calorie Prediction)
calorie_model = RandomForestRegressor(n_estimators=100, random_state=42)
calorie_model.fit(df[["BMI", "Step Count", "Activity Level"]], df["Recommended Daily Calories Intake"])

# 🔹 Water Intake Prediction
water_model = RandomForestRegressor(n_estimators=100, random_state=42)
water_model.fit(df[["BMI", "Step Count"]], df["Recommended Daily Water Intake (ml)"])

# Save models
joblib.dump(knn_model, "models/workout_recommender.pkl")
joblib.dump(calorie_model, "models/calorie_predictor.pkl")
joblib.dump(water_model, "models/water_intake_predictor.pkl")
joblib.dump(label_encoders, "models/label_encoders.pkl")
joblib.dump(scaler, "models/scaler.pkl")

print("Models trained and saved successfully!")
