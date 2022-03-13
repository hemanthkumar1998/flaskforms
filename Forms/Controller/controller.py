from flask_wtf import FlaskForm
from wtforms import SelectField, StringField
from wtforms.validators import DataRequired
from Forms.constants import STATEDATA

class DataForm(FlaskForm):
    name = name = StringField('Name', validators=[DataRequired()])
    state = SelectField('State',choices=['Andaman Nicobar','Andhra Pradesh','Karnataka','Maharashtra'],validators=[DataRequired()])
    city = SelectField('City',choices=[],validators=[DataRequired()])
    pincode = SelectField('Pincode',choices=[],validators=[DataRequired()])
    

def get_cities(state):
    """Function that gets the city based on the state"""
    cities_data = STATEDATA[state]
    cities = []
    for city in cities_data.keys():
        cities.append(city)
    return cities

def get_pincodes(state, city):
    """Function that gets the Pincode based on the State and City"""
    pincode_data = STATEDATA[state][city]
    return pincode_data
