from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Post(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created = db.Column(
        db.DateTime(timezone=True), nullable=False, default=datetime.utcnow
    )
    title = db.Column(db.Text, nullable=False)
    content = db.Column(db.Text, nullable=False)
