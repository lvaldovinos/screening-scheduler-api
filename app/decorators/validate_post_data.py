from flask import request, jsonify, make_response, g
from functools import wraps
from app.lib.validator import Validator

def validate_post_data(schema=None):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            validator = Validator(schema)
            data = request.get_json()
            validator.validate(data)
            if validator.isvalid == False:
                response_body = { 'message': 'Invalid payload' }
                return make_response(jsonify(response_body), 400)
            g.validated_data = data
            return f(*args, **kwargs)
        return wrapper
    return decorator
