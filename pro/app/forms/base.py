from flask_wtf import FlaskForm
from wtforms import SubmitField


class HelloForm(FlaskForm):
    signin = SubmitField('Войти')
    register = SubmitField('Зарегестрироваться')