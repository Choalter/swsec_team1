from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo, Email
from wtforms.fields.html5 import EmailField


class MenuUploadForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    price = StringField('Price', validators=[DataRequired()])
    ingredients = TextAreaField('Ingredients'
                                , validators=[DataRequired()])


class UserCreateForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password1 = PasswordField('Password', validators=[DataRequired(), EqualTo('password2', 'Incorrect Password')])
    password2 = PasswordField('Check Password', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    access = StringField('Types', validators=[DataRequired()])


class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=20)])
    password = PasswordField('Password', validators=[DataRequired()])
