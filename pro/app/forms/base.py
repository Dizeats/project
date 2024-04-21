from flask_wtf import FlaskForm
from wtforms import SubmitField


class HelloForm(FlaskForm):
    signin = SubmitField('Войти/Sign in')
    register = SubmitField('Зарегестрироваться/Sign up')