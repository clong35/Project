# s = 'hello_world'

# print(s.title().replace('_', ' '))


# labels = ["age","anaemia","creatinine_phosphokinase","diabetes","ejection_fraction","high_blood_pressure","platelets","serum_creatinine","serum_sodium","sex","smoking","time"]
# data = [i for i in range(1, 13)]
    
# print(data)
# res = dict(map(lambda i,j : (i,j) , labels,data))
# print(res)
# print(len(data))
# print(len(labels))


import pandas as pd
import numpy as np

df = pd.read_csv('student_lifestyle_dataset.csv')

from sklearn.model_selection import train_test_split

X = df.copy().drop(['Stress_Level', 'Student_ID'], axis='columns')
y = df['Stress_Level'].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score

model = DecisionTreeClassifier()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print(y_pred)
# print(f"f1 score {f1_score(y_test, y_pred)}")

# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# import matplotlib.pyplot as plt

# cm = confusion_matrix(y_test, y_pred)
# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['True', 'False'])

# disp.plot(cmap='Blues')
# plt.title('Confusion Matrix')
# plt.show()


