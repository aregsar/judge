from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import Required, Email


class JudgeEditForm(Form):
    name = TextField('name', validators=[Required()])