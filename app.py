from flask import Flask
from flask_cors import CORS
import csv

# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn import Des

app = Flask(__name__)
CORS(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True
# selected_features = []
# selected_model = ""


def train_model(features, model):
    pass


if __name__ == '__main__':
    app.run(debug=True)