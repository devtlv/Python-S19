#!/usr/local/bin/python3
#
import flask, flask_login
from functools import wraps

def role_required(*roles):
    def decorator(function):
        @wraps(function)
        def protected_function(*args, **kwargs):
            user = flask_login.current_user

            if user.is_anonymous:
                return flask.abort(403)

            if user.role not in roles:
                return flask.abort(403)

            return function(*args, **kwargs)
        return protected_function
    return decorator

