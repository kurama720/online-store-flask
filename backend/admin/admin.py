from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import abort

from backend.db import db
from backend.accounts.models import User
from backend.admin.models import AdminUser
from backend.shop.models import Category, Product


class PermissionController(ModelView):
    """Class for admin panel security"""

    @jwt_required()
    def is_accessible(self):
        """Return 404 if requesting user is not an admin"""
        current_user = get_jwt_identity()
        if isinstance(current_user, str):
            return True
        else:
            return False


admin = Admin(name='Online store', template_mode='bootstrap3')
# Register models in admin panel
admin.add_view(PermissionController(User, db.session, name='Users'))
admin.add_view(PermissionController(AdminUser, db.session, name='Admin Users'))
admin.add_view(PermissionController(Category, db.session, name='Categories'))
admin.add_view(PermissionController(Product, db.session, name='Products'))
