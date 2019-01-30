from flask import render_template, request, Blueprint, session
from flask import Flask, render_template, current_app, request, redirect, url_for, flash
from flask_uploads import UploadSet, configure_uploads, IMAGES

import numpy as np
import keras
import h5py
from keras.models import load_model

from skimage.io import imread
from skimage.transform import resize



## BLUEPRINT INIT

cat_dog_classifier_blueprint = Blueprint(
    'cat_dog_classifier', __name__,
    template_folder="templates"
)


############################################################################# VIEWS #####################################################################################################################################


### MAIN PAGE



@cat_dog_classifier_blueprint.route('/classifier', methods=['GET', 'POST'])
def classifier():

    return render_template("cat_dog_classifier.html")
