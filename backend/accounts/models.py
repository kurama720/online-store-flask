from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean
from sqlalchemy.orm import relationship

from backend.db import db


class AbstractBaseUser(db.Model):
    __abstract__ = True
    email = Column(String(120), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    created_at = Column(DateTime, default=db.func.now())
    is_staff = Column(Boolean, default=False)


class User(AbstractBaseUser):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    products = relationship('Product', backref='owner', cascade="all, delete-orphan")

    def __repr__(self):
        return f"User: {self.email}"
