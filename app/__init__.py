from flask import Flask
from config import config_options
from flask_sqlalchemy import SQLAlchemy


def create_app(config_name):

    app = Flask(__name__)
    
    db = SQLAlchemy()
    # Creating the app configurations
    app.config.from_object(config_options[config_name])
    # config_options[config_name].init_app(app)


    #Initializing the applications
    db.init_app(app)
    
    # Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)


    return app