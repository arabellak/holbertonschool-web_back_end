#!/usr/bin/env python3
"""
Manage the API authentication.
"""
from flask import request, jsonify
from models.user import User
from os import getenv
from api.v1.views import app_views


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    psswrd = request.form.get('password')
    if not psswrd:
        return jsonify({"error": "password missing"}), 400

    try:
        users = User.search({'email': email})
    except Exception:
        return jsonify({"error": "no user found for this email"}), 404

    for user in users:
        if not user.is_valid_password(psswrd):
            return jsonify({"error": "wrong password"}), 401
        else:
            from api.v1.app import auth
            iD = user.id
            create = auth.create_session(iD)
            resu = jsonify(user.to_json())
            se_name = getenv('SESSION_NAME')
            resu.set_cookie(se_name, create)
    return resu
