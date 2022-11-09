from flask import Blueprint, request, abort
from init import db, jwt, bcrypt
from models.users import User, UserSchema
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import jwt_required, get_jwt_identity

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def auth_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)

@auth_bp.route('/users/', methods=['GET'])
@jwt_required()
def display_users():
    # auth_admin()
    pass
    

@auth_bp.route('/users/<int:id>/', methods=['DELETE'])
@jwt_required()
def delete_user():
    # auth_admin()
    pass

@auth_bp.route('/register/', methods = ['POST'])
def user_register():
    try:
        user = User(
            username = request.json['username'],
            email = request.json['email'],
            password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8'),
        )

        db.session.add(user)
        db.session.commit()
        return UserSchema(exclude=['password']).dump(user), 201
    except IntegrityError:
        return {'error': 'Username already in use'}, 409

@auth_bp.route('/register/admin/', methods = ['POST'])
@jwt_required()
def admin_register():
    # auth_admin()
    pass

@auth_bp.route('/login/')
def login():
    pass

