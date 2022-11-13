from flask import Blueprint
from init import db
from models.teamboards_champions_traits_items import Trait, TraitSchema

traits_bp = Blueprint('traits', __name__, url_prefix='/traits/')

@traits_bp.route('/')
# View all traits in the database
def get_traits():
    stmt = db.select(Trait)
    traits = db.session.scalars(stmt)
    return TraitSchema(many=True).dump(traits)

@traits_bp.route('/<string:name>/')
# View a specific trait in the database
def get_single_trait(name):
    stmt = db.select(Trait).filter_by(name=name)
    trait = db.session.scalar(stmt)
    if trait:
        return TraitSchema(many=False).dump(trait)
    else:
        return{'message': f'{name} is not a trait'}, 404 