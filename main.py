from flask import Flask
from init import db, ma, bcrypt, jwt
from controllers.auth_controller import auth_bp
from controllers.cli_commands import db_commands
from controllers.items_controllers import items_bp
from controllers.champions_controller import champions_bp
from controllers.teamboards_controller import teamboards_bp
from controllers.traits_controller import traits_bp
from controllers.origins_controller import origins_bp
from marshmallow.exceptions import ValidationError
import os

def create_app():
    
    app = Flask(__name__)

    @app.errorhandler(KeyError)
    def key_error(err):
        return {'error': f'The field {err} is required'}, 400
    
    @app.errorhandler(401)
    def unauth_error(err):
        return {'error': str(err)}, 404

    app.config['JSON_SORT_KEYS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
    app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY')

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(champions_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(db_commands)
    app.register_blueprint(teamboards_bp)
    app.register_blueprint(items_bp)
    app.register_blueprint(traits_bp)
    app.register_blueprint(origins_bp)

    return app