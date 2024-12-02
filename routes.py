from app import app
from flask import jsonify, request, render_template, redirect
import csv
from train_model import train_model


# Gets the features from the data file
def get_data():
    data = []
    rows = []
    with open("student_lifestyle_dataset.csv") as f:
        csv_reader = csv.reader(f)
        for row in csv_reader:
            rows.append(row)
        # print(rows)

        feature_names = rows[0]
        feature_names.pop(0)
        feature_names.pop(-1)

        for i in range(len(feature_names)):
            data.append({
                "featureName": feature_names[i],
                "formattedFeatureName": feature_names[i].title().replace('_', ' ')
            })
    return data


# Gets all of the saved models from the models folder.
def get_models():
    import os
    path = "models"
    model_list = os.listdir(path)
    print(model_list)
    return model_list


# Displays the index.hmtl page passing in the models saved to disk.
@app.route('/')
def view_form():
    return render_template('index.html', models=get_models())


# Trains a model with the selected model and features
@app.route('/train_new_model', methods=['GET', 'POST'])
def train_new_model():
    return render_template('train_new_model.html', features=get_data())


# A temporary redirect while the model trains in the background
@app.route('/process_model', methods=['GET', 'POST'])
def process_model():
    if request.method == 'POST':
        model_name = request.form.get('model_name')
        selected_features = request.form.getlist('selected_features')
        selected_model = request.form.getlist('selected_model')
        
        print(selected_features)
        print(selected_model)

        train_model(selected_model, selected_features, f"{model_name}.pkl")

        # print(request.form)
    return redirect("/")
    return render_template('process_model.html')


# Takes the user input for the selected model.
@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        selected_model = request.form.get('model')
        selected_features = None
        import pickle
        if selected_model:

            with open(f"models/{selected_model}", 'rb') as file:
                data = pickle.load(file)
                model = data["model"]
                model_type = data["model_type"]
                selected_features = data["selected_features"]
                print(1)
                return render_template('predict.html', features=selected_features, model=selected_model, model_type=model_type)

        else:
            import pandas as pd
            
            a = {}
            for feature in selected_features:
                a[feature] = request.form.get(feature)
            
                
            print(2)
            return render_template('predict.html', model=selected_model)
    return "Hello World"


# Using the inputed data returns the models prediction.
@app.route('/get_prediction', methods=['POST'])
def get_prediction():
    print(request.form)
    model_name = request.form.get('model')
    print(model_name)

    # return f"<p>{model_name}</p>"
    import pickle
    import pandas as pd

    with open(f"models/{model_name}", 'rb') as file:
        data = pickle.load(file)
        model = data["model"]
        selected_features = data["selected_features"]

        a = {}
        for feature in selected_features:
            a[feature] = request.form.get(feature)
        
        df = pd.DataFrame(a, index=[0])

        if model:
            stress_level = model.predict(df)
            print(stress_level[0])
            return f"<p>{stress_level[0]}</p>"

