from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from init import db
from models.teamboards_champions_traits_items import Teamboard, TeamboardSchema, Champion


teamboards_bp = Blueprint('teamboards', __name__, url_prefix='/teamboards/')

@teamboards_bp.route('/')
@jwt_required()
# View all teamboards for the signed in user
def get_user_teamboards():
    user_id = get_jwt_identity()
    stmt = db.select(Teamboard).filter_by(user_id = user_id)
    teamboards = db.session.scalars(stmt)
    return TeamboardSchema(many=True).dump(teamboards)

@teamboards_bp.route('/<int:id>')
@jwt_required()
# View a specific teamboards for the signed in user
def get_one_teamboard(id):
    user_id = get_jwt_identity()
    stmt = db.select(Teamboard).filter_by(id = id, user_id = user_id)
    teamboard = db.session.scalar(stmt)
    if teamboard:
        return TeamboardSchema().dump(teamboard)
    else:
        return {'error' : f'Teamboard not found with id {id}.'}, 404

@teamboards_bp.route('/', methods=['POST'])
@jwt_required()
# Create a new Teamboard
def create_teamboard():
    data = TeamboardSchema().load(request.json)

    teamboard = Teamboard(
        title = data['title'],
        description = data['description'],
        user_id = get_jwt_identity()
    )
    db.session.add(teamboard)
    db.session.commit()
    return TeamboardSchema().dump(teamboard)

@teamboards_bp.route('/update/<int:id>/', methods=['PUT', 'PATCH'])
@jwt_required()
# Update a users Teamboard
def update_one_card(id):
    user_id = get_jwt_identity()
    stmt = db.select(Teamboard).filter_by(id=id, user_id = user_id)
    teamboard = db.session.scalar(stmt)
    if teamboard:
        teamboard.title = request.json.get('title') or teamboard.title
        teamboard.description = request.json.get('description') or teamboard.description
        db.session.commit()
        return TeamboardSchema().dump(teamboard)
    else:
        return {'error' : f'Teamboard not found with id {id}'}, 404

@teamboards_bp.route('/addchamp/', methods=['POST'])
@jwt_required()
# Create a relationship between a users teamboard and a champion (many-to-many). Adds a record to the association table
def add_champ_board():
    user_id = get_jwt_identity()
    stmt = db.select(Teamboard).filter_by(id=request.json['teamboard_id'], user_id=user_id)
    teamboard = db.session.scalar(stmt)
    if teamboard:
        stmt = db.select(Champion).filter_by(name=request.json["champion_name"])
        champion = db.session.scalar(stmt)
        if champion:
            teamboard.champions.append(champion)
            db.session.commit()
            return{'message' : f'{champion.name} has been added to Teamboard {teamboard.title} ID {teamboard.id}'}, 201
        else:
            return{'error': 'Champion was not found.'}, 404
    else:
        return{'error': 'Teamboard ID not found. Please enter an existing Teamboard ID.'}, 404

@teamboards_bp.route('/removechamp/', methods=['DELETE'])
@jwt_required()
# Delete a relationship between a users teamboard and a champion (many-to-many). Removes a record from the association table
def remove_champ_board():
    try:
        user_id = get_jwt_identity()
        stmt = db.select(Teamboard).filter_by(id=request.json['teamboard_id'], user_id=user_id)
        teamboard = db.session.scalar(stmt)
        if teamboard:
            stmt = db.select(Champion).filter_by(name=request.json["champion_name"])
            champion = db.session.scalar(stmt)
            if champion:
                teamboard.champions.remove(champion)
                db.session.commit()
                return{'message' : f'{champion.name} is not longer in {teamboard.title} ID {teamboard.id}'}, 201
            else:
                return{'error': 'Champion not found.'}, 404
        else:
            return{'error': 'Teamboard ID was not found.Please enter an existing Teamboard ID.'}, 404
    except ValueError:
        return{'error': f'That champion was not in {teamboard.title}\'s suggested item list'}, 404
