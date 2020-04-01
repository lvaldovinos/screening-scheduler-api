from app.tables.calendar import create_calendars_table_definition

TABLE_NAMES = {
    'CALENDAR': 'CALENDAR'
}

class ConnectionSingleton:
    __connection = None
    @staticmethod
    def initialize(engine=None):
        if ConnectionSingleton.__connection is None:
            ConnectionSingleton.__connection = Connection(engine)
        return ConnectionSingleton.__connection
    @staticmethod
    def get_instance():
        return ConnectionSingleton.__connection

class Connection:
    def __init__(self, engine=None):
        self.__engine = engine
        self.__tables = {}
    def initialize_tables_dict(self, metadata=None):
        # initialize all tables
        self.__tables[TABLE_NAMES['CALENDAR']] = create_calendars_table_definition(metadata)
    def get_table(self, table_name=None):
        return self.__tables[table_name]
    def connect(self, **params):
        return self.__engine.connect(**params)
    def execute(self, statement, *multiparams, **params):
        return self.__engine.execute(statement, *multiparams, **params) 
    def begin(self):
        return self.__engine.begin()
