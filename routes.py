from app import app
from flask import jsonify, request, render_template, redirect
import csv
from train_model import train_model


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


@app.route('/')
def view_form():
    return render_template('index.html', features=get_data())


@app.route('/train_new_model', methods=['GET', 'POST'])
def train_new_model():
    return render_template('train_new_model.html', features=get_data())


@app.route('/process_model', methods=['GET', 'POST'])
def process_model():
    if request.method == 'POST':
        selected_features = request.form.getlist('selected_features')
        selected_model = request.form.getlist('selected_model')
        
        print(selected_features)
        print(selected_model)

        train_model(selected_model, selected_features, "new_model_1")

        # print(request.form)
    return redirect("/")
    return render_template('process_model.html')





@app.route('/pretrained_model/', methods=['GET', 'POST'])
def pretrained_model():
    return render_template('pretrained_model.html', data=get_data())


@app.route('/train_own_model/', methods=['GET', 'POST'])
def train_own_model():
    return render_template('train_own_model.html', features=get_data())



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

@app.route('/predict/trained_own_model', methods=['GET', 'POST'])
def trained_own_model():
    if request.method == 'POST':
        study_hours_per_day = request.form.get('Study_Hours_Per_Day')
        extracurricular_hours_per_day = request.form.get('Extracurricular_Hours_Per_Day')
        sleep_hours_per_day = request.form.get('Sleep_Hours_Per_Day')
        social_hours_per_day = request.form.get('Social_Hours_Per_Day')
        physical_activity_hours_per_day = request.form.get('Physical_Activity_Hours_Per_Day')
        gpa = request.form.get('GPA')

        
        import pickle
        import pandas as pd
        from numpy import reshape
        loaded_model = None
        stress_level = None
        data = [study_hours_per_day,extracurricular_hours_per_day,sleep_hours_per_day,social_hours_per_day,physical_activity_hours_per_day,gpa]
        print(data)
        labels = ['Study_Hours_Per_Day','Extracurricular_Hours_Per_Day','Sleep_Hours_Per_Day','Social_Hours_Per_Day','Physical_Activity_Hours_Per_Day','GPA']
        res = dict(map(lambda i,j : (i,j) , labels,data))
        df = pd.DataFrame(res, index=[0])
        # print(df.head)
        # print(request.form)
        # return request.form
        reshape(data, shape=(1, -1))
        with open('saved_model.pkl', 'rb') as file:
            loaded_model = pickle.load(file)

        if loaded_model:
            stress_level = loaded_model.predict(df)
            print(stress_level[0])
            return f"<p>{stress_level[0]}</p>"



@app.route('/predict/pretrained', methods=['GET', 'POST'])
def predict_pretrained():
    if request.method == 'POST':
        import pickle
        import pandas as pd

        with open('saved_model.pkl', 'rb') as file:
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