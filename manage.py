import os
from app.lib.connection import ConnectionSingleton
from app import create_app
from config import config
from sqlalchemy import create_engine, MetaData
from app.routes import init_routes

env = os.getenv('FLASK_ENV') or 'default'
config = config[env]
engine = create_engine(config.SQLALCHEMY_DB_URI)
con = ConnectionSingleton.initialize(engine)
con.initialize_tables_dict(MetaData())
app = create_app(config)
init_routes(app)

if __name__ == '__main__':
    app.run()
