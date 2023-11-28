from datetime import datetime

from . import db
from settings import MAX_ORIGINAL_LENGTH, MAX_SHORT_ID_LENGTH


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_ORIGINAL_LENGTH), nullable=False)
    short = db.Column(
        db.String(MAX_SHORT_ID_LENGTH), nullable=False, unique=True
    )
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def to_dict(self):
        """Метод сериализации объекта модели в словарь"""
        return dict(
            id=self.id,
            original=self.original,
            short=self.short,
            timestamp=self.timestamp
        )

    def from_dict(self, data):
        """Метод-десериализатор"""
        for field in ['original', 'short']:
            if field in data:
                setattr(self, field, data[field])
