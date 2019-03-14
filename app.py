## App Utilities
import os
# import env
from db import db

from flask import Flask, render_template, session
from flask_uploads import UploadSet, configure_uploads, IMAGES
from flask_bootstrap import Bootstrap
from flask_restful import Api

from project.classify_image.resources import ImageClassify


## App Settings
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['UPLOADED_PHOTOS_DEST'] = 'static/uploads'
app.config['DEBUG'] = True
api = Api(app)
Bootstrap(app)


## Image upload handling - Cat & Dog Classifier
photos = UploadSet('photos', IMAGES)                                            ## image upload handling
configure_uploads(app, photos)



api.add_resource(ImageClassify, '/imageclassify')




from project.users.views import users_blueprint
from project.digit_recognition.views import digit_recognition_blueprint
from project.cat_dog_classifier.views import cat_dog_classifier_blueprint
from project.classify_image.views import classify_image_blueprint

app.register_blueprint(users_blueprint)
app.register_blueprint(digit_recognition_blueprint)
app.register_blueprint(cat_dog_classifier_blueprint)
app.register_blueprint(classify_image_blueprint)





## User Login ######################### ########################################################

@app.context_processor
def context_processor():
    current_user = session.get('current_user') or 'Guest'
    return dict(current_user=current_user)


@app.errorhandler(404)
def error404(error):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error500(error):
    return render_template('500.html'), 500


@app.route('/')
def dashboard():
    return render_template('dashboard.html')


## DB INIT
db.init_app(app)

## APP INITIATION
if __name__ == '__main__':

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 