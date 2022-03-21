from flask import Blueprint, jsonify


auth = Blueprint('auth', __name__, url_prefix='/auth')


@auth.get('/')
def index():
    return jsonify({"mode": 'Hello'})
