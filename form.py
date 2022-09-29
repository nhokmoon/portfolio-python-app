from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField


class SignupForm(FlaskForm):
    inputname = StringField(required=True, default="")
    inputemail = StringField(required=True, default="")
    inputpassword = PasswordField(required=True, default="")
    submit = SubmitField('sign up')
