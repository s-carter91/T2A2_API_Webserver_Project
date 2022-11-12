from flask import Blueprint, request
from flask_jwt_extended import jwt_required
from init import db
from controllers.auth_controller import auth_admin
from models.teamboards_champions_traits_items import Item, ItemSchema, Champion, ChampionSchema 



items_bp = Blueprint('items', __name__, url_prefix='/items/')

@items_bp.route('/')
# View all items in the database
def get_items():
    stmt = db.select(Item)
    items = db.session.scalars(stmt)
    return ItemSchema(many=True).dump(items)

@items_bp.route('/<string:name>/')
# View a specific items in the database
def get_single_item(name):
    stmt = db.select(Item).filter_by(name=name)
    item = db.session.scalar(stmt)
    if item:
        return ItemSchema(many=False).dump(item)
    else:
        return{'message': f'{name} is not an item'}, 404


@items_bp.route('/addsuggitem/', methods=['POST'])
@jwt_required()
# Allows an admin to create a relationship between an item and a champion (many-to-many). Adds a record to the association table. Champion suggested items
def add_sugg_item():
    auth_admin()
    stmt = db.select(Champion).filter_by(name=request.json['champion_name'])
    champion = db.session.scalar(stmt)
    if champion:
        stmt = db.select(Item).filter_by(name=request.json["item_name"])
        item = db.session.scalar(stmt)
        if item:
            item.champions.append(champion)
            db.session.commit()
            return{'message' : f'{champion.name} now has {item.name} as a suggested item'}, 201
        else:
            return{'error': 'Champion was not found.'}, 404
    else:
        return{'error': 'Item not found.'}, 404

@items_bp.route('/removesuggitem/', methods=['DELETE'])
@jwt_required()
# Allows an admin to delete a relationship between an item and a champion (many-to-many). Removes a record from the association table
def remove_sugg_item():
    auth_admin()
    try:
        stmt = db.select(Champion).filter_by(name=request.json['champion_name'])
        champion = db.session.scalar(stmt)
        if champion:
            stmt = db.select(Item).filter_by(name=request.json["item_name"])
            item = db.session.scalar(stmt)
            if item:
                item.champions.remove(champion)
                db.session.commit()
                return{'message' : f'{champion.name} no longer has {item.name} as a suggested item'}
            else:
                return{'error': 'Item not found.'}, 404
        else:
            return{'error': 'Champion was not found.'}, 404
    except ValueError:
        return{'error': f'That item was not in {champion.name}\'s suggested item list'}, 404