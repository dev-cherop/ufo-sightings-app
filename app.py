import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Load pre-trained model
with open("ufod-model.pkl", "rb") as f:
    model = pickle.load(f)

COUNTRIES = ["Australia", "Canada", "Germany", "UK", "US"]

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Convert form values to float features
        float_features = [float(x) for x in request.form.values()]
        final_features = np.array([float_features])  # shape (1, n)

        # Model prediction
        prediction = model.predict(final_features)[0]
        
        # Map output index to country
        country = COUNTRIES[prediction]

        return render_template("index.html", prediction_text=f"🌍 Likely country: {country}")

    except ValueError:
        return render_template("index.html", prediction_text="⚠️ Invalid input: please enter valid numbers.")
    except Exception as e:
        return render_template("index.html", prediction_text=f"🚨 Error: {str(e)}")

if __name__ == "__main__":
    app.run(debug=True)
