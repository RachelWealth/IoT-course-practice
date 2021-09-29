from flask import Flask, render_template
from models.book import Book
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def book_list():
    book = Book('Python Flask',59.00,'段应该努力','富婆出版社')
    return render_template('book_list.html',book=book)


if __name__ == '__main__':
    app.run(debug=True)
