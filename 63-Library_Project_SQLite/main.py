from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

all_books = []


@app.route('/')
def home():
    return render_template("index.html", books=all_books)


@app.route("/add", methods=["GET", "POST"])
def add():
    # if the request method is POST, fetch the input from the form as a dictionary and append into the all_books list
    if request.method == "POST":
        new_book = {
            "title": request.form["title"],
            "author": request.form["author"],
            "rating": request.form["rating"]
        }

        all_books.append(new_book)

        return redirect(url_for('home')) # redirects back to the home page after the form is submitted
    return render_template("add.html")


if __name__ == "__main__":
    app.run(debug=True)

