# import random
import pandas as pd
# import numpy as np


# model = DecisionTreeClassifier()
# model.fit(X_train, y_train)

# y_pred = pd.Series(np.array(model.predict(X_test)))




import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Load the Iris dataset
df = pd.read_csv('student_lifestyle_dataset.csv')

from sklearn.model_selection import train_test_split

X = df.loc[:,['Study_Hours_Per_Day', "GPA"]]
# print(X.head)
y = df['Stress_Level'].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=1)


clf = DecisionTreeClassifier()
clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = clf.predict(X_test)

# Generate the confusion matrix
cm = confusion_matrix(y_test, y_pred)

# Display the confusion matrix
disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Low', 'Moderate', 'High'])
disp.plot(cmap=plt.cm.Blues)
plt.title('Confusion Matrix')
plt.show()

# Print the confusion matrix
print("Confusion Matrix:")
print(cm)











