from flask import render_template, redirect, url_for, Blueprint, session
from werkzeug.security import generate_password_hash, check_password_hash

users_blueprint = Blueprint(
    'users', __name__,
    template_folder="templates"
)

from .forms import *
from .models import UserModel


########################################################################## USER VIEWS ###################################################################################################################


## SIGN UP ##########################################################################
@users_blueprint.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    session['current_user'] = 'Guest'
    if form.validate_on_submit():
        if UserModel.find_by_username(form.username.data) or UserModel.find_by_email(form.email.data):
            return render_template('register.html', form=form, message="User already exists")

        hashed_password = generate_password_hash(form.password.data,
                                                 method='sha256')  ## password get hashed for security purposes
        new_user = UserModel(username=form.username.data, email=form.email.data, password=hashed_password)
        new_user.save_to_db()
        return redirect(url_for('users.login'))

    return render_template('register.html', form=form)  ## passing signup form to signup template


## LOGIN ############################################################################

@users_blueprint.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():  ## if form was submitted....
        user = UserModel.find_by_username(username=form.username.data)
        if user:
            if check_password_hash(user.password, form.password.data):
                session['current_user'] = user.username
                return redirect(url_for('digit_recognition.digit_recognition'))

        return render_template('login.html', form=form, message="Invalid Username or Password")

    return render_template('login.html', form=form)  ## passing login form to login template


## LOGOUT ###########################################################################

@users_blueprint.route('/logout')
def logout():
    session['current_user'] = 'Guest'
    return redirect(url_for('users.login'))