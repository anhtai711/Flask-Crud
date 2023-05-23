from flask import request, jsonify, make_response, Blueprint
from app.db import db
from app.models import Book
from app.schema import book_schema, books_schema

book = Blueprint('book', __name__)

"""
===========================
endpoints for Book CRUD
===========================
"""

# endpoint to CREATE book
@book.route("/book", methods=["POST"])
def create_book():

    name = request.json['name']
    tagline = request.json['tagline']
    category_id = request.json['category_id']
    author_id = request.json['author_id']

    if 'short_desc' in request.json:
        short_desc = request.json['short_desc']
    else:
        short_desc = ""

    new_book = Book(name, tagline, short_desc, category_id, author_id)

    db.session.add(new_book)
    db.session.commit()

    result = book_schema.dump(new_book)

    data = {
        'message': 'New Book Created!',
        'status': 201,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET all books
@book.route("/book", methods=["GET"])
def get_books():

    all_book = Book.query.all()
    result = books_schema.dump(all_book)

    data = {
        'message': 'All Books!',
        'status': 200,
        'data': result
    }
    return make_response(jsonify(data))



# endpoint to GET book detail by uuid
@book.route("/book/<path:uuid>", methods=["GET"])
def get_book(uuid):

    book = Book.query.get(uuid)

    if(book):
        result = book_schema.dump(book)
        data = {
            'message': 'Book Info!',
            'status': 200,
            'data': result
        }
    else:
        data = {
            'message': 'Invalid Book ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to UPDATE book
@book.route("/book/<path:uuid>", methods=["PUT"])
def update_book(uuid):

    book = Book.query.get(uuid)

    if(book):
        if 'name' in request.json:
            book.name = request.json['name']
        if 'short_desc' in request.json:
            book.short_desc = request.json['short_desc']
        if 'tagline' in request.json:
            book.tagline = request.json['tagline']
        if 'is_published' in request.json:
            book.is_published = request.json['is_published']
        if 'category_id' in request.json:
            book.category_id = request.json['category_id']
        if 'author_id' in request.json:
            book.author_id = request.json['author_id']

        db.session.commit()
        result = book_schema.dump(book)
        
        data = {
            'message': 'Book Info Edited!',
            'status': 200,
            'data': result
        }

    else:
        data = {
            'message': 'Invalid Book ID!',
            'status': 200
        }
    return make_response(jsonify(data))



# endpoint to DELETE author
@book.route("/book/<path:uuid>", methods=["DELETE"])
def delete_book(uuid):

    book = Book.query.get(uuid)

    if(book):
        db.session.delete(book)
        db.session.commit()

        data = {
            'message': 'Book Deleted!',
            'status': 200
        }
    else:
        data = {
            'message': 'Invalid Book ID!',
            'status': 200
        }
    return make_response(jsonify(data))