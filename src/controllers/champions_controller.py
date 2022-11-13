from flask import Blueprint
from init import db
from models.teamboards_champions_traits_items import Champion, ChampionSchema

champions_bp = Blueprint('champions', __name__, url_prefix='/champions/')

@champions_bp.route('/')
# View all champions in the database
def get_champions():
    stmt = db.select(Champion).order_by('cost', 'name')
    champions = db.session.scalars(stmt)
    return ChampionSchema(many=True).dump(champions)

@champions_bp.route('/<string:name>/')
# View a specific champion in the database
def get_single_champion(name):
    stmt = db.select(Champion).filter_by(name=name)
    champion = db.session.scalar(stmt)
    if champion:
        return ChampionSchema(many=False).dump(champion)
    else:
        return {'message' : f'{name} is not a champion'}, 404
