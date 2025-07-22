# UFO Sightings Visualization App 
A Flask web app that analyzes and visualizes UFO sightings from a public dataset.

## Tech Stack
- Python, Flask
- Pandas / Matplotlib / Plotly (if used)
- Docker
- GitHub Actions for CI

##  Features
- Interactive web dashboard for sightings
- Location/time-based filtering
- CI pipeline with GitHub Actions
- Dockerized app for easy deployment

##  Setup
```bash
docker build -t ufo-app .
docker run -p 5000:5000 ufo-app
