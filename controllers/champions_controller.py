from flask import Blueprint, request, abort
from init import db
from models.teamboards_champions import Champion, ChampionSchema
from models.origins import Origin
# from models.champions import Champion, ChampionSchema

champions_bp = Blueprint('champions', __name__, url_prefix='/champions/')




@champions_bp.route('/')
# def get_champions():
#     stmt = db.select(Champion).order_by('cost')
#     champions = db.session.scalars(stmt)
#     return ChampionSchema(many=True).dump(champions)

def get_champs():
    # do a try except rule here to check this teamboard belongs to the signed in user
    # user_id = get_jwt_identity()
    stmt = db.select(Champion).options(db.lazyload(Champion.traits))
    # .subqueryload(Champion.subelements))
    champion = db.session.scalars(stmt)
    return ChampionSchema(many=True).dump(champion)

@champions_bp.route('/<string:name>/')
def get_single_champion(name):
    stmt = db.select(Champion).filter_by(name=name)
    champion = db.session.scalar(stmt)
    if champion:
        return ChampionSchema(many=False).dump(champion)
    else:
        return "champion doesn't exist"



