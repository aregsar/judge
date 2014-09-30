from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField
from wtforms.validators import Required, Email


STATE_ABBREV = ['AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'HI', 'ID', 'IL', 'IN', 'IO', 'KS', 'KY', 'LA', 'ME', 'MD',
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY']

#TODO: Move this to a common file.
STATE_CHOICES = [('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AL', 'Alabama'),('AL', 'Alabama'),('AL', 'Alabama'),
                ('AK','Alaska'),('AL', 'Alabama')]

#from wtforms.fields.html5 import EmailField

class SignupForm(Form):
    firstname = TextField('Firstname', validators=[Required()])
    lastname = TextField('Lastname', validators=[Required()])
    barnumber = TextField('Barnumber', validators=[Required()])
    state = TextField('State', validators=[Required()])
    #state = wtforms.SelectField(label='State', choices=STATE_CHOICES)
    username = TextField('Username', validators=[Required()])
    email = TextField('Email', validators=[Required()])
    #email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])

