from flask import request, jsonify, make_response, Blueprint
from app.db import db
from app.models import Category
from app.schema import category_schema, categories_schema

category = Blueprint('category', __name__)

"""
===========================
endpoints for Category CRUD
===========================
"""

# endpoint to CREATE category
@category.route("/category", methods=["POST"])
def create_category():
    name = request.json['name']
    new_category = Category(name)
    db.session.add(new_category)
    db.session.commit()

    result = category_schema.dump(new_category)

    data = {
        'message': 'New Category Created!',
        'status': 201,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET all categories
@category.route("/category", methods=["GET"])
def get_categories():

    all_categories = Category.query.all()
    result = categories_schema.dump(all_categories)

    data = {
        'message': 'All Categories!',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET category detail by id
@category.route("/category/<int:id>", methods=["GET"])
def get_category(id):

    category = Category.query.get(id)

    if(category):
        result = category_schema.dump(category)
        data = {
            'message': 'Category Info!',
            'status': 200,
            'data': result
        }
    else:
        data = {
            'message': 'Invalid Category ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to UPDATE category
@category.route("/category/<int:id>", methods=["PUT"])
def update_category(id):

    category = Category.query.get(id)

    if(category):
        if 'name' in request.json:
            category.name = request.json['name']

        db.session.commit()
        result = category_schema.dump(category)
        
        data = {
            'message': 'Category Info Edited!',
            'status': 200,
            'data': result
        }

    else:
        data = {
            'message': 'Invalid Category ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to DELETE category
@category.route("/category/<int:id>", methods=["DELETE"])
def delete_category(id):

    category = Category.query.get(id)

    if(category):
        db.session.delete(category)
        db.session.commit()

        data = {
            'message': 'Category Deleted!',
            'status': 200
        }
    else:
        data = {
            'message': 'Invalid Category ID!',
            'status': 200
        }
    return make_response(jsonify(data))