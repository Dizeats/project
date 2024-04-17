from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class HomepageForm(FlaskForm):
    name_product = StringField('Название продукта', validators=[DataRequired()])
    submit = SubmitField('Добавить')
