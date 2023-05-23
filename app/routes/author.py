from flask import request, jsonify, make_response, Blueprint
from app.db import db
from app.models import Author
from app.schema import author_schema, authors_schema

author = Blueprint('author', __name__)

"""
===========================
endpoints for Author CRUD
===========================
"""

# endpoint to CREATE author
@author.route("/author", methods=["POST"])
def create_author():

    name = request.json['name']

    if 'about' in request.json:
        about = request.json['about']
    else:
        about = ""

    new_author = Author(name, about)

    db.session.add(new_author)
    db.session.commit()

    result = author_schema.dump(new_author)

    data = {
        'message': 'New Author Created!',
        'status': 201,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET all authors
@author.route("/author", methods=["GET"])
def get_authors():

    all_author = Author.query.all()
    result = authors_schema.dump(all_author)

    data = {
        'message': 'All Authors!',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET author detail by id
@author.route("/author/<int:id>", methods=["GET"])
def get_author(id):

    author = Author.query.get(id)

    if(author):
        result = author_schema.dump(author)
        data = {
            'message': 'Author Info!',
            'status': 200,
            'data': result
        }
    else:
        data = {
            'message': 'Invalid Author ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to UPDATE author
@author.route("/author/<int:id>", methods=["PUT"])
def update_author(id):

    author = Author.query.get(id)

    if(author):
        if 'name' in request.json:
            author.name = request.json['name']
        if 'about' in request.json:
            author.about = request.json['about']

        db.session.commit()
        result = author_schema.dump(author)
        
        data = {
            'message': 'Author Info Edited!',
            'status': 200,
            'data': result
        }

    else:
        data = {
            'message': 'Invalid Author ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to DELETE author
@author.route("/author/<int:id>", methods=["DELETE"])
def delete_author(id):

    author = Author.query.get(id)

    if(author):
        db.session.delete(author)
        db.session.commit()

        data = {
            'message': 'Author Deleted!',
            'status': 200
        }
    else:
        data = {
            'message': 'Invalid Author ID!',
            'status': 200
        }
    return make_response(jsonify(data))