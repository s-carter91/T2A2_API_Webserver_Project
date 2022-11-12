from flask import Blueprint, request
from init import db
from models.teamboards_champions import Teamboard, TeamboardSchema, Champion
from flask_jwt_extended import jwt_required, get_jwt_identity

teamboards_bp = Blueprint('teamboards', __name__, url_prefix='/teamboards/')

@teamboards_bp.route('/')
@jwt_required()
# View all teamboards for signed in user
def get_user_teamboards():
    user_id = get_jwt_identity()
    stmt = db.select(Teamboard).filter_by(user_id = user_id)
    # stmt = db.select(Teamboard).options(db.lazyload(Teamboard.champions)).subqueryload(Champion.traits).filter_by(user_id = user_id)
    teamboards = db.session.scalars(stmt)
    return TeamboardSchema(many=True).dump(teamboards)
    # x = TeamboardSchema(many=True).dump(teamboards)
    # return x.count('Tempest')


# @teamboards_bp.route('/<id:integer>/')
# @jwt_required()
# # View all teamboards for signed in user
# def get_user_teamboard(id):
#     user_id = get_jwt_identity()
#     stmt = db.select(Teamboard).filter_by(teamboard_id = id, user_id = user_id)
#     teamboards = db.session.scalar(stmt)
#     if teamboards:
#         return TeamboardSchema(many=False).dump(teamboards)
#     # x = teamboards.count("Tempest")
#     else:
#         return "That teamboard does not exist."
    
    # return x

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

@teamboards_bp.route('/full_info')
# @jwt_required()
# View all teamboards for signed in user
def get_user_teamboard():
    # do a try except rule here to check this teamboard belongs to the signed in user
    # user_id = get_jwt_identity()
    stmt = db.select(Teamboard).options(db.lazyload(Teamboard.champions))
    # .subqueryload(Champion.subelements))
    teamboard = db.session.scalar(stmt)
    return TeamboardSchema().dump(teamboard)


@teamboards_bp.route('/addchamp/', methods=['POST'])
@jwt_required()
def add_champ():
    stmt = db.select(Teamboard).filter_by(id=request.json['teamboard_id'])
    teamboard = db.session.scalar(stmt)
    if teamboard:
        stmt = db.select(Champion).filter_by(name=request.json['champion_name'])
        champion = db.session.scalar(stmt)
        if champion:
            # teamboard = Teamboard(
            #     status = request.json['status'],
            #     start_date = request.json['start_date'],
            #     end_date = request.json['end_date'],
            #     units_hours = request.json['units_hours'],
            #     description = request.json['description'],
            # )

            teamboard.champions.append(champion)
            db.session.commit()
            return{'error' : f'{"champion_name"} has been added to {["teamboard_id"]}'}, 201
        else:
            return{'error': f'{"champion_name"} not found.'}, 404
    else:
        return{'error': f'{["teamboard_id"]} not found. Please enter an existed Teamboard ID.'}, 404

# @teamboards_bp.route('/addchamp/', methods=['POST'])
# def add_champ():
#     tb_id = request.json['tb_id']
#     champ_name = request.json['champ_name']
#     stmt = db.insert('teamboard_champions').values(teamboard_id=tb_id, champion_name=champ_name)
#     db.session.add(stmt)
#     db.session.commit()


# @teamboards_bp.route('/<int:id>/<string:name>/', methods=['POST'])
# @jwt_required()
# def update_one_card(id, name):
#     stmt = db.select(Teamboard).filter_by(id=id)
#     teamboard = db.session.scalar(stmt)
#     if teamboard:
#         user_id = get_jwt_identity()
#         if teamboard.user_id == user_id:
#             teamboard.champions.append(name)
#             db.session.commit()
#             return TeamboardSchema().dump(teamboard)
#         else:
#             return {'error' : 'You do not have access to view Teamboard with id {id}'}, 401
#     else:
#         return {'error' : 'Teamboard not fund with id {id}'}, 404

# @route('/teamboards_champions', methods=['POST'])
# @jwt_required()
# def create_teamboard_champions_join():
#     data = association_table().load(request.json)

#     teamboard = (
#         id1 = data['title'],
#         id2 = data['description'],
#         user_username = get_jwt_identity()
#     )

