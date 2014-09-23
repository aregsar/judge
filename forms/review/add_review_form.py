from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, SelectField
from wtforms import BooleanField, HiddenField, DateTimeField, IntegerField
from wtforms.validators import Required,length
from wtforms.widgets import TextArea

class AddReviewForm(Form):
    title = TextField('Title', validators=[Required(),length(max=255)])
    #body = TextField('Review', validators=[Required()])
    #cols="35", rows="20",
    body = StringField(u'Review', widget=TextArea(), validators=[Required()])
    #rating = TextField('Rating', validators=[Required()])
    rating = IntegerField('Rating', validators=[Required()])

