from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import InputRequired, Email, ValidationError, Length, EqualTo

from config.config import db
from database.db import dict_factory


def arr_factory(cursor, row):
    return row[0]


def unique_email(form, field):
    db.row_factory = arr_factory
    cur = db.cursor()
    res = cur.execute('''SELECT email FROM user''')
    emails = res.fetchall()
    cur.close()
    db.row_factory = dict_factory
    if emails and field.data in emails:
        raise ValidationError('This email is already associated with an account!')


class SignUpForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email('Please enter a valid email address.'), unique_email])
    password = PasswordField('Password', validators=[InputRequired(), Length(3, 20, 'Password must be between 3 and 20 characters.'),
                                                     EqualTo('retype_pass', message='Passwords must match.')])
    retype_pass = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign Up')


class SignInForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(), Email('Please enter a valid email address.')])
    password = PasswordField('Password', validators=[InputRequired()])
    submit = SubmitField('Sign In')