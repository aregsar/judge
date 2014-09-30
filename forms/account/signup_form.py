from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import Required, Email


class SignupForm(Form):
    firstname = TextField('Firstname', validators=[Required()])
    lastname = TextField('Lastname', validators=[Required()])
    barnumber = TextField('Barnumber', validators=[Required()])
    state = TextField('State', validators=[Required()])
    username = TextField('Username', validators=[Required()])
    email = TextField('Email', validators=[Required()])
    #email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])

