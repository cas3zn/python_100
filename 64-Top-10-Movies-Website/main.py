from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests
import os

# create the extension
db = SQLAlchemy()

# create the app
app = Flask(__name__)
Bootstrap5(app)

# configuring extension to the Flask app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///a-100-movies-to-watch.db"

# initialize the app with the extension
db.init_app(app)

# CSRF protection
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

# TMDB API Key
API_KEY = "d97bf4e53abaff7bb01620ac001cb870"
API_READ_ACCESS_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJkOTdiZjRlNTNhYmFmZjdiYjAxNjIwYWMwMDFjYjg3MCIsInN1YiI6IjY1NWQwNmMxZmQ0YTk2MDEwMGRmZjA3ZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.erv6C_I64uY1I9yqz9QAqNwj0_qj4EdInQJHRMrhQZU"

url = "https://api.themoviedb.org/3/search/movie?include_adult=false&language=en-US&page=1"
headers = {
    "accept": "application/json",
    "Authorization": f"Bearer {API_READ_ACCESS_TOKEN}"
}

# define the models
class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)
    ranking = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

# create the table
with app.app_context():
    db.create_all()
    
# create the necessary forms using Flask
class RateMovieForm(FlaskForm):
    rating = StringField("Your Rating Out of 10 e.g. 7.5")
    review = StringField("Your Review")
    submit = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submit = SubmitField("Add Movie")

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars()

    return render_template("index.html", movies=all_movies)

# Updating the movie rating and review
@app.route("/edit", methods=["GET", "POST"])
def rate_movie():
    form = RateMovieForm()
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)
    if form.validate_on_submit():
        movie.rating = float(form.rating.data)
        movie.review = form.review.data
        db.session.commit()
        return redirect(url_for('home'))
    
    return render_template("edit.html", movie=movie, form=form)


# Delete the movie
@app.route("/delete")
def delete_movie():
    movie_id = request.args.get("id")
    movie = db.get_or_404(Movie, movie_id)

    db.session.delete(movie)
    db.session.commit()

    return redirect(url_for('home'))


# Adding a movie
@app.route("/add", methods=["GET", "POST"])
def add_movie():
    form = AddMovieForm()

    if form.validate_on_submit():
        movie_title = form.title.data
        response = requests.get(url, headers=headers, params={"query": movie_title})
        movie_results = response.json()["results"]

        return render_template("select.html", options=movie_results)

    return render_template("add.html", form=form)

if __name__ == '__main__':
    app.run(debug=True)
