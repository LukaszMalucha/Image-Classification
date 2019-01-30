from flask import session, Response, render_template,redirect
from werkzeug.security import generate_password_hash, check_password_hash
from flask_restful import Resource
from models.user import UserModel
from models.forms import RegisterForm, LoginForm


class UserRegister(Resource):


    def get(self):
        form = RegisterForm()
        return Response(render_template('user/register.html', form=form))  ## passing signup form to signup template

    def post(self):
        form = RegisterForm()
        session['current_user'] = 'Guest'
        if form.validate_on_submit():
            if UserModel.find_by_username(form.username.data) or UserModel.find_by_email(form.email.data):
                return Response (render_template('user/register.html', form=form, message="User already exists"))

            hashed_password = generate_password_hash(form.password.data,
                                                     method='sha256')  ## password get hashed for security purposes
            new_user = UserModel(username=form.username.data, email=form.email.data, password=hashed_password)
            new_user.save_to_db()
            return redirect ("login")

        return Response(render_template('user/register.html', form=form))  ## passing signup form to signup template


class UserLogin(Resource):

    def get(self):
        form = LoginForm()

        return Response(render_template('user/login.html', form=form))  ## passing login form to login template

    def post(self):
        form = LoginForm()

        if form.validate_on_submit():  ## if form was submitted....
            user = UserModel.find_by_username(username=form.username.data)
            if user:
                if check_password_hash(user.password, form.password.data):
                    session['current_user'] = user.username
                    return redirect("/")

            return Response(render_template('user/login.html', form=form, message="Invalid Username or Password"))


class UserLogout(Resource):

    def get(self):
        session['current_user'] = 'Guest'
        return redirect("login")


