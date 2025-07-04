#!/usr/bin/env python3
"""This module defines views for handling session authentication routes using Flask.
"""
from flask import jsonify, request, abort
from api.v1.views import app_views
from api.v1.app import auth
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def session_auth_login() -> str:
    """
    Handles user login and session creation for session authentication.
    Returns a JSON response with user data and sets a session cookie.
    """
    email = request.form.get('email')
    password = request.form.get('password')

    if not email:
        return jsonify({"error": "email missing"}), 400

    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({'email': email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    # Import here to avoid circular import issues
    from api.v1.app import auth
    session_id = auth.create_session(user.id)

    response = jsonify(user.to_json())
    cookie_name = os.getenv("SESSION_NAME")
    response.set_cookie(cookie_name, session_id)

    return response


@app_views.route(
    '/auth_session/logout', methods=['DELETE'], strict_slashes=False
)
def session_auth_logout() -> str:
    """
    Handles user logout by destroying the session using the session cookie.
    Returns an empty JSON response and clears the session cookie.
    """
    if not auth.destroy_session(request):
        abort(404)

    response = jsonify({})
    cookie_name = os.getenv("SESSION_NAME")
    if cookie_name:
        response.set_cookie(cookie_name, "", expires=0)

    return response
