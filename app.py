from flask import Flask, jsonify, render_template, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

books = [
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee'},
    {'title': '1984', 'author': 'George Orwell'},
    {'title': 'The Catcher in the Rye', 'author': 'J.D Salinger'}
    ]

# Endpoint to return the list of books
@app.route('/api/books')
def get_books():
    return jsonify(books)

#Endpoint to add a new book
@app.route('/api/books', methods=['POST'])
def add_book():
    # Get the title and author from the request data
    title = request.json['title']
    author = request.json['author']

    # Generate a new ID for the book
    id = len(books) + 1

    #Create the new book object
    new_book = {'id': id, 'title': title, 'author': author}

    # Add the new book to the list of books
    books.append(new_book)

    # Return the new book object
    return jsonify(new_book)

# Endpoint to render the index.html template
@app.route('/')
def index():
    return render_template('index.html')
