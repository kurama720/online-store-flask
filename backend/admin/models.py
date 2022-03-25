from sqlalchemy import Column, Integer, Boolean

from backend.accounts.models import AbstractBaseUser


class AdminUser(AbstractBaseUser):
    __tablename__ = 'admins'

    id = Column(Integer, primary_key=True)

    def __repr__(self):
        return f"Admin: {self.email}"
