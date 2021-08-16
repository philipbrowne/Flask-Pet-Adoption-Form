from flask_wtf import FlaskForm

from wtforms import StringField, FloatField, BooleanField, IntegerField, RadioField, SelectField

from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange


class NewPetForm(FlaskForm):
    """Form for Pets"""
    name = StringField('Pet Name', validators=[
                       InputRequired(message='Name cannot be blank')])
    species = StringField('Species (must be \"cat\", \"dog\", or \"porcupine\")', validators=[
        InputRequired(message='Must Select "cat", "dog", or "porcupine"'), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField('Photo URL', validators=[
        URL(message='Must be valid URL'), Optional()])
    age = IntegerField('Pet Age', validators=[Optional(), NumberRange(
        min=0, max=30, message="Must be a valid number between 0 and 30")])
    notes = StringField('Notes About Pet', validators=[Optional()])


class EditPetForm(FlaskForm):
    """Form for Pets"""
    name = StringField('Pet Name', validators=[
                       InputRequired(message='Name cannot be blank')])
    species = StringField('Species (must be \"cat\", \"dog\", or \"porcupine\")', validators=[
        InputRequired(message='Must Select "cat", "dog", or "porcupine"'), AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url = StringField('Photo URL', validators=[
        URL(message='Must be valid URL'), Optional()])
    age = IntegerField('Pet Age', validators=[Optional(), NumberRange(
        min=0, max=30, message="Must be a valid number between 0 and 30")])
    notes = StringField('Notes About Pet', validators=[Optional()])
    available = RadioField('Is this Pet Still Available for Adoption?', choices=[
                           (True, 'Yes'), (False, 'No')], validators=[InputRequired(message='Must select Yes or No')])
