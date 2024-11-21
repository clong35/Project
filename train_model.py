import numpy as np
import pandas as pd 



from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import f1_score


df = pd.read_csv('heart_failure_clinical_records_dataset.csv')

X = df.copy().drop('DEATH_EVENT', axis='columns')
y = df['DEATH_EVENT'].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

# model = DecisionTreeClassifier()

from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
model = LinearDiscriminantAnalysis()
# model = LogisticRegression()
# model = KNeighborsClassifier()
# descision tree classifier instead
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
print(y_pred)
# print(y_test)
print(f"f1 score {f1_score(y_test, y_pred)}")

import pickle
s = pickle.dumps(model)

with open('saved_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# loaded_model = None
# with open('saved_model.pkl', 'rb') as file:
#     loaded_model = pickle.load(file)

# if loaded_model:
#     y_pred = model.predict(X_test)
#     print(y_pred)

from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt


cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["True", "False"])

# Plot the confusion matrix
disp.plot(cmap='Blues')
plt.title('Confusion Matrix')
plt.savefig("static/styles/pretrained_confusion_matrix.png")
plt.show()