# Machine Learning Project

[Dataset](https://www.kaggle.com/datasets/steve1215rogg/student-lifestyle-dataset?select=student_lifestyle_dataset.csv)

## Setup

Install the dependencies from the requirements.txt file
`pip install -r requirements.txt`

Set the environment variable for flask and then run the app
`$env:FLASK_APP='app'`
`flask run`

By running the train_model.py file this will create a model trained on all of the input data. This can be used when running the app.

## Using the app
When the app is run you can test the pretrained model on the dataset or choose to train your own. There are a few different basic models to choose from and you can select which features to train the model on.