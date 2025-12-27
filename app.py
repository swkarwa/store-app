import os
import secrets

from flask import Flask
from flask_smorest import Api
from flask_jwt_extended import JWTManager

from db import db
from flask_migrate import Migrate
import models
from resources.store import blp as store_blue_print
from resources.item import blp as item_blue_print
from resources.tag import blp as tag_blue_print
from resources.user import blp as user_blue_print


def create_app(db_url=None):
    app = Flask(__name__)

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Stores REST API"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/api"
    app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger"
    app.config["OPENAPI_SWAGGER_UI_URL"] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv('DB_URL', 'sqlite:///db.sqlite3')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    
    # JWT secret key - must be set via environment variable
    jwt_secret = os.getenv('JWT_SECRET_KEY')
    if not jwt_secret:
        raise RuntimeError("JWT_SECRET_KEY environment variable is required")

    app.config['JWT_SECRET_KEY'] = jwt_secret
    jwt = JWTManager(app)
    db.init_app(app)
    migrate = Migrate(app , db)
    api = Api(app)

    with app.app_context():
        db.create_all()

    api.register_blueprint(store_blue_print)
    api.register_blueprint(item_blue_print)
    api.register_blueprint(tag_blue_print)
    api.register_blueprint(user_blue_print)
    
    return app

if __name__=='__main__':
    app = create_app()
    app.run(
        host = '0.0.0.0',
        port = 5000,
        debug=True
    )


