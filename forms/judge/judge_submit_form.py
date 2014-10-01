from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField,SelectField
from wtforms.validators import Required, Email
from models.state import STATE_CHOICES

class JudgeSubmitForm(Form):
    judge_name = TextField('name', validators=[Required()])
    #state = SelectField(label='State', choices=STATE_CHOICES)
    #state = TextField('state', validators=[Required()])
    #retired = BooleanField('retired', default=False)

