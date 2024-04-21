from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class HomepageForm(FlaskForm):
    name_added_product = StringField('Название продукта', validators=[DataRequired()])
    name_deleted_product = StringField('Название продукта', validators=[DataRequired()])
    add = SubmitField('Добавить')
    delete = SubmitField('Удалить')
    clear = SubmitField('Очистить список')
