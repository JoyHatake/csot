from flask import Flask, request, jsonify
import joblib
import numpy as np

app = Flask(__name__)
model = joblib.load('like_predictor3.pkl')

weekdayOHE = {'friday': [1, 0, 0, 0, 0, 0, 0],
     'monday': [0, 1, 0, 0, 0, 0, 0],
     'saturday': [0, 0, 1, 0, 0, 0, 0],
     'sunday': [0, 0, 0, 1, 0, 0, 0],
     'thursday': [0, 0, 0, 0, 1, 0, 0],
     'tuesday': [0, 0, 0, 0, 0, 1, 0],
     'wednesday': [0, 0, 0, 0, 0, 0, 1]}

@app.route('/predict', methods=['POST', 'GET'])



def predict():
    data = request.get_json()
    features = np.array([
        data['word_count'],
        data['char_count'],
        data['has_media'],
        data['hour'],
        data['sentiment'],
        data['company_avg_likes']
    ] + [i for i in weekdayOHE[data['weekday']]]).reshape(1, -1)

    prediction = model.predict(features)[0]
    return jsonify({'predicted_likes': int(np.expm1(prediction))})

if __name__ == '__main__':
    app.run(debug=True)