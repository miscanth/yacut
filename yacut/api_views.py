from flask import jsonify, request

from . import app, db
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .views import get_unique_short_id
from settings import pattern


def replacements_key_data(data):
    # Метод соотнесения ключей из json запроса к полям модели URLMap
    data['original'] = data.pop('url')
    data['short'] = data.pop('custom_id')


@app.route('/api/id/<string:short_id>/', methods=['GET'])
def get_original_link(short_id):
    # GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is not None:
        return jsonify({'url': url_map.original}), 200
    raise InvalidAPIUsage('Указанный id не найден', 404)


@app.route('/api/id/', methods=['POST'])
def generate_short_link():
    # POST-запрос на создание новой короткой ссылки
    data = request.get_json()
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    if 'url' not in data:
        raise InvalidAPIUsage('\"url\" является обязательным полем!')
    if 'custom_id' not in data or data['custom_id'] in ['', None]:
        data['custom_id'] = get_unique_short_id()
    else:
        if not pattern.match(data['custom_id']):
            raise InvalidAPIUsage('Указано недопустимое имя для короткой ссылки', 400)
        if URLMap.query.filter_by(short=data['custom_id']).first() is not None:
            raise InvalidAPIUsage('Предложенный вариант короткой ссылки уже существует.')
    url_map = URLMap()
    replacements_key_data(data)
    url_map.from_dict(data)
    db.session.add(url_map)
    db.session.commit()
    return jsonify(
        {'url': url_map.original,
         'short_link': request.host_url + url_map.short}), 201
