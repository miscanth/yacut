# Проект YaCut.

## Об авторе

Меня зовут Юлия, и учусь в ЯндексПрактикуме в 21 когорте курса «Python-разработчик плюс».

### Описание проекта и используемые технологии

Проект YaCut — это сервис укорачивания ссылок и API к нему.
Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.
Если пользователь не заполнит поле со своим вариантом короткой ссылки, то сервис сгенерирует её автоматически.

Ключевые возможности сервиса:

1) Генерация коротких ссылок и связь их с исходными длинными ссылками
2) Переадресация на исходный адрес при обращении к коротким ссылкам

Это полностью рабочий проект, бэкенд-приложение которого создано на базе **Flask**.
К проекту подключены следующие расширения для этого фреймворка:
* Адаптированная под Flask обёртка модуля WTForms — расширение **Flask-WTF**.
* Адаптированная под Flask обёртка модуля Alembic (специальная библиотека миграции баз данных для SQLAlchemy) — модуль **Flask-Migrate**.

К проекту так же подключено **ORM SQLAlchemy**. На этапе разработки использована база данных **SQLite**.

Для YaCut написан простой API-сервис без подключения специальных библиотек - ***REST API на Flask***.
API проекта доступен всем желающим. Сервис обслуживает только два эндпоинта:
* /api/id/ — POST-запрос на создание новой короткой ссылки;
* /api/id/<short_id>/ — GET-запрос на получение оригинальной ссылки по указанному короткому идентификатору;

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке: 
```
git clone git@github.com:miscanth/yacut.git
```
Cоздать и активировать виртуальное окружение: 
```
python3.9 -m venv venv 
```
* Если у вас Linux/macOS 

    ```
    source venv/bin/activate
    ```
* Если у вас windows 
 
    ```
    source venv/scripts/activate 
    ```
```
python3.9 -m pip install --upgrade pip
```
Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
Запустить проект:

```
flask run
```

### Примеры запросов:

Пример GET-запроса на получение оригинальной ссылки по указанному короткому идентификатору:

*GET .../api/id/helicopter/*

Пример ответа:
```
{
    "url": "https://github.com/readme/featured/nasa-ingenuity-helicopter"
}
```
Пример POST-запроса на создание новой короткой ссылки, в котором short_id содержит пустую строку:
```
{
    "url": "https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-types",
    "custom_id": ""
}
```

*POST .../api/id/*

Пример ответа:
```
{
    "short_link": "http://127.0.0.1:5000/StlGJB",
    "url": "https://docs.sqlalchemy.org/en/14/core/type_basics.html#generic-types"
}
```
