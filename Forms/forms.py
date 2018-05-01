from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[InputRequired()])
    retype_pass = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign In')