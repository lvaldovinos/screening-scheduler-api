from app.lib.model import Model
from app.lib.connection import ConnectionSingleton, TABLE_NAMES
from app.lib.table import Table

class CalendarModel:
    def __init__(self, data=None):
        self.__model = Model.create(
                connection=ConnectionSingleton.get_instance(), 
                table_name=TABLE_NAMES['CALENDAR']
                )
        self.__data = data
    def insert(self):
        return self.__model.insert(self.__data)
    @staticmethod
    def get_all():
        rows = Model.get_all(
            connection=ConnectionSingleton.get_instance(), 
            table_name=TABLE_NAMES['CALENDAR']
            )
        calendars = []
        for row in rows:
            calendars.append(dict(row))
        return calendars
