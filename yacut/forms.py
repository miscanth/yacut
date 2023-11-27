from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, URL

from settings import MAX_ORIGINAL_LENGTH, MAX_SHORT_ID_LENGTH


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=[DataRequired(message='Обязательное поле'),
                    Length(1, MAX_ORIGINAL_LENGTH), URL(require_tld=True, message='Введите существующую ссылку')]
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=[Length(1, MAX_SHORT_ID_LENGTH), Optional()]
    )
    submit = SubmitField('Создать')
