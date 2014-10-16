from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import Required, Email,Length

class SigninForm(Form):
    #email = TextField('Email', validators=[Required(), Email()])
    email = TextField('Email', validators=[Required(), Email(),Length(max=100)])
    password = PasswordField('Password', validators=[Required(),Length(max=100)])
