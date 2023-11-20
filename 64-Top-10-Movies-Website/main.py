from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired
import requests

'''
Red underlines? Install the required packages first: 
Open the Terminal in PyCharm (bottom left). 

On Windows type:
python -m pip install -r requirements.txt

On MacOS type:
pip3 install -r requirements.txt

This will install the packages from requirements.txt for this project.
'''
# create the extension
db = SQLAlchemy()

# create the app
app = Flask(__name__)
Bootstrap5(app)

# configuring extension to the Flask app
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///a-100-movies-to-watch.db"

# initialize the app with the extension
db.init_app(app)

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

# create a new record
'''
second_movie = Movie(
    title="Avatar The Way of Water",
    year=2022,
    description="Set more than a decade after the events of the first film, learn the story of the Sully family (Jake, Neytiri, and their kids), the trouble that follows them, the lengths they go to keep each other safe, the battles they fight to stay alive, and the tragedies they endure.",
    rating=7.3,
    ranking=9,
    review="I liked the water.",
    img_url="https://image.tmdb.org/t/p/w500/t6HIqrRAclMCA60NsSmeqe9RmNV.jpg"
)


# add it to the database
with app.app_context():
    db.session.add(second_movie)
    db.session.commit()
'''
    

@app.route("/")
def home():
    result = db.session.execute(db.select(Movie))
    all_movies = result.scalars()

    return render_template("index.html", movies=all_movies)


if __name__ == '__main__':
    app.run(debug=True)
