from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired('Username is required')])
    password = PasswordField('Password', [DataRequired('Please enter your password')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')


class RegistrationForm(FlaskForm):
    username = StringField('Username', [DataRequired('Username is required')])
    email = StringField('Email', [DataRequired('Email Required'), Email('Invalid Email')])
    password = PasswordField('Password', [DataRequired('Please enter your password')])
    password2 = PasswordField('Confirm Password', [DataRequired('Please re-enter your password'), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Username already exist, please use a different one or login instead!')

    def validate_email(self, email):
        email = User.query.filter_by(email=email.data).first()
        if email is not None:
            raise ValidationError('Email already exists, please use a different one or login instead')


