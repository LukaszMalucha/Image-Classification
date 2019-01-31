from flask import request, Blueprint
from flask import render_template, request

import numpy as np
import keras
from keras.models import load_model

from skimage.io import imread
from skimage.transform import resize
import os.path

## BLUEPRINT INIT

cat_dog_classifier_blueprint = Blueprint(
    'cat_dog_classifier', __name__,
    template_folder="templates"
)

## DEFINE ALLOWED TEMPLATE FILE FORMAT ##############################################

ALLOWED_EXTENSIONS = set(['jpg'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


## MODEL ############################################################################

my_path = os.path.abspath(os.path.dirname(__file__))
cat_dog_classifier = os.path.join(my_path, "../../static/cat_dog_classifier/cat_dog_classifier.h5")


############################################################################# VIEWS #####################################################################################################################################


### MAIN PAGE


@cat_dog_classifier_blueprint.route('/classifier', methods=['GET', 'POST'])
def classifier():
    return render_template("cat_dog_classifier.html")


@cat_dog_classifier_blueprint.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        img = request.files['photo']
        if allowed_file(img.filename):
            keras.backend.clear_session()  ## clear Tensor session to avoid error
            image_classifier = load_model(cat_dog_classifier)  ## load saved model
            class_labels = {0: 'Cat', 1: 'Dog'}  ## prepare labels
            img = imread(request.files['photo'])  ## read photo & transform it into array
            img = resize(img, (128, 128))
            img = np.expand_dims(img, axis=0)
            if (np.max(img) > 1):
                img = img / 255.0
            prediction = image_classifier.predict_classes(img)  ## predict class
            guess = class_labels[prediction[0][0]]  ## for website display
            keras.backend.clear_session()  ## clear Tensor session to avoid error

            return render_template("cat_dog_classify.html", guess=guess)
        else:
            return render_template("cat_dog_classifier.html")
