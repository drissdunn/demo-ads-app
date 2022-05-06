from sys import float_info
import numpy as np
from flask import Flask, render_template, request, jsonify
import pickle
import sklearn 
import os

# Create flask app
flask_app = Flask(__name__)
model = pickle.load(open("rff.pkl", "rb"))

# picFolder = os.path.join('static', 'images')

# flask_app.config['UPLOAD_FOLDER'] = picFolder

@flask_app.route("/")
def Home():
    return render_template("index.html")

@flask_app.route("/result", methods = ["POST"])
def result():
    float_features = [float(x) for x in request.form.values()]
    features = [np.array(float_features)] 
    prediction = model.predict(features)
    if prediction == 0:
        picFolder = os.path.join('static', 'samsung')
        flask_app.config['UPLOAD_FOLDER'] = picFolder

        Samsung = os.listdir('static/samsung')
        samsung = ['samsung/' + image for image in Samsung]

        return render_template("result.html", imagelist = samsung, prediction_text = "You're receiving this Ads because of your recent interaction with Samsung brand")

    elif prediction == 1:
        picFolder = os.path.join('static', 'apple')
        flask_app.config['UPLOAD_FOLDER'] = picFolder

        Apple = os.listdir('static/apple')
        apple = ['apple/' + image for image in Apple]
        return render_template("result.html", imagelist = apple, prediction_text = "You're receiving this Ads because of your recent interaction with Apple brand")

    elif prediction == 2:
        picFolder = os.path.join('static', 'xiaomi')
        flask_app.config['UPLOAD_FOLDER'] = picFolder

        Xiaomi = os.listdir('static/xiaomi')
        xiaomi = ['xiaomi/' + image for image in Xiaomi]
        return render_template("result.html", imagelist = xiaomi, prediction_text = "You're receiving this Ads because of your recent interaction with Xiaomi brand")

    elif prediction == 3:
        picFolder = os.path.join('static', 'huawei')
        flask_app.config['UPLOAD_FOLDER'] = picFolder

        Huawei = os.listdir('static/huawei')
        huawei = ['huawei/' + image for image in Huawei]
        return render_template("result.html", imagelist = huawei, prediction_text = "You're receiving this Ads because of your recent interaction with Huawei brand")

    elif prediction == 4:
        picFolder = os.path.join('static', 'oppo')
        flask_app.config['UPLOAD_FOLDER'] = picFolder

        Oppo = os.listdir('static/oppo')
        oppo = ['oppo/' + image for image in Oppo]
        return render_template("result.html", imagelist = oppo, prediction_text = "You're receiving this Ads because of your recent interaction with Oppo brand")
 
    else: 
        return render_template("result.html", prediction_text = "Please input valid details")

if __name__ == "__main__":
    flask_app.run(debug=True)