from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField, BooleanField
from wtforms.validators import DataRequired
from flask_login import *


class SigninForm(FlaskForm, UserMixin):
    email = EmailField('Почта/email', validators=[DataRequired()])
    password = PasswordField('Пароль/password', validators=[DataRequired()])
    remember_me = BooleanField('Запомнить меня/remember me')
    submit = SubmitField('Войти/sign in')
