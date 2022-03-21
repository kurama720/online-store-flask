import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime

from backend.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now())

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User: {self.email}"
