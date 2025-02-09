import json
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .login import login_blueprint

db=SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    with open('config.json') as cf:
        config_data = json.load(cf)

    app.config.update(config_data)
    app.logger.info(config_data)
    db.init_app(app)

    app.register_blueprint(login_blueprint)
    from .models import User, IdentityVerification, Post, PostInteraction, Like, Report, PostHistory, PostExpiry
    
    with app.app_context():
        db.create_all()


    return app



