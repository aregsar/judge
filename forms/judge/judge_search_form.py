from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField,SelectField
from wtforms.validators import Required, Email
from models.state import STATE_CHOICES

class JudgeSearchForm(Form):
    name = TextField('Name', validators=[Required()])
    state = SelectField(label='State', choices=STATE_CHOICES)

