from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# create the extension
db = SQLAlchemy()

# create the app
app = Flask(__name__)

# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///the-books-collection.db"

# initialize the app with the extension
db.init_app(app)

# Define the models
class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False, unique=True)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)


# create the table
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add():
    # if the request method is POST, fetch the input from the form as a dictionary and append into the all_books list
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )

        db.session.add(new_book)
        db.session.commit()

        return redirect(url_for('home')) # redirects back to the home page after the form is submitted
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

