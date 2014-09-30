from flask.ext.wtf import Form
from wtforms import StringField, SubmitField, TextField, SelectField
from wtforms import BooleanField, HiddenField, DateTimeField, IntegerField,RadioField
from wtforms.validators import Required,length
from wtforms.widgets import TextArea

class AddReviewForm(Form):
    rating = RadioField('rating', choices=[('1','1'),('2','2'),('3','3'),
                        ('4','4'),('5','5')], validators=[Required()])
    knowledge = RadioField('knowledge', choices=[('1','1'),('2','2'),('3','3'),
                        ('4','4'),('5','5')], validators=[Required()])
    decorum = RadioField('decorum', choices=[('1','1'),('2','2'),('3','3'),
                        ('4','4'),('5','5')], validators=[Required()])
    tentatives = RadioField('tentatives', choices=[('1','1'),('2','2'),('3','3'),
                        ('4','4'),('5','5')], validators=[Required()])
    curiosity = RadioField('curiosity', choices=[('1','1'),('2','2'),('3','3'),
                        ('4','4'),('5','5')], validators=[Required()])
    title = TextField('Title', validators=[Required(),length(max=255)])
    #body = TextField('Review', validators=[Required()])
    #cols="35", rows="20",
    #body = TextAreaField("Review",  [validators.Required()])
    body = StringField(u'Review', widget=TextArea(), validators=[Required()])
    #rating = IntegerField('Rating', validators=[Required()])


