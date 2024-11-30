# import OS module
import os
# Get the list of all files and directories
path = "models"
dir_list = os.listdir(path)
print("Files and directories in '", path, "' :")
# prints all files
print(dir_list)


# import pandas as pd
# import numpy as np

# df = pd.read_csv('student_lifestyle_dataset.csv')

# from sklearn.model_selection import train_test_split

# X = df.loc[:,['Stress_Level', "GPA"]]
# print(X.head)
# y = df['Stress_Level'].copy()

# X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

# from sklearn.tree import DecisionTreeClassifier
# from sklearn.metrics import f1_score

# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)
# y_pred = model.predict(X_test)
# print(y_pred)

# import pickle

# with open('test_save.pkl', 'wb') as file:
#     data = (model, "Hello World")
#     data = {
#         "model": model,
#         "model_type": "Decision Tree Classifier",
#         "selected_features": []
#     }
#     pickle.dump(data, file)


# with open('test_save.pkl', 'rb') as file:
#     loaded_model = pickle.load(file)
#     print(loaded_model[1])


