from app.exceptions.unknown import UnknownError
from app.routes.calendar import calendar_routes_init
from flask import jsonify, request, make_response, g

def init_routes(app):
    calendar_routes_init(app)

    @app.errorhandler(UnknownError)
    def handle_unknown(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
