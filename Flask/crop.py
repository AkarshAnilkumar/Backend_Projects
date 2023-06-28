from flask import Flask, request, jsonify
import joblib
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings("ignore")

classifier = joblib.load("E:\Pheonix\programing\Visual_studio_codes\Pythonpg\Miniproject_service\disease_prediction\classifier.pkl")
app = Flask(__name__)

@app.route('/predict', methods=['POST', 'OPTIONS'])
def predict():
    data = request.get_json()
    # data = {
    #     'N':105,
    #     'P':14,
    #     'K':50,
    #     'temperature':26.14,
    #     'humidity':87.68,
    #     'ph':6.41,
    #     'rainfall':59.65
    #     }
    user_data = pd.DataFrame(data, index=[0])
    column = ['N','P','K','temperature','humidity','ph','rainfall'] 
    user_data = user_data[column]
    return jsonify({'result': classifier.predict(user_data)[0]}), 201

if __name__ == '__main__':
    app.run()

# it returns 
# {
#     "result": "watermelon"
# }


