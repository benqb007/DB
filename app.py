from flask import Flask, request, jsonify
from joblib import load

app = Flask(__name__)

# Load your machine learning model
model = load('tuned_ridge_model.joblib')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    # Validate input data
    required_features = ['sbp', 'dbp', 'bmi', 'trig', 'hdl', 'total_chol', 'ldl']
    if not all(feature in data['features'] for feature in required_features):
        return jsonify({'error': 'Missing features'}), 400

    try:
        features = [
            data['features']['sbp'],
            data['features']['dbp'],
            data['features']['bmi'],
            data['features']['trig'],
            data['features']['hdl'],
            data['features']['total_chol'],
            data['features']['ldl']
        ]
        prediction = model.predict([features])
        return jsonify({'prediction': prediction.tolist()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)
