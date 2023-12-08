from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)


parent_directory = os.getcwd()
db_path = parent_directory + '/tmdb_movie_100.db'
# Configure the SQLite database for Flask
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+ db_path  # Replace this with your full database path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Movie(db.Model):
    __tablename__ = 'movie'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    overview = db.Column(db.Text)
    release_date = db.Column(db.String(20))
    popularity = db.Column(db.Float)
    genres = db.Column(db.String(200))
    average_vote = db.Column(db.Float)
    runtime = db.Column(db.Integer)
    poster_path = db.Column(db.String(100))

# Route to handle the root endpoint
@app.route('/')
def home():
    return jsonify({"Home": "Welcome to Movie Search"})

# Route to get all movie titles
@app.route('/all_movie_titles')
def get_all_movie_titles():
    try:
        movies = Movie.query.all()
        movie_titles = [movie.title for movie in movies]
        return jsonify({'movie_titles': movie_titles})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Route to get movie information by title
@app.route('/get_movie_info/<movie_title>')  # Include movie_title parameter in the route
def get_movie_info(movie_title):
    if movie_title:
        movie = Movie.query.filter_by(title=movie_title).first()

        if movie:
            movie_info = {
                'title': movie.title,
                'overview': movie.overview,
                'release_date': movie.release_date,
                'popularity': movie.popularity,
                'genres': movie.genres,
                'average_vote': movie.average_vote,
                'runtime': movie.runtime,
                'poster_path': movie.poster_path
            }
            return jsonify(movie_info)
        else:
            return jsonify({'error': 'Movie not found!'}), 404
    else:
        return jsonify({'error': 'Invalid request!'}), 400

app.run()
