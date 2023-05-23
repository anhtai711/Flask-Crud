from app.db import db
from sqlalchemy_utils import ChoiceType

import enum

class BookIsPublishedEnum(enum.Enum):
    yes=True
    no=False
    
class Book(db.Model):
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    tagline =db.Column(db.String(255))
    short_desc =db.Column(db.Text())
    is_published = db.Column(
        db.Boolean(),
        ChoiceType(BookIsPublishedEnum),
        default=False
    )
    
    category_id = db.Column(db.Integer, db.ForeignKey("category.id"), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey("author.id"), nullable=False)
    
    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)

    def __init__(self, name, tagline, short_desc, category_id, author_id):
        self.name = name
        self.tagline = tagline
        self.short_desc = short_desc
        self.category_id = category_id
        self.author_id = author_id
        
class Category(db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    
    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    
    books = db.relationship(Book, backref='category', lazy=True)
    
    def __init__(self, name):
        self.name = name
        
class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    about = db.Column(db.Text())
    
    created = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)
    modified = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False)
    
    books = db.relationship(Book, backref='author', lazy=True)
    
    def __init__(self, name, about):
        self.name = name
        self.about = about