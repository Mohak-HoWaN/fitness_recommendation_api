import pandas as pd
from sklearn.preprocessing import MinMaxScaler, LabelEncoder

def preprocess_data(filepath="dataset.csv"):
    df = pd.read_csv(filepath)

    # Fill missing values
    df.fillna(df.mean(numeric_only=True), inplace=True)

    # Encoding categorical columns
    label_encoders = {}
    categorical_cols = ["Gender", "Activity Level", "Fitness Goal", "Suggested Workout Type"]

    for col in categorical_cols:
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])
        label_encoders[col] = le

    # Normalize numerical features
    scaler = MinMaxScaler()
    numerical_cols = ["BMI", "Step Count", "Daily Water Intake Goal (ml)"]
    df[numerical_cols] = scaler.fit_transform(df[numerical_cols])

    return df, label_encoders, scaler

if __name__ == "__main__":
    df, encoders, scaler = preprocess_data()
    print("Preprocessing done!")
