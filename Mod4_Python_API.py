########################################################
#
#  WRITTEN BY -    D.Bhattacharya
#
#  FILENAME    -    Mod4_Python_API
#
#  DATE -           02/05/2025
#
########################################################

from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage (replace with database in a real-world application)
books = []

# Book Model (simplified)
class Book:
    def __init__(self, id, book_name, author, publisher):
        self.id = id
        self.book_name = book_name
        self.author = author
        self.publisher = publisher

    def to_dict(self):
        return {
            "id": self.id,
            "book_name": self.book_name,
            "author": self.author,
            "publisher": self.publisher
        }
    # Create a new book
@app.route("/books", methods=["POST"])
def create_book():
    data = request.get_json()
    new_book = Book(len(books) + 1, data["book_name"], data["author"], data["publisher"])
    books.append(new_book)
    return jsonify(new_book.to_dict()), 201


# Get all books
@app.route("/books", methods=["GET"])
def get_books():
    return jsonify([book.to_dict() for book in books])


# Get a book by ID
@app.route("/books/<int:id>", methods=["GET"])
def get_book(id):
    for book in books:
        if book.id == id:
            return jsonify(book.to_dict())
    return jsonify({"message": "Book not found"}), 404


# Update a book
@app.route("/books/<int:id>", methods=["PUT"])
def update_book(id):
    data = request.get_json()
    for i, book in enumerate(books):
        if book.id == id:
            book.book_name = data["book_name"]
            book.author = data["author"]
            book.publisher = data["publisher"]
            return jsonify(book.to_dict())
    return jsonify({"message": "Book not found"}), 404


# Delete a book
@app.route("/books/<int:id>", methods=["DELETE"])
def delete_book(id):
    for i, book in enumerate(books):
        if book.id == id:
            del books[i]
            return jsonify({"message": "Book deleted"})
    return jsonify({"message": "Book not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)