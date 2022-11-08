from flask import Blueprint, request, abort

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

def auth_admin():
    user_id = get_jwt_identity()
    stmt = db.select(User).filter_by(id=user_id)
    user = db.session.scalar(stmt)
    if not user.is_admin:
        abort(401)

@auth_bp.route('/users/', methods=['GET'])
@jwt_required
def display_users():
    auth_admin()
    pass

@auth_bp.route('/register/', methods = ['POST'])
def user_register():
    pass

@auth_bp.route('/registeradmin/', methods = ['POST'])
@jwt_required
def admin_register():
    auth_admin()
    pass

@auth_bp.route('/login/')
def login():
