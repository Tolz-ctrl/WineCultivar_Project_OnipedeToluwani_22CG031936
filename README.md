# Wine Cultivar Origin Prediction System

A machine learning web application that predicts wine cultivar origin based on chemical properties using the UCI Wine dataset.

## 📋 Project Overview

This project implements a multiclass classification system to predict wine cultivar (class 0, 1, or 2) using 6 chemical features:
- Alcohol
- Malic Acid
- Ash
- Alcalinity of Ash
- Magnesium
- Flavanoids

## 🗂️ Project Structure

```
WineCultivar_Project/
│
├── app.py                                  # Flask web application
├── requirements.txt                        # Python dependencies
├── WineCultivar_hosted_webGUI_link.txt    # Deployment link placeholder
├── README.md                               # Project documentation
│
├── /model/
│   ├── model_building.ipynb               # Model training notebook
│   ├── wine_cultivar_model.pkl            # Trained model (generated)
│   └── scaler.pkl                         # Fitted scaler (generated)
│
├── /templates/
│   └── index.html                         # Web interface
│
└── /static/
    └── style.css                          # Optional CSS (styles in HTML)
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- Jupyter Notebook (for model training)

### Installation

1. **Clone or download this project**

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Train the model**
   
   Open and run the Jupyter notebook:
   ```bash
   jupyter notebook model/model_building.ipynb
   ```
   
   Execute all cells to:
   - Load and preprocess the Wine dataset
   - Train the Logistic Regression model
   - Generate `wine_cultivar_model.pkl` and `scaler.pkl` files

4. **Run the Flask application**
   ```bash
   python app.py
   ```

5. **Access the web interface**
   
   Open your browser and navigate to:
   ```
   http://localhost:5000
   ```

## 📊 Model Details

- **Algorithm**: Logistic Regression
- **Dataset**: UCI Wine Dataset (sklearn)
- **Features**: 6 chemical properties
- **Target**: Wine cultivar (0, 1, 2)
- **Train/Test Split**: 80/20
- **Preprocessing**: StandardScaler normalization
- **Evaluation Metrics**: Accuracy, Precision, Recall, F1-Score

## 🌐 Deployment

### Option 1: Render

1. Create account at [render.com](https://render.com)
2. Create new Web Service from GitHub repo
3. Add to requirements.txt: `gunicorn==21.2.0`
4. Build command: `pip install -r requirements.txt`
5. Start command: `gunicorn app:app`

### Option 2: Railway

1. Create account at [railway.app](https://railway.app)
2. Create new project from GitHub
3. Auto-detection handles deployment

### Option 3: Streamlit Cloud

Convert to Streamlit app or use Flask as-is with appropriate configuration.

## 📝 Usage

1. Enter the 6 wine chemical property values in the web form
2. Click "Predict Cultivar"
3. View the predicted cultivar and confidence score

### Example Input Values

**Cultivar 0 Example:**
- Alcohol: 14.23
- Malic Acid: 1.71
- Ash: 2.43
- Alcalinity of Ash: 15.6
- Magnesium: 127
- Flavanoids: 3.06

## 🧪 Testing

The model achieves high accuracy on the test set. Detailed performance metrics are available in the Jupyter notebook output.

## 📦 Dependencies

- Flask 2.3.0
- scikit-learn 1.3.0
- pandas 2.0.3
- numpy 1.24.3
- joblib 1.3.2
- Werkzeug 2.3.0

## 🎓 Academic Project

This project follows academic best practices:
- Clean, well-commented code
- Proper train/test split
- Feature scaling
- Comprehensive evaluation
- Professional documentation

## 📄 License

This is an academic project for educational purposes.

## 👤 Author

[Your Name]  
[Your Matric Number]  
[Your Institution]

## 🙏 Acknowledgments

- UCI Machine Learning Repository for the Wine dataset
- scikit-learn for machine learning tools
- Flask for web framework

