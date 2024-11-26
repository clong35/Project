from app import app
from flask import jsonify, request, render_template
import csv

@app.route('/')
def view_form():
    return render_template('index.html', features=get_data())


@app.route('/pretrained_model/', methods=['GET', 'POST'])
def pretrained_model():
    return render_template('pretrained_model.html', data=get_data())


@app.route('/train_own_model/', methods=['GET', 'POST'])
def train_own_model():
    return render_template('train_own_model.html', features=get_data())


@app.route('/api/data', methods=['GET', 'POST'])
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
        feature_type = rows[2]

        for i in range(len(feature_names)):
            data.append({
                "featureName": feature_names[i],
                "featureDescription": feature_descriptions[i],
                "isFeatureSelected": True,
                "formattedFeatureName": feature_names[i].title().replace('_', ' '),
                "featureType": feature_type[i]
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


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        age = request.form.get('age')
        anaemia = True if request.form.get('anaemia') else False
        creatinine_phosphokinase = request.form.get('creatinine_phosphokinase')
        diabetes = True if request.form.get('diabetes') else False
        ejection_fraction = request.form.get('ejection_fraction')
        high_blood_pressure = True if request.form.get('high_blood_pressure') else False
        platelets = request.form.get('platelets')
        serum_creatinine = request.form.get('serum_creatinine')
        serum_sodium = request.form.get('serum_sodium')
        sex = 0 if request.form.get('sex') == "female" else 1
        smoking = True if request.form.get('smoking') else False
        time = request.form.get('time')
        
    import pickle
    import pandas as pd
    from numpy import reshape
    loaded_model = None
    death_event = None
    data = [age,anaemia,creatinine_phosphokinase,diabetes,ejection_fraction,high_blood_pressure,platelets,serum_creatinine,serum_sodium,sex,smoking,time]
    labels = ["age","anaemia","creatinine_phosphokinase","diabetes","ejection_fraction","high_blood_pressure","platelets","serum_creatinine","serum_sodium","sex","smoking","time"]
    res = dict(map(lambda i,j : (i,j) , labels,data))
    df = pd.DataFrame(res, index=[0])
    print(df.head)
    # print(request.form)
    # return request.form
    reshape(data, shape=(1, -1))
    with open('saved_model.pkl', 'rb') as file:
        loaded_model = pickle.load(file)

    if loaded_model:
        death_event = loaded_model.predict(df)
        print(death_event[0])
        return f"<p>{death_event[0]}</p>"