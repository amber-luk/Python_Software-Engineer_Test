from wtforms import Form, SubmitField, StringField
from flask_wtf import FlaskForm as Form
from wtforms.validators import DataRequired

from app import app


class InputNumbers(Form): 
    """
    form that receives a list of numbers to add together
    """
    numbers_to_add = StringField(default='1,2,3, etc.', validators=[DataRequired()])
    submit = SubmitField("Submit")
