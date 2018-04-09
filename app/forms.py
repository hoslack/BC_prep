from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', [DataRequired('Username is required')])
    password = PasswordField('Password', [DataRequired('Please enter your password')])
    remember_me = BooleanField('Remember me')
    submit = SubmitField('Submit')

