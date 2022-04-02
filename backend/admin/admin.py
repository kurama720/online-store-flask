from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask import abort

from backend.db import db
from backend.accounts.models import User
from backend.shop.models import Category, Product


class PermissionController(ModelView):
    """Class for admin panel security"""

    @jwt_required()
    def is_accessible(self):
        """Return 403 if requesting user is not staff"""
        current_user = get_jwt_identity()
        user = User.query.filter_by(id=current_user).first_or_404()
        if not user.is_staff:
            return abort(403)


admin = Admin(name='Online store', template_mode='bootstrap3')
# Register models in admin panel
admin.add_view(PermissionController(User, db.session, name='Users'))
admin.add_view(PermissionController(Category, db.session, name='Categories'))
admin.add_view(PermissionController(Product, db.session, name='Products'))
