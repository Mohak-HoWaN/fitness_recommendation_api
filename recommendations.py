import joblib
import numpy as np
import pandas as pd

# Load models
knn_model = joblib.load("models/workout_recommender.pkl")
calorie_model = joblib.load("models/calorie_predictor.pkl")
water_model = joblib.load("models/water_intake_predictor.pkl")
label_encoders = joblib.load("models/label_encoders.pkl")
scaler = joblib.load("models/scaler.pkl")

# Load dataset to map indices back to workout types
df = pd.read_csv("dataset.csv")

def recommend_workout(bmi, activity_level, fitness_goal, step_count):
    user_data = np.array([[bmi, activity_level, fitness_goal, step_count]])
    
    # Find the 5 nearest neighbors
    _, indices = knn_model.kneighbors(user_data)

    # Get workout types from dataset
    recommended_workouts = df.iloc[indices[0]]["Suggested Workout Type"].values.tolist()
    
    return {"Suggested Workouts": recommended_workouts}

def predict_calories(bmi, step_count, activity_level):
    return calorie_model.predict([[bmi, step_count, activity_level]])[0]

def predict_water_intake(bmi, step_count):
    return water_model.predict([[bmi, step_count]])[0]
