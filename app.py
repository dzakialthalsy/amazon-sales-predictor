from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load model
MODEL_PATH = os.path.join(os.path.dirname(__file__), 'model.joblib')

# Cek apakah model ada, jika tidak coba download dari Hugging Face
if not os.path.exists(MODEL_PATH):
    print("Model not found locally. Trying to download from Hugging Face...")
    try:
        from huggingface_hub import hf_hub_download
        # Hugging Face repo
        HF_REPO_ID = "dz4ic7/amazon-sales-predictor"
        MODEL_PATH = hf_hub_download(repo_id=HF_REPO_ID, filename="model.joblib", local_dir=os.path.dirname(__file__))
        print(f"Model downloaded successfully from Hugging Face: {MODEL_PATH}")
    except Exception as e:
        print(f"Failed to download model: {e}")
        print("Please download model manually and place it in the project folder.")
        raise

model = joblib.load(MODEL_PATH)

# Feature names
FEATURE_NAMES = ['Stock', 'index_sales_int', 'PCS', 'RATE', 'GROSS AMT', 'Qty', 'ship-postal-code']


@app.route('/')
def index():
    return render_template('index.html', feature_names=FEATURE_NAMES)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input data from form
        features = []
        for feature in FEATURE_NAMES:
            value = request.form.get(feature)
            if value is None or value == '':
                return jsonify({'error': f'Please fill in all fields. {feature} is missing.'}), 400
            features.append(float(value))
        
        # Create numpy array and reshape for prediction
        features_array = np.array(features).reshape(1, -1)
        
        # Make prediction
        prediction = model.predict(features_array)
        
        # Get the predicted value
        predicted_sales = prediction[0]
        
        return render_template(
            'index.html',
            feature_names=FEATURE_NAMES,
            prediction=predicted_sales,
            input_values=request.form
        )
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/predict-api', methods=['POST'])
def predict_api():
    """API endpoint for JSON requests"""
    try:
        data = request.get_json()
        
        if data is None:
            return jsonify({'error': 'Please provide JSON data'}), 400
        
        features = []
        for feature in FEATURE_NAMES:
            if feature not in data:
                return jsonify({'error': f'Missing feature: {feature}'}), 400
            features.append(float(data[feature]))
        
        features_array = np.array(features).reshape(1, -1)
        prediction = model.predict(features_array)
        
        return jsonify({
            'prediction': prediction[0],
            'features': dict(zip(FEATURE_NAMES, features))
        })
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
