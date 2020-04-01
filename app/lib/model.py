from app.lib.table import Table
from app.exceptions.unknown import UnknownError
import sqlalchemy

class Model:
    def __init__(self, connection=None, table=None):
        self.__table = table
        self.__connection = connection
    def insert(self, data):
        try:
            with self.__connection.connect() as connection:
                insert_stmt = self.__table.create_insert_stmt(**data)
                result = connection.execute(insert_stmt)
                return result.inserted_primary_key[0]
        except sqlalchemy.exc.OperationalError as error:
            print('Error: ', error)
            raise UnknownError(message='Error with DB connection')
    @staticmethod
    def create(connection=None, table_name=None):
        return Model(connection=connection, table=Table(connection.get_table(table_name)))
    @staticmethod
    def get_all(connection=None, table_name=None):
        try:
            table = Table(connection.get_table(table_name))
            with connection.connect() as connection:
                return connection.execute(table.create_select_all_stmt())
        except sqlalchemy.exc.OperationalError as error:
            print('Error: ', error)
            raise UnknownError(message='Error with DB connection')
