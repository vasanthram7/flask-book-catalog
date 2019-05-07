from  flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,BooleanField
from wtforms.validators import DataRequired,Length,Email,EqualTo, ValidationError
from app.auth.models import User

def email_exists(form, field):
    email= User.query.filter_by(user_email=field.data).first()
    if email:
        raise ValidationError('Email Already Exists')



class RegistrationForm(FlaskForm):
    name= StringField('Name', validators=[DataRequired(), Length(4,25, message='Should be more than 4 less than 25 char')])
    email= StringField('Email', validators=[DataRequired(), Email(), email_exists] )
    password = PasswordField('Password', validators=[DataRequired(), Length(6)])
    confirm = PasswordField('Confirm', validators=[DataRequired(), EqualTo('password', message='Password must match')])
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(6)])
    stay_loggedin = BooleanField('Stay logged-in')
    submit = SubmitField('Login')



# from flask_wtf import FlaskForm
# from wtforms import StringField, SubmitField
#
#
# class RegistrationForm(FlaskForm):
#     name = StringField('Whats your name')
#     email = StringField('Enter your Email')
#     submit = SubmitField('Register')

# INCREMENTAL CODE FOR SECTION : 11 LECTURE : 44 - VALIDATING FORMS
# auth/forms.py

