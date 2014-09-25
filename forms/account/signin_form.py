from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import Required, Email

class SigninForm(Form):
    #email = TextField('Email', validators=[Required(), Email()])
    email = TextField('Email', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
