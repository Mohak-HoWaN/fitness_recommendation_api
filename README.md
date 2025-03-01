# **📌 Fitness Recommendation API**  

🚀 **Deployed at:** [`https://fitness-recommendation-api.onrender.com`](https://fitness-recommendation-api.onrender.com)  
Odoo x Charusat

This API provides **personalized fitness recommendations**, including **workout suggestions, calorie intake, and water intake predictions**, based on user data such as **BMI, step count, and activity level**.  

---

## **📌 Endpoints & Usage**  

### **1️⃣ Recommend Workout**
- **Endpoint:** `POST /recommend_workout`
- **Description:** Suggests a workout type based on user fitness data.  
- **Request Body (JSON):**  
  ```json
  {
    "BMI": 24.5,
    "Step Count": 8000,
    "Activity Level": 2
  }
Response (JSON):
json
```
{
  "Suggested Workout Type": "Cardio"
}
```

📌 Example cURL Request:

bash
```
curl -X POST https://fitness-recommendation-api.onrender.com/recommend_workout \
-H "Content-Type: application/json" \
-d '{"BMI": 24.5, "Step Count": 8000, "Activity Level": 2}'
```

2️⃣ Predict Calorie Intake
Endpoint: POST /recommend_calories
Description: Predicts the ideal daily calorie intake.
Request Body (JSON):
json
```
{
  "BMI": 24.5,
  "Step Count": 8000,
  "Activity Level": 2
}
```
Response (JSON):
json
```
{
  "Recommended Daily Calories": 2200
}
```
📌 Example cURL Request:

bash
```
curl -X POST https://fitness-recommendation-api.onrender.com/recommend_calories \
-H "Content-Type: application/json" \
-d '{"BMI": 24.5, "Step Count": 8000, "Activity Level": 2}'
```
3️⃣ Predict Water Intake
Endpoint: POST /recommend_water
Description: Predicts the ideal daily water intake.
Request Body (JSON):
json
```
{
  "BMI": 24.5,
  "Step Count": 8000
}
```
Response (JSON):
json
```
{
  "Recommended Daily Water Intake (ml)": 2500
}
```
📌 Example cURL Request:

bash
```
curl -X POST https://fitness-recommendation-api.onrender.com/recommend_water \
-H "Content-Type: application/json" \
-d '{"BMI": 24.5, "Step Count": 8000}'
```

📌 How to Integrate in Frontend
🔹 JavaScript (Fetch API)
javascript
```
fetch("https://fitness-recommendation-api.onrender.com/recommend_calories", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({ BMI: 24.5, "Step Count": 8000, "Activity Level": 2 })
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error("Error:", error));
  ```

🔹 Python (Requests)\
python\
```
import requests

url = "https://fitness-recommendation-api.onrender.com/recommend_calories"
data = {"BMI": 24.5, "Step Count": 8000, "Activity Level": 2}
response = requests.post(url, json=data)
print(response.json())
```

📌 Deployment Details
Framework: Flask
Model Storage: Joblib (models/workout_recommender.pkl, etc.)
Hosting: Render
Port: 5000 (Default Flask)
📌 Common Issues & Fixes
❌ Getting 404 Not Found?
✔ Ensure you are using the correct endpoint and method (POST).

❌ Model File Not Found (FileNotFoundError)?
✔ Ensure the models/ directory contains the required .pkl files.

❌ CORS Issues in Frontend?
✔ Use the Flask-CORS package:

python
```
from flask_cors import CORS
CORS(app)
```

📌 Future Improvements
✅ Add user authentication for personalized tracking
✅ Improve recommendation accuracy using advanced ML models
✅ Optimize deployment for faster API response times