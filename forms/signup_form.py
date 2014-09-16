from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import Required, Email


class SignupForm(Form):
    username = TextField('Username', validators=[Required()])
    barnumber = TextField('Barnumber', validators=[Required()])
    email = TextField('Email', validators=[Required()])
    #email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])

