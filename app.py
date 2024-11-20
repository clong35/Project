from flask import Flask, jsonify, request, render_template
from flask_cors import CORS
import csv

# import numpy as np
# import pandas as pd
# from sklearn.linear_model import LinearRegression
# from sklearn import Des

app = Flask(__name__)
CORS(app)
app.config['TEMPLATES_AUTO_RELOAD'] = True
selected_features = []
selected_model = ""

@app.route('/')
def view_form():
    return render_template('login.html', features=get_data())


@app.route('/api/data', methods=['GET'])
def get_data():
    data = []
    rows = []
    with open("list.csv") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            rows.append(row)
        # print(rows)

        feature_names = rows[0]
        feature_descriptions = rows[1]

        for i in range(len(feature_names)):
            data.append({
                "featureName": feature_names[i],
                "featureDescription": feature_descriptions[i],
                "isFeatureSelected": True,
                "formattedFeatureName": feature_names[i].title().replace('_', ' '),
            })
    return data
    return jsonify(data)

    # with open("heart_failure_clinical_records_dataset.csv") as f:
    #     list_of_column_names = []
    #     csv_reader = csv.reader(f, delimiter = ',')

    #     for row in csv_reader:
    #         list_of_column_names.append(row)
    # data = {'message': list_of_column_names[0]}
    # return jsonify(data)


@app.route('/api/set_data', methods=['GET', 'POST'])
def set_data():

    if request.method == 'POST':

        print(request.form)
        # selected_features = request.form.get('selected_features')
        # selected_model = request.form['selected_model']
        # print(selected_features, selected_model)
        return "<h1>Welcome!!!</h1>"
    return "<h1>Hello!!!</h1>"
    
    # return render_template('login.html')#"<h1>Welcome!!!</h1>"


def train_model(features, model):
    pass


if __name__ == '__main__':
    app.run(debug=True)