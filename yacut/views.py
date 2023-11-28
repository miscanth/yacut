from random import choice
import string

from flask import flash, redirect, render_template, request

from . import app, db
from .forms import URLMapForm
from .models import URLMap
from settings import pattern, SYMBOLS_QUANTITY


@app.route('/', methods=['GET', 'POST'])
def my_index_view():
    """Функция для главной страницы с формой для пользователя"""
    form = URLMapForm()
    if form.validate_on_submit():
        short_url = form.custom_id.data
        if not short_url:
            short_url = get_unique_short_id()
        elif not pattern.match(short_url):
            flash('Указано недопустимое имя для короткой ссылки.')
            return render_template('url_shorten.html', form=form)
        if URLMap.query.filter_by(short=short_url).first():
            flash('Предложенный вариант короткой ссылки уже существует.')
            return render_template('url_shorten.html', form=form)
        new_url = URLMap(
            original=form.original_link.data,
            short=short_url,
        )
        db.session.add(new_url)
        db.session.commit()
        short_url = request.host_url + short_url
        context = {'form': form, 'short_url': short_url}
        return render_template('url_shorten.html', **context)
    return render_template('url_shorten.html', form=form)


@app.route('/<string:short>')
def redirect_to_original(short):
    """Метод переадресации на исходный адрес
    при обращении к короткой ссылке"""
    link = URLMap.query.filter_by(short=short).first_or_404()
    if link:
        return redirect(link.original)


def get_unique_short_id():
    """Метод формирования коротких идентификаторов случайным образом"""
    return ''.join(choice(
        string.ascii_letters + string.digits
    ) for _ in range(SYMBOLS_QUANTITY))
