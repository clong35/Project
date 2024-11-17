from flask import Flask, jsonify
from flask_cors import CORS
import csv

app = Flask(__name__)

CORS(app)
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

    return jsonify(data)

    # with open("heart_failure_clinical_records_dataset.csv") as f:
    #     list_of_column_names = []
    #     csv_reader = csv.reader(f, delimiter = ',')

    #     for row in csv_reader:
    #         list_of_column_names.append(row)
    # data = {'message': list_of_column_names[0]}
    # return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)