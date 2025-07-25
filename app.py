import numpy as np
from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

model = pickle.load(open("ufod-model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        float_features = [float(x) for x in request.form.values()]
        final_features = [np.array(float_features)]
        prediction = model.predict(final_features)
        output = prediction[0]

        countries = ["Australia", "Canada", "Germany", "UK", "US"]
        return render_template(
            "index.html", prediction_text="Likely country: {}".format(countries[output])
        )
    except ValueError:
        return render_template("index.html", prediction_text="Invalid input: please enter valid numbers.")

if __name__ == "__main__":
    app.run(debug=True)
