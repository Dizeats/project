from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class HomepageForm(FlaskForm):
    name_added_product = StringField('Название продукта/name of product', validators=[DataRequired()])
    name_deleted_product = StringField('Название продукта/name of product', validators=[DataRequired()])
    add = SubmitField('Добавить/add')
    delete = SubmitField('Удалить/delete')
    clear = SubmitField('Очистить список/clear list')
