from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, SelectField
from wtforms import BooleanField, HiddenField, DateTimeField, IntegerField,RadioField
from wtforms.validators import Required,length
from wtforms.widgets import TextArea

RATING_CHOICES = [('1', '1&nbsp;&nbsp;'),('2', '2&nbsp;&nbsp;'),
('3', '3&nbsp;&nbsp;'),('4', '4&nbsp;&nbsp;'),('5', '5&nbsp;&nbsp;')]
RATING_CHOICE_DEFAULT='5'
# RATING_SELECT_CHOICES = [('1', '1'),('2', '2'),
# ('3', '3'),('4', '4'),('5', '5')]

class AddReviewForm(Form):
#,default='5'
    knowledge = RadioField('knowledge', choices=RATING_CHOICES,default=None, validators=[Required()])
    decorum = RadioField('decorum', choices=RATING_CHOICES, validators=[Required()])
    tentatives = RadioField('tentatives', choices=RATING_CHOICES,default=RATING_CHOICE_DEFAULT, validators=[Required()])
    curiosity = RadioField('curiosity', choices=RATING_CHOICES,default=RATING_CHOICE_DEFAULT, validators=[Required()])
    body = StringField('Review', widget=TextArea(), validators=[Required()])
    #body = StringField(u'Review', widget=TextArea(), validators=[Required()])
    #body = TextField('Review', validators=[Required()])
    #cols="35", rows="20",
    #body = TextAreaField("Review",  [validators.Required()])
    #rating = IntegerField('Rating', validators=[Required()])


