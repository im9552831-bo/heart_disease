
# ❤️ Heart Disease Prediction Web Application

## 📌 Overview
This project is a web-based Machine Learning application that predicts the likelihood of heart disease based on user-provided medical parameters.  
The system integrates a trained classification model with a Flask backend and a responsive web interface.

---

## 🎯 Objectives
- Develop a predictive model for heart disease detection  
- Build an interactive web interface for user input  
- Integrate Machine Learning with a web application  
- Provide real-time prediction results  

---

## 🚀 Features
- Simple and intuitive user interface  
- Real-time prediction using trained model  
- Lightweight and fast execution  
- Clean and responsive UI design  

---

## 🛠️ Tech Stack
**Frontend:**
- HTML5
- CSS3

**Backend:**
- Python
- Flask

**Machine Learning:**
- Scikit-learn
- NumPy
- Pandas

---

## 📂 Project Structure
aml/
│
├── app.py # Flask application
├── requirements.txt # Dependencies
├── model/
│ └── model.pkl # Trained ML model
├── templates/
│ └── index.html # User interface
└── README.md # Project documentation


---

## ⚙️ Installation & Setup

### 1. Clone or Download Project
```bash
git clone <repository-url>
cd aml
pip install -r requirements.txt
python app.py


---
LOCAL HOST
http://127.0.0.1:5000




📊 Input Parameters

The model takes the following features:

Age
Sex
Chest Pain Type (cp)
Resting Blood Pressure (trestbps)
Cholesterol (chol)
Fasting Blood Sugar (fbs)
Resting ECG (restecg)
Maximum Heart Rate (thalach)
Exercise Induced Angina (exang)
ST Depression (oldpeak)
Slope
Number of Major Vessels (ca)
Thalassemia (thal)



🧠 Model Information
Algorithm: Random Forest Classifier
Dataset: Heart Disease Dataset
Evaluation Metrics:
Accuracy
Confusion Matrix
Classification Report


📈 Output
No Heart Disease
Heart Disease Detected



## 📂 Project Structure
