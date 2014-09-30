from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import Required, Email


class JudgeEditForm(Form):
    name = TextField('name', validators=[Required()])
    state = TextField('state', validators=[Required()])
    scope = TextField('scope', validators=[Required()])
    #scope = RadioField('Label', choices=[(1,'State'),(2,'Federal')])
    #scope = RadioField('Label', choices=[('1','State'),('2','Federal')],coerce=int,default=2, validators=[Required()])

