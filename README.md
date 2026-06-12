# Fraud Detection Assistant (XGBoost + Streamlit + LLM)

## 🚀 Overview
This project is an AI-powered Fraud Detection System that predicts whether a financial transaction is fraudulent or legitimate using Machine Learning (XGBoost). It also includes an LLM-based explanation module to analyze suspicious transactions and provide insights.

---

## ✨ Features
- Fraud detection using **XGBoost classifier**
- Feature engineering for transaction analysis
- Real-time fraud prediction
- Risk scoring system
- LLM-based fraud explanation (investigation assistant)
- Streamlit web interface
- Model evaluation using Accuracy, Precision, Recall, F1-score

---

## 🏗️ Project Structure

fraud_detection_assistant/
│
├── app.py # Streamlit frontend
├── train_xgboost.py # Model training script
├── requirements.txt
├── .gitignore
│
├── core/
│ ├── preprocessing.py
│ ├── feature_engineering.py
│ ├── model.py
│ ├── predictor.py
│
├── utils/
│ ├── helpers.py
│ ├── logger.py
│
└── README.md


---

## ⚙️ Installation

### 1. Clone repository
```bash
git clone https://github.com/your-username/fraud_detection_assistant.git
cd fraud_detection_assistant

2. Create virtual environment
python -m venv venv
venv\Scripts\activate   # Windows
3. Install dependencies
pip install -r requirements.txt
▶️ Run the Application
streamlit run app.py

Then open:

http://localhost:8501

🧠 Model Information
Algorithm Used
XGBoost Classifier
Why XGBoost?
High performance on structured/tabular data
Handles imbalanced datasets effectively
Fast and scalable
📊 Evaluation Metrics

The model is evaluated using:

Accuracy
Precision
Recall
F1 Score
Confusion Matrix

🔄 Workflow
Input transaction data
Preprocessing and feature engineering
Fraud prediction using trained model
Risk score generation
LLM explains suspicious patterns

🛠️ Tech Stack
Python
Pandas, NumPy
Scikit-learn
XGBoost
Streamlit
Google Generative AI (LLM module)

📦 Requirements
streamlit
scikit-learn
numpy
pandas
xgboost
joblib
google-generativeai

🚀 Future Improvements
Add real-time transaction API
Add SHAP explainability plots
Improve UI dashboard analytics

👩‍💻 Author

G. Chandini
GitHub: https://github.com/ChandiniGogulamanda