# NASA-Asteroid-Classifier

This is a machine learning project that predicts whether a near-Earth asteroid is potentially hazardous using real data from NASA's NeoWs API.

## About
It fetches real asteroid data from NASA's Near Earth Object Web Service (NeoWs) API and trains a Random Forest classifier to predict whether an asteroid is potentially hazardous to Earth.

## Dataset
- Source: NASA NeoWs API
- Size: 1759 asteroids (1 year of data)
- Features: absolute magnitude, velocity, diameter (min/max), miss distance
- Target: is_potentially_hazardous_asteroid
