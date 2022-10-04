from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, InputRequired


class SignupForm(FlaskForm):
    inputname = StringField('name', [DataRequired('loi roi dmm')])
    inputemail = StringField('email', )
    inputpassword = PasswordField('password', )
    inputzip = StringField('zip', )
    inputaddress = StringField('address', )
    inputcity = StringField('city', )
    inputstate = StringField('state', )
    inputcomfirmpassword = PasswordField('comfirmpassword')
    submit = SubmitField('sign up')
