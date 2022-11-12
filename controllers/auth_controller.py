from flask import Blueprint, request, abort
from datetime import timedelta
from init import db, jwt, bcrypt
from models.users import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def auth_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(username=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)

@auth_bp.route('/login/', methods=['POST'])
def login():
    stmt = db.select(User).filter_by(username=request.json['username'])
    user = db.session.scalar(stmt)
    # checking the username exists and then password against the username
    if user and bcrypt.check_password_hash(user.password, request.json['password']):
        token = create_access_token(identity=str(user.username), expires_delta=timedelta(days=2))
        return {'username': user.username, 'token': token, 'is_admin': user.is_admin}
    else:
        return {'error': 'Invalid username or password'}, 401

@auth_bp.route('/users/', methods=['GET'])
@jwt_required()
def display_users():
    auth_admin()
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many = True, exclude=['password']).dump(users)

@auth_bp.route('/users/<string:username>/')
@jwt_required()
def get_single_user(username):
    auth_admin()

    stmt = db.select(User).filter_by(username=username)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': 'User cannot be found with username '+ (username)}, 404    

@auth_bp.route('/users/<string:username>/', methods=['DELETE'])
@jwt_required()
def delete_user(username):
    auth_admin()
    
    stmt = db.select(User).filter_by(username=username)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': 'User ' + (user.username) + ' has been successfully deleted'}
    else:
        return {'error': 'User cannot be found with username ' + (username)}, 404
    

@auth_bp.route('/register/', methods = ['POST'])
def user_register():
    try:
        user = User(
            username = request.json['username'],
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
        )

        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Username or email already in use'}, 409

@auth_bp.route('/register/admin/', methods = ['POST'])
@jwt_required()
def admin_register():
    auth_admin()
    try:
        user = User(
            username = request.json['username'],
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
            is_admin = True
        )

        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Username or email already in use'}, 409



