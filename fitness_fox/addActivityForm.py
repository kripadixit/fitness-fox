from flask_wtf import FlaskForm

from wtforms import Form
from wtforms import DateField, IntegerField, TextField, PasswordField, BooleanField, StringField, SubmitField
from flask_sqlalchemy import SQLAlchemy
from wtforms_components import TimeField, read_only
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError

from wtforms.validators import DataRequired

class addActivityForm(FlaskForm):
