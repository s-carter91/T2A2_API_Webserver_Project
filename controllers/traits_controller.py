from flask import Blueprint, request
from init import db
from models.teamboards_champions import Trait, TraitSchema

traits_bp = Blueprint('traits', __name__, url_prefix='/traits/')

@traits_bp.route('/')
def get_traits():
    stmt = db.select(Trait)
    traits = db.session.scalars(stmt)
    return TraitSchema(many=True).dump(traits)