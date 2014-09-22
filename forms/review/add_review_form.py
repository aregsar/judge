from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, SelectField
from wtforms import BooleanField, HiddenField, DateTimeField, IntegerField
from wtforms.validators import Required,length

class AddReviewForm(Form):
    title = TextField('Title', validators=[Required(), length(max=255)])
    body = TextField('Review', validators=[Required()])
    rating = IntegerField('Rating (1 to 5)', validators=[Required()])

