from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField,RadioField,SelectField
from wtforms.validators import Required, Email
from models.state import STATE_CHOICES

class RetiredJudgeEditForm(Form):
    name = TextField('name', validators=[Required()])
    #state = TextField('state', validators=[Required()])
    state = SelectField(label='State', choices=STATE_CHOICES)
    #scope = TextField('scope', validators=[Required()])
    scope = RadioField('type', choices=[('1','Moderator'),('2','Arbitrator')],default='1')






