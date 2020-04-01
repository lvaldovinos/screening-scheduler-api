import os
from app.lib.connection import ConnectionSingleton
from config import config
from sqlalchemy import create_engine, MetaData
from app.tables.calendar import create_calendars_table_definition

env = os.getenv('FLASK_ENV') or 'default'
config = config[env]
engine = create_engine(config.SQLALCHEMY_DB_URI)
metadata = MetaData()
ConnectionSingleton.initialize(engine, metadata)
# define all tables
calendars = create_calendars_table_definition()

metadata.create_all(engine)
