from flask import Flask
from flask import jsonify
from flask import request
from flask import make_response
from flask import abort
from models import movies

app = Flask(__name__)


@app.route("/api/v1/m/movies/", methods=["GET"])
def movies_list_api_v1():
    return jsonify(movies.all())

@app.route("/api/v1/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    movie = movies.get(movie_id)
    if not movie:
        abort(404)
    return jsonify({"movie": movie})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found', 'status_code': 404}), 404)


@app.route("/api/v1/movies/", methods=["POST"])
def create_movie():
    if not request.json or not 'title' in request.json:
        abort(400)
    movie = {
        'id': movies.all()[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    movies.create(movie)
    return jsonify({'movie': movie}), 201

@app.route("/api/v1/movies/<int:movie_id>", methods=['DELETE'])
def delete_movie(movie_id):
    result = movies.delete(movie_id)
    if not result:
        abort(404)
    return jsonify({'result': result})



@app.route('/', methods=['GET'])
def home():
    return "<h1>witam</h1>"


if __name__ == "__main__":
    app.run(debug=True)