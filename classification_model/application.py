import pandas as pd
import sys
import os
sys.path.append(".")
import numpy as np
from flask import Flask, request, render_template
from pydantic import validate_arguments
from sklearn.model_selection import train_test_split
from processing.data_manager import data_inputting, DATA_STORE
from processing.validation import validate_inputs
from predict import make_prediction
from config.core import config

# Initiating Flask
application = Flask(__name__,
                    template_folder='templates',
                    static_folder='templates/static')


# Rendering Website
@application.route("/")
@application.route("/home")
def home():
    return render_template("index.html")


@application.route('/predict', methods=["POST"])
def predict():
    """ Rendering Result on the HTML"""
    features_ = {
        'Pclass': None,
        'Sex': None,
        'Age': None,
        'SibSp': None,
        'Parch': None,
        'Fare': None,
        'Embarked': None
    }
    if request.method == "POST":
        for key_ in features_.keys():
            if key_ not in ['Fare']:
                if key_ == "Pclass":
                    if request.form[key_] == '1':
                        features_["Fare"] = 30
                    elif request.form[key_] == '2':
                        features_["Fare"] = 13
                    else:
                        features_["Fare"] = 7
                else:
                    features_[key_] = request.form[key_]

        # Inputing / Requesting Data
        data_ = pd.DataFrame(data=features_, index=[0])

        # Load trained - Pipeline
        predictions = make_prediction(input_data=data_)
        output_ = np.round(predictions['predictions'][0][1], 4)

        return render_template('predict.html',
                               prediction_text=output_ * 100,
                               prediction_class=request.form["Pclass"],
                               prediction_fare=features_["Fare"])
    else:
        pass


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 8000))
    application.run(debug=True, host='0.0.0.0', port=port)
