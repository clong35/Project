import numpy as np
import pandas as pd 


# from sklearn.neighbors import KNeighborsClassifier
# from sklearn.linear_model import LogisticRegression
# from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
# model = LinearDiscriminantAnalysis()
# # model = LogisticRegression()
# # model = KNeighborsClassifier()
# # descision tree classifier instead

# # loaded_model = None
# # with open('saved_model.pkl', 'rb') as file:
# #     loaded_model = pickle.load(file)

# # if loaded_model:
# #     y_pred = model.predict(X_test)
# #     print(y_pred)

# from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
# import matplotlib.pyplot as plt


# cm = confusion_matrix(y_test, y_pred)
# disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["True", "False"])

# # Plot the confusion matrix
# disp.plot(cmap='Blues')
# plt.title('Confusion Matrix')
# plt.savefig("static/styles/pretrained_confusion_matrix.png")
# plt.show()


def train_model(model_type, selected_features, name):
    from sklearn.model_selection import train_test_split

    df = pd.read_csv('student_lifestyle_dataset.csv')


    X = df.copy().loc[:,selected_features]
    y = df['Stress_Level'].copy()

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=1)

    match model_type:
        case "Decision Tree Classifier":
            from sklearn.tree import DecisionTreeClassifier
            model = DecisionTreeClassifier()
        case "Linear Discriminant Analysis":
            from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
            model = LinearDiscriminantAnalysis()
        case "Logistic Regression":
            from sklearn.linear_model import LogisticRegression
            model = LogisticRegression()

        case _:
            model_type = "Decision Tree Classifier"
            from sklearn.tree import DecisionTreeClassifier
            model = DecisionTreeClassifier()

    model.fit(X_train, y_train)

    # Save a confusion matrix of the performance
    import matplotlib.pyplot as plt
    from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

    y_pred = model.predict(X_test)

    # Generate the confusion matrix
    cm = confusion_matrix(y_test, y_pred)

    # Display the confusion matrix
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=['Low', 'Moderate', 'High'])
    disp.plot(cmap=plt.cm.Blues)
    plt.title('Confusion Matrix')
    plt.savefig(f"static/{name.split('.')[0]}")
    # plt.show()
    save_model(model, model_type, selected_features, name)



def save_model(model, model_type, selected_features, filename):
    data = {
        "model": model,
        "model_type": model_type,
        "selected_features": selected_features
    }

    import pickle
    
    with open(f"models/{filename}", 'wb') as file:
        pickle.dump(data, file)


if __name__ == "__main__":
    train_model("Decision Tree Classifier", [
        "Study_Hours_Per_Day",
        "Extracurricular_Hours_Per_Day",
        "Sleep_Hours_Per_Day",
        "Social_Hours_Per_Day",
        "Physical_Activity_Hours_Per_Day",
        "GPA"
    ], "saved_model.pkl")