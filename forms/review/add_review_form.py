from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, SelectField
from wtforms import BooleanField, HiddenField, DateTimeField, IntegerField,RadioField
from wtforms.validators import Required,length
from wtforms.widgets import TextArea

RATING_CHOICES = [('1', '1'),('2', '2'),('3', '3'),('4', '4'),('5', '5')]

class AddReviewForm(Form):
#,default='5'
    rating = RadioField('rating', choices=RATING_CHOICES,default='5', validators=[Required()])
    knowledge = SelectField('knowledge', choices=RATING_CHOICES,default='5', validators=[Required()])
    decorum = SelectField('decorum', choices=RATING_CHOICES,default='5', validators=[Required()])
    tentatives = SelectField('tentatives', choices=RATING_CHOICES,default='5', validators=[Required()])
    curiosity = SelectField('curiosity', choices=RATING_CHOICES,default='5', validators=[Required()])
    title = TextField('Title', validators=[Required(),length(max=255)])
    body = StringField('Review', widget=TextArea(), validators=[Required()])
    #body = StringField(u'Review', widget=TextArea(), validators=[Required()])
    #body = TextField('Review', validators=[Required()])
    #cols="35", rows="20",
    #body = TextAreaField("Review",  [validators.Required()])
    #rating = IntegerField('Rating', validators=[Required()])


