# Import libraries
from flask import Flask, jsonify, request
import pandas as pd
import joblib

# Initialize API
app = Flask(__name__)


# Define API service
@app.route("/") # API service path
def hello(): # API service functionality
    return "Máster en Data Analytics "

# Run API
if __name__ == '__main__':
    app.run(host = '0.0.0.0', debug=True)
