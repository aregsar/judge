from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField,RadioField,SelectField
from wtforms.validators import Required, Email
from models.state import STATE_CHOICES

class RetiredJudgeEditForm(Form):
    state = SelectField(label='State', choices=STATE_CHOICES)
    name = TextField('name', validators=[Required()])
    #state = TextField('state', validators=[Required()])

    #scope = TextField('scope', validators=[Required()])
    scope = RadioField('type', choices=[('1','Moderator&nbsp;&nbsp;'),('2','Arbitrator&nbsp;&nbsp;')],default='1')






