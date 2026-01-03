from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
import xgboost as xgb
import numpy as np

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests

# Load the XGBoost model from JSON format
model = xgb.XGBRegressor()
model.load_model("model.json")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        # Extract features from the request
        gender=  float(data['gender'])
        age = float(data['age'])
        height = float(data['height'])
        weight = float(data['weight'])
        duration= float(data['duration'])
        heartrate = float(data['heartrate'])
        bodytemp = float(data['bodytemp'])
        
        

        # Prepare the input for prediction
        features = np.array([[gender,age, height, weight, duration, heartrate, bodytemp]])

        # Make prediction
        prediction = model.predict(features)[0]

        return jsonify({"prediction": round(float(prediction), 2)})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=False) 
