import datetime

from sqlalchemy import Column, Integer, String, Text, DateTime
from sqlalchemy.orm import relationship

from backend.db import db


class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(DateTime, default=datetime.datetime.now())
    products = relationship('Product', backref='owned_products')

    def __repr__(self):
        return f"User: {self.email}"
