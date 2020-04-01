from flask import Flask
from config import config

def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)

    return app
