# UFO Sightings Predictor

**Author:** devcherop  
  

---

## Project Overview
The **UFO Sightings Predictor** is a Flask web application that predicts UFO sightings based on input features using a pre-trained machine learning model (`ufod-model.pkl`). The project is Dockerized and includes a **GitHub Actions workflow** for CI/CD.

---

## Features
- Predict UFO sightings based on input features.
- Web interface built with Flask and templates.
- Styled using CSS in `static/css`.
- Pre-trained model stored as `ufod-model.pkl`.
- Docker support for containerized deployment.
- Continuous Integration with GitHub Actions (`.github/workflows/CI.yml`).

---

## Installation

### Local Setup

1. **Clone the repository:**

git clone https://github.com/dev-cherop/UFO-Predictor.git

cd UFO-Predictor
Create a virtual environment and activate it:


python -m venv venv

source venv/bin/activate   # Linux/Mac

venv\Scripts\activate      # Windows

Install dependencies:


pip install -r requirements.txt
Run the Flask app:


python run.py
Access the app:
Open http://127.0.0.1:5000 in your browser.

Docker Setup

Build the Docker image:


docker build -t ufo-predictor .

Run the container:


docker run -p 5000:5000 ufo-predictor

Open http://127.0.0.1:5000 in your browser.

Usage

1.Navigate to the web interface.

2.Provide the necessary input features.

3.Click “Predict” to get UFO sighting predictions.

Notes
Ensure ufod-model.pkl is in the project root.

CI/CD workflow runs automatically on GitHub Actions (.github/workflows/CI.yml).

