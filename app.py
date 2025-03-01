from flask import Flask, request, jsonify
from recommendations import recommend_workout, predict_calories, predict_water_intake

app = Flask(__name__)

@app.route('/recommend_calories', methods=['POST'])
def calories():
    data = request.json
    calorie_intake = predict_calories(data["BMI"], data["Step Count"], data["Activity Level"])
    return jsonify({"recommended_calories": round(calorie_intake, 2)})

@app.route('/recommend_workout', methods=['POST'])
def workout():
    data = request.json
    recommendation = recommend_workout(data["BMI"], data["Activity Level"], data["Fitness Goal"], data["Step Count"])
    return jsonify(recommendation)

@app.route('/recommend_water', methods=['POST'])
def water():
    data = request.json
    water_intake = predict_water_intake(data["BMI"], data["Step Count"])
    return jsonify({"recommended_water_intake": round(water_intake, 2)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
