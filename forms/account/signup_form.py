from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, SubmitField, TextField,SelectField
from wtforms.validators import Required, Email
from wtforms.fields.html5 import EmailField
from models.state import STATE_CHOICES

#TODO: Move this to a common file.
# STATE_CHOICES = [('AL', 'Alabama'),('AK', 'Alaska'),('AZ', 'Arizona'),
#                 ('AR', 'Arkansas'),('CA', 'California'),('CO', 'Colorado'),
#                 ('CT', 'Connecticut'),('DE', 'Delaware'),('FL', 'Florida'),
#                 ('GA', 'Georgia'),('HI', 'Hawai'),('ID', 'Idaho'),
#                 ('IL', 'Illinois'),('IN', 'Indiana'),('IO', 'Iowa'),
#                 ('KS', 'Kansas'),('KY', 'Kentucky'),('LA', 'Louisiana'),
#                 ('ME', 'Maine'),('MD', 'Maryland'),('MA', 'Massachusetts'),
#                 ('MI', 'Missouri'),('MN', 'Minessota'),('MS', 'Mississippi'),
#                 ('MO', 'Montana'),('MT', 'Montana'),('NE', 'Nebraska'),
#                 ('NV', 'Nevada'),('NH', 'New Hampshire'),('NJ', 'New Jersey'),
#                 ('NM', 'New Mexico'),('NY', 'New York'),('NC', 'North Carolina'),
#                 ('ND', 'North Dakota'),('OH', 'Ohio'),('OK', 'Oklahoma'),
#                 ('OR', 'Oregon'),('PA', 'Pensylvania'),('RI', 'Rhode Island'),
#                 ('SC', 'South Carolina'),('SD', 'South Dakota'),('TN', 'Tenessee'),
#                 ('TX', 'Texas'),('UT', 'Utah'),('VT', 'Vermont'),
#                 ('VA', 'Virginia'),('WA', 'Washington'),('WV', 'West Virginia'),
#                 ('WI','Wisconsin'),('WY', 'Wyoming')]



class SignupForm(Form):
    firstname = TextField('Firstname', validators=[Required()])
    lastname = TextField('Lastname', validators=[Required()])
    barnumber = TextField('Barnumber', validators=[Required()])
    #state = TextField('State', validators=[Required()])
    state = SelectField(label='State', choices=STATE_CHOICES)
    username = TextField('Username', validators=[Required()])
    email = TextField('Email', validators=[Required()])
    #email = TextField('Email', validators=[Required(), Email()])
    password = PasswordField('Password', validators=[Required()])

