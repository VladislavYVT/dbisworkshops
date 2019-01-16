from flask_wtf import FlaskForm
from wtforms import (StringField,
                     DateField,
                     RadioField,
                     SubmitField,
                     validators)


class RegistrationForm(FlaskForm):
    login = StringField('Email: ', validators=[
        validators.DataRequired('Required'),
        validators.Length(30)])
    password = StringField('Password: ', validators=[
        validators.DataRequired('Required'),
        validators.Length(30)])
    first_name = StringField('First name: ', validators=[
        validators.DataRequired('Required'),
        validators.Length(30)])
    last_name = StringField('Last name: ', validators=[
        validators.DataRequired('Required'),
        validators.Length(30)])
    birth_day = DateField('Birth day: ', validators=[
        validators.DataRequired('Required')
    ])
    sex = RadioField('Sex: ', choices=[
        ('M', 'Male'),
        ('F', 'Female')
    ])
    registration = SubmitField('Registration')
