from app.decorators.validate_post_data import validate_post_data
from app.models.calendar import CalendarModel
from app.validators.calendar import Calendar

def calendar_routes_init(app):
    @app.route('/calendars', methods=['POST'])
    @validate_post_data(schema=Calendar())
    def create_calendars():
        calendarModel = CalendarModel(data=g.validated_data)
        result = calendarModel.insert()
        response = make_response()
        response.status_code = 201
        response.headers['Location'] = '/calendars/{}'.format(result)
        return response

    @app.route('/calendars', methods=['GET'])
    def get_calendars():
        calendars = CalendarModel.get_all()
        return jsonify(calendars)
