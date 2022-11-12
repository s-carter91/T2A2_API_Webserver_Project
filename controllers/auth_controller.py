from flask import Blueprint, request, abort
from datetime import timedelta
from init import db, jwt, bcrypt
from models.users import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

# Function to authorise if active user is an admin
def auth_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(username=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)

@auth_bp.route('/register/', methods = ['POST'])
# Allows end user to register/create a login
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
# Allows an admin to register/create another admin account
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

@auth_bp.route('users/update/', methods=['PUT', 'PATCH'])
@jwt_required()
# Update a users Teamboard
def update_one_card():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(username=user_id)
    user = db.session.scalar(stmt)
    user.email = request.json.get('email') or user.email
    db.session.commit()
    return UserSchema(exclude=['password']).dump(user)



@auth_bp.route('/login/', methods=['POST'])
# Allows end user to login with their registered details
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
# Allows an admin to view all accounts
@jwt_required()
def display_users():
    auth_admin()
    stmt = db.select(User)
    users = db.session.scalars(stmt)
    return UserSchema(many = True, exclude=['password']).dump(users)

@auth_bp.route('/users/<string:username>/')
# Allows an admin to view a specific account
@jwt_required()
def get_single_user(username):
    auth_admin()
    stmt = db.select(User).filter_by(username=username)
    user = db.session.scalar(stmt)
    if user:
        return UserSchema(exclude=['password']).dump(user)
    else:
        return {'error': f'User cannot be found with username {username}'}, 404

@auth_bp.route('/users/<string:username>/', methods=['DELETE'])
# Allows an admin to delete a specific account
@jwt_required()
def delete_user(username):
    auth_admin()
    
    stmt = db.select(User).filter_by(username=username)
    user = db.session.scalar(stmt)
    if user:
        db.session.delete(user)
        db.session.commit()
        return {'message': f'User {username} has been successfully deleted'}
    else:
        return {'error': f'User cannot be found with username {username}'}, 404
    







