import sqlite3
import uuid
from flask import (
        Blueprint, g, flash, redirect, url_for, request, session, jsonify
        )
from . import db

bp = Blueprint('order', __name__)

# this route will list out all the orders
@bp.route('/list')
def list():
    DB = db.get_db()

    orders = DB.execute("""
SELECT 
    o.OrderID, 
    o.CustomerID, 
    o.Items, 
    o.CreatedAt, 
    o.ShippedAt, 
    o.CompletedAt,
    i.ItemID,
    i.Quantity,
    i.Price
FROM 
    `order` o
INNER JOIN 
    `item` i
ON 
    o.OrderID = i.OrderID;
""").fetchall()

    return jsonify(orders)

# this will create an order
@bp.route('/create', methods=["POST"])
def create():
    DB = db.get_db()
    data = request.get_json()

    # validate the required fields
    if not data or not all(k in data for k in ('OrderID', 'Items', 'CreatedAt')):
        return jsonify({'error': 'Invalid input'}), 400

    # we will create a uuid for CustomerID field
    uuid_customerID = str(uuid.uuid1())
    try:
        # insert the order into database
        DB.execute(
                'INSERT INTO `order` (OrderID, CustomerID, Items, CreatedAt, ShippedAt, CompletedAt) VALUES (?, ?, ?, ?, ?, ?)',
                (data['OrderID'], uuid_customerID, data['Items'], data['CreatedAt'], data.get('ShippedAt'), data.get('CompletedAt'))
                )
        DB.commit()
    except sqlite3.IntegrityError:
        return jsonify({'error': 'OrderID already exists'}), 400

    return jsonify({'message': 'Order created successfully'}), 201
