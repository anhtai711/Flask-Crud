from app import ma
from app.models import Author, Book, Category

class CategorySchema(ma.Schema):
    class Meta:
        model = Category
        fields = ('id', 'name')
        
category_schema = CategorySchema()
categories_schema = CategorySchema(many=True)

class AuthorSchema(ma.Schema):
    class Meta:
        model = Author
        fields = ('id', 'name', 'about') # fields to expose

author_schema = AuthorSchema()
authors_schema = AuthorSchema(many=True)



class BookSchema(ma.Schema):
    class Meta:
        model = Book
        fields = ('id', 'name', 'tagline', 'short_desc', 'is_published', 'category_id', 'author_id') # fields to expose

book_schema = BookSchema()
books_schema = BookSchema(many=True)