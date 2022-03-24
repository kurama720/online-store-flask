from datetime import datetime

from sqlalchemy import Column, Integer, String, Index, ForeignKey, Text, Numeric, Boolean, DateTime
from sqlalchemy.orm import relationship

from backend.db import db
from backend.accounts.models import User


class Category(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    products = relationship('Product', backref='product_list')

    def __repr__(self):
        return f"Category: {self.name}"


category_name_index = Index('category_name', Category.name)


class Product(db.Model):
    id = Column(Integer, primary_key=True)
    category = Column(Integer, ForeignKey('category.id'))
    owner = Column(Integer, ForeignKey(User.id))
    name = Column(String(200), nullable=False)
    image = Column(String(400))
    description = Column(Text)
    price = Column(Numeric(decimal_return_scale=2), nullable=False)
    available = Column(Boolean, default=True)
    created = Column(DateTime, default=datetime.now())
    updated = Column(DateTime, onupdate=datetime.now())

    def __repr__(self):
        return f"Product: {self.name}"