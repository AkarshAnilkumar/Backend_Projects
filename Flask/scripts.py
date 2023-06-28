 from flask import Flask, request, jsonify
import numpy as np
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder
# from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

target = joblib.load("./targetpkl.pkl")
LE = LabelEncoder()
target = LE.fit_transform(target)
model_used = joblib.load('./decisiontreenew.pkl')


@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    data = request.get_json()
    # data = {
    # "features": [[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1],[1]]
    # }
    features = np.array(data['features'])
    # print(model_used.feature_names_in_)
    user_data = pd.DataFrame(features, columns=(model_used.feature_names_in_).reshape(
        1, 22))  # feature_names_in_ is a method to list all the features of a decision tree
    new_user_data = dict()
    for i in range(len(user_data)):
        value = features[1][0]
        column = user_data.columns
        new_user_data[column[0][i]] = [value]
    user_class = pd.DataFrame.from_dict(new_user_data)

    # prediction = np.array(model_used.predict(user_class))#[0]
    prediction = model_used.predict(user_class)
    # decode the prediction to a category
    predicted_class = LE.inverse_transform(prediction)[0]
    response = {'prediction': predicted_class}
    return jsonify(response)


if __name__ == '__main__':
    app.run(debug=True)
