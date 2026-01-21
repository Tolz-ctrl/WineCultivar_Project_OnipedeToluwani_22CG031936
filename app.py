"""
Wine Cultivar Origin Prediction System
Flask Web Application

This application loads a trained machine learning model and allows users
to predict wine cultivar origin based on chemical properties.
"""

from flask import Flask, render_template, request
import joblib
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Define paths to model and scaler files
MODEL_PATH = os.path.join('model', 'wine_cultivar_model.pkl')
SCALER_PATH = os.path.join('model', 'scaler.pkl')

# Load the trained model and scaler
try:
    model = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    print("✓ Model and scaler loaded successfully!")
except Exception as e:
    print(f"✗ Error loading model or scaler: {e}")
    model = None
    scaler = None

# Define feature names (must match training order)
FEATURE_NAMES = [
    'alcohol',
    'malic_acid',
    'ash',
    'alcalinity_of_ash',
    'magnesium',
    'flavanoids'
]


@app.route('/')
def home():
    """
    Render the home page with input form.
    """
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    """
    Handle prediction request from the form.
    Receives user input, preprocesses it, and returns prediction.
    """
    try:
        # Check if model and scaler are loaded
        if model is None or scaler is None:
            return render_template(
                'index.html',
                error="Model or scaler not loaded. Please check the model files."
            )
        
        # Extract feature values from form
        features = []
        for feature_name in FEATURE_NAMES:
            value = request.form.get(feature_name)
            if value is None or value == '':
                return render_template(
                    'index.html',
                    error=f"Missing value for {feature_name}. Please fill all fields."
                )
            try:
                features.append(float(value))
            except ValueError:
                return render_template(
                    'index.html',
                    error=f"Invalid value for {feature_name}. Please enter a valid number."
                )
        
        # Convert to numpy array and reshape for prediction
        input_data = np.array(features).reshape(1, -1)
        
        # Scale the input using the loaded scaler
        input_scaled = scaler.transform(input_data)
        
        # Make prediction
        prediction = model.predict(input_scaled)[0]
        
        # Get prediction probability for confidence
        prediction_proba = model.predict_proba(input_scaled)[0]
        confidence = max(prediction_proba) * 100
        
        # Map prediction to cultivar name
        cultivar_name = f"Cultivar {prediction}"
        
        # Render result
        return render_template(
            'index.html',
            prediction=cultivar_name,
            confidence=f"{confidence:.2f}",
            input_values={name: val for name, val in zip(FEATURE_NAMES, features)}
        )
    
    except Exception as e:
        # Handle any unexpected errors
        return render_template(
            'index.html',
            error=f"An error occurred during prediction: {str(e)}"
        )


if __name__ == '__main__':
    # Run the Flask app
    # Set debug=False for production deployment
    app.run(debug=True, host='0.0.0.0', port=5000)

