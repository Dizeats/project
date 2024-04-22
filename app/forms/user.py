from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import DataRequired


class RegisterForm(FlaskForm):
    email = EmailField('Почта/email', validators=[DataRequired()])
    password = PasswordField('Пароль/password', validators=[DataRequired()])
    password_again = PasswordField('Повторите пароль/password again', validators=[DataRequired()])
    submit = SubmitField('Зарегестрироваться/sign up')