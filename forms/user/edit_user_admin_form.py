from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, SelectField
from wtforms import BooleanField, HiddenField, DateTimeField, IntegerField
from wtforms.validators import Required,length


class EditUserAdminForm(Form):
    banned = BooleanField('Banned', default=False)
