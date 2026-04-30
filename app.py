from flask import Flask, render_template, request
import pickle
import numpy as np
import os

app = Flask(__name__)

# Load model
model_path = "model/model.pkl"

if os.path.exists(model_path):
    model = pickle.load(open(model_path, "rb"))
    print("Model loaded successfully")
else:
    model = None
    print("model.pkl not found")

# Home route
@app.route("/")
def home():
    return render_template("index.html")

# Prediction route
@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return "Model not found. Put model.pkl inside model folder"

    try:
        features = [
            float(request.form["age"]),
            float(request.form["sex"]),
            float(request.form["cp"]),
            float(request.form["trestbps"]),
            float(request.form["chol"]),
            float(request.form["fbs"]),
            float(request.form["restecg"]),
            float(request.form["thalach"]),
            float(request.form["exang"]),
            float(request.form["oldpeak"]),
            float(request.form["slope"]),
            float(request.form["ca"]),
            float(request.form["thal"])
        ]

        final_input = np.array([features])
        prediction = model.predict(final_input)

        if prediction[0] == 1:
            result = "Heart Disease Detected"
        else:
            result = "No Heart Disease"

        return render_template("index.html", prediction_text=result)

    except Exception as e:
        return f"Error: {str(e)}"

# Run app
if __name__ == "__main__":
    app.run(debug=True)