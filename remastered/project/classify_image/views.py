from flask import Blueprint
from flask import render_template
from flask_restful import Api, Resource





## BLUEPRINT INIT

classify_image_blueprint = Blueprint(
    'classify_image', __name__,
    template_folder="templates"
)






############################################################################# VIEWS #####################################################################################################################################


### MAIN PAGE


@classify_image_blueprint.route('/classify', methods=['GET', 'POST'])
def classify():

    return render_template("classify_image.html")