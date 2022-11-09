from flask import Blueprint, request, abort
from init import db
from models.champions import Champion, ChampionSchema

champions_bp = Blueprint('champions', __name__, url_prefix='/champions/')

@champions_bp.route('/')
def get_champions():
    stmt = db.select(Champion).order_by('cost')
    champions = db.session.scalars(stmt)
    return ChampionSchema(many=True).dump(champions)


