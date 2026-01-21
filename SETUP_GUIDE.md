# Wine Cultivar Prediction System - Setup Guide

## Quick Start Guide

Follow these steps to set up and run the Wine Cultivar Prediction System.

### Step 1: Install Python Dependencies

Open a terminal/command prompt in the project directory and run:

```bash
pip install -r requirements.txt
```

This will install:
- Flask (web framework)
- scikit-learn (machine learning)
- pandas (data manipulation)
- numpy (numerical computing)
- joblib (model serialization)

### Step 2: Train the Model

You have two options:

#### Option A: Using Python Script (Recommended)

```bash
cd model
python train_model.py
cd ..
```

This will:
- Load the Wine dataset
- Train the Logistic Regression model
- Generate `wine_cultivar_model.pkl` and `scaler.pkl`
- Display performance metrics

#### Option B: Using Jupyter Notebook

```bash
jupyter notebook model/model_building.ipynb
```

Then execute all cells in the notebook.

### Step 3: Verify Model Files

Check that these files were created in the `model/` directory:
- `wine_cultivar_model.pkl`
- `scaler.pkl`

### Step 4: Run the Flask Application

```bash
python app.py
```

You should see output like:
```
✓ Model and scaler loaded successfully!
 * Running on http://0.0.0.0:5000
```

### Step 5: Access the Web Interface

Open your web browser and navigate to:
```
http://localhost:5000
```

### Step 6: Test the Application

Enter sample wine chemical values:

**Example 1 (Cultivar 0):**
- Alcohol: 14.23
- Malic Acid: 1.71
- Ash: 2.43
- Alcalinity of Ash: 15.6
- Magnesium: 127
- Flavanoids: 3.06

**Example 2 (Cultivar 1):**
- Alcohol: 12.37
- Malic Acid: 1.63
- Ash: 2.3
- Alcalinity of Ash: 24.5
- Magnesium: 88
- Flavanoids: 2.22

**Example 3 (Cultivar 2):**
- Alcohol: 13.2
- Malic Acid: 1.78
- Ash: 2.14
- Alcalinity of Ash: 11.2
- Magnesium: 100
- Flavanoids: 2.65

Click "Predict Cultivar" to see the results!

## Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution:** Install dependencies with `pip install -r requirements.txt`

### Issue: "Model or scaler not loaded"
**Solution:** Run the training script first: `python model/train_model.py`

### Issue: "Port 5000 already in use"
**Solution:** Change the port in `app.py` (last line) to another port like 5001

### Issue: Jupyter notebook won't open
**Solution:** Install Jupyter: `pip install jupyter notebook`

## Project Structure Verification

Your project should look like this:

```
WineCultivar_Project/
│
├── app.py                                  ✓ Flask application
├── requirements.txt                        ✓ Dependencies
├── README.md                               ✓ Documentation
├── SETUP_GUIDE.md                          ✓ This file
├── WineCultivar_hosted_webGUI_link.txt    ✓ Deployment info
│
├── /model/
│   ├── model_building.ipynb               ✓ Training notebook
│   ├── train_model.py                     ✓ Training script
│   ├── wine_cultivar_model.pkl            ⚠ Generated after training
│   └── scaler.pkl                         ⚠ Generated after training
│
├── /templates/
│   └── index.html                         ✓ Web interface
│
└── /static/
    └── style.css                          ✓ Optional styles
```

## Next Steps

1. ✅ Install dependencies
2. ✅ Train the model
3. ✅ Run the Flask app
4. ✅ Test predictions
5. 🚀 Deploy to cloud (optional)

## Deployment

See `WineCultivar_hosted_webGUI_link.txt` for deployment instructions to:
- Render
- Railway
- Streamlit Cloud

## Support

For issues or questions, refer to:
- README.md for project overview
- Model training output for performance metrics
- Flask console output for debugging

---

**Happy Predicting! 🍷**

