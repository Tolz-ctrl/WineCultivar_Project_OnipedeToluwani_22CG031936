"""
Wine Cultivar Origin Prediction System
Model Training Script

This script trains the machine learning model and saves it for deployment.
Alternative to running the Jupyter notebook.
"""

import pandas as pd
import numpy as np
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score
import joblib
import os


def main():
    print("=" * 70)
    print("Wine Cultivar Origin Prediction System - Model Training")
    print("=" * 70)
    
    # Step 1: Load the Wine dataset
    print("\n[1/11] Loading Wine dataset...")
    wine_data = load_wine()
    print(f"✓ Dataset loaded: {wine_data.data.shape[0]} samples, {wine_data.data.shape[1]} features")
    
    # Step 2: Convert to Pandas DataFrame
    print("\n[2/11] Converting to DataFrame...")
    df = pd.DataFrame(data=wine_data.data, columns=wine_data.feature_names)
    df['cultivar'] = wine_data.target
    print(f"✓ DataFrame created: {df.shape}")
    
    # Step 3: Check for missing values
    print("\n[3/11] Checking for missing values...")
    missing_count = df.isnull().sum().sum()
    print(f"✓ Missing values found: {missing_count}")
    
    # Step 4: Select the six specified features
    print("\n[4/11] Selecting features...")
    selected_features = [
        'alcohol',
        'malic_acid',
        'ash',
        'alcalinity_of_ash',
        'magnesium',
        'flavanoids'
    ]
    
    X = df[selected_features]
    y = df['cultivar']
    print(f"✓ Selected {len(selected_features)} features")
    print(f"  Features: {', '.join(selected_features)}")
    
    # Step 5: Split dataset (80/20)
    print("\n[5/11] Splitting dataset (80% train, 20% test)...")
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    print(f"✓ Training set: {X_train.shape[0]} samples")
    print(f"✓ Test set: {X_test.shape[0]} samples")
    
    # Step 6: Apply feature scaling
    print("\n[6/11] Applying StandardScaler...")
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    print("✓ Feature scaling completed")
    
    # Step 7: Train Logistic Regression model
    print("\n[7/11] Training Logistic Regression model...")
    model = LogisticRegression(max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)
    print("✓ Model training completed")
    
    # Step 8: Make predictions
    print("\n[8/11] Making predictions...")
    y_train_pred = model.predict(X_train_scaled)
    y_test_pred = model.predict(X_test_scaled)
    print("✓ Predictions completed")
    
    # Step 9: Evaluate model
    print("\n[9/11] Evaluating model performance...")
    train_accuracy = accuracy_score(y_train, y_train_pred)
    test_accuracy = accuracy_score(y_test, y_test_pred)
    precision = precision_score(y_test, y_test_pred, average='macro')
    recall = recall_score(y_test, y_test_pred, average='macro')
    f1 = f1_score(y_test, y_test_pred, average='macro')
    
    print("\n" + "=" * 70)
    print("MODEL PERFORMANCE EVALUATION")
    print("=" * 70)
    print(f"Training Accuracy:   {train_accuracy:.4f} ({train_accuracy*100:.2f}%)")
    print(f"Test Accuracy:       {test_accuracy:.4f} ({test_accuracy*100:.2f}%)")
    print(f"Precision (macro):   {precision:.4f}")
    print(f"Recall (macro):      {recall:.4f}")
    print(f"F1-Score (macro):    {f1:.4f}")
    
    print("\n" + "=" * 70)
    print("DETAILED CLASSIFICATION REPORT")
    print("=" * 70)
    target_names = ['Cultivar 0', 'Cultivar 1', 'Cultivar 2']
    print(classification_report(y_test, y_test_pred, target_names=target_names))
    
    # Step 10: Save model and scaler
    print("\n[10/11] Saving model and scaler...")
    model_filename = 'wine_cultivar_model.pkl'
    scaler_filename = 'scaler.pkl'
    
    joblib.dump(model, model_filename)
    joblib.dump(scaler, scaler_filename)
    
    print(f"✓ Model saved: {model_filename} ({os.path.getsize(model_filename)} bytes)")
    print(f"✓ Scaler saved: {scaler_filename} ({os.path.getsize(scaler_filename)} bytes)")
    
    # Step 11: Verify loading
    print("\n[11/11] Verifying model loading...")
    loaded_model = joblib.load(model_filename)
    loaded_scaler = joblib.load(scaler_filename)
    
    # Test prediction
    sample_data = X_test.iloc[0:1]
    sample_scaled = loaded_scaler.transform(sample_data)
    sample_prediction = loaded_model.predict(sample_scaled)
    
    print("✓ Model and scaler loaded successfully")
    print(f"✓ Test prediction: Cultivar {sample_prediction[0]} (Actual: {y_test.iloc[0]})")
    
    print("\n" + "=" * 70)
    print("✓ MODEL TRAINING COMPLETED SUCCESSFULLY!")
    print("=" * 70)
    print("\nYou can now run the Flask app with: python app.py")
    print("(Make sure to run this script from the 'model' directory)")


if __name__ == "__main__":
    main()

