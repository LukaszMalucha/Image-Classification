from flask import render_template, request, Blueprint, session

from scipy.misc import imread, imresize
import numpy as np

import os
import base64
import re
import sys

## BLUEPRINT INIT

digit_recognition_blueprint = Blueprint(
    'digit_recognition', __name__,
    template_folder="templates"
)

from project.digit_recognition.load import init_model

sys.path.append(os.path.abspath(",/model"))

global model, graph


## Image Converter from str to b64
def convertImage(imgData1):
    imgstr = re.search(b'base64,(.*)', imgData1).group(1)
    with open('output.png', 'wb') as output:
        output.write(base64.b64decode(imgstr))


## User Login
@digit_recognition_blueprint.context_processor
def context_processor():
    current_user = session.get('current_user') or 'Guest'
    return dict(current_user=current_user)


############################################################################# VIEWS #####################################################################################################################################


@digit_recognition_blueprint.route('/digit_recognition')
def digit_recognition():
    return render_template("digit_recognition.html")


@digit_recognition_blueprint.route('/predict', methods=['GET', 'POST'])
def predict():
    model, graph = init_model()
    imgData = request.get_data()

    ## transform
    convertImage(imgData)
    x = imread('output.png', mode='L')
    x = np.invert(x)
    x = imresize(x, (28, 28))
    x = x.reshape(1, 28, 28, 1)
    ## predict
    with graph.as_default():
        out = model.predict(x)
        print(np.argmax(out, axis=1))
        response = np.array_str(np.argmax(out, axis=1))
        response = ' '.join(map(str, response))
        response = response.replace('[', '')
        response = response.replace(']', '')
        return response
