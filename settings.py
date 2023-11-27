import os
import re


class Config(object):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URI')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv('SECRET_KEY')


SYMBOLS_QUANTITY = 6
MAX_ORIGINAL_LENGTH = 400
MAX_SHORT_ID_LENGTH = 16
pattern = re.compile(r'^([a-zA-Z0-9_]{1,16})$')
