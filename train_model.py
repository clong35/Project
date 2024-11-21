import numpy as np
import pandas as pd 



from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


df = pd.read_csv('heart_failure_clinical_records_dataset.csv')

X = df.copy()
y = df['DEATH_EVENT'].copy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

model = LinearRegression()

model.fit(X_train, y_train)
