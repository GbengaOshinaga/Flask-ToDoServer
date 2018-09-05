from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_restplus import Api

from server import api_blueprint
from config import app_config

db = SQLAlchemy()

api = Api(api_blueprint, doc=False)

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.register_blueprint(api_blueprint)
    db.init_app(app)

    migrate = Migrate(app, db)

    from server.models import User, Todo
    from server.views import TodoResource

    return app
