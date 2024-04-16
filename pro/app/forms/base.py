from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired


class HelloForm(FlaskForm):
    signin = SubmitField('Войти')
    register = SubmitField('Зарегестрироваться')