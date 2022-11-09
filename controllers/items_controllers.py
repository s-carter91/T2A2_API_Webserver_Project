from flask import Blueprint
from init import db
from models.items import Item, ItemSchema

items_bp = Blueprint('items', __name__, url_prefix='/items/')

@items_bp.route('/')
def get_champs():
    stmt = db.select(Item)
    items = db.session.scalars(stmt)
    return ItemSchema(many=True).dump(items)