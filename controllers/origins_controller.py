from flask import Blueprint
from init import db
from models.origins import Origin, OriginSchema

origins_bp = Blueprint('origins', __name__, url_prefix='/origins/')

@origins_bp.route('/')
# View all origins in the database
def get_origins():
    stmt = db.select(Origin)
    items = db.session.scalars(stmt)
    return OriginSchema(many=True).dump(items)

@origins_bp.route('/<string:name>/')
# View a specific origin in the database
def get_single_origin(name):
    stmt = db.select(Origin).filter_by(name=name)
    origin = db.session.scalar(stmt)
    if origin:
        return OriginSchema(many=False).dump(origin)
    else:
        return{'message': f'{name} is not an origin'}, 404 