from flask import Blueprint, request
from init import db
from models.teamboards import Teamboard, TeamboardSchema
from flask_jwt_extended import jwt_required, get_jwt_identity

teamboards_bp = Blueprint('teamboards', __name__, url_prefix='/teamboards/')

@teamboards_bp.route('/')
# View all teamboards for signed in user
def get_user_teamboards():
    user_id = get_jwt_identity
    stmt = db.select(Teamboard).filter_by(user_username = user_id)
    teamboards = db.session.scalars(stmt)
    return TeamboardSchema(many=True).dump(teamboards)

@teamboards_bp.route('/', methods=['POST'])
@jwt_required
# Create a new Teamboard
def create_teamboard():
    data = TeamboardSchema().load(request.json)

    teamboard = Teamboard(
        title = data['title'],
        description = data['description'],
        user_username = get_jwt_identity()
    )

    db.session.add(teamboard)
    db.session.commit()
