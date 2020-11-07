import json

class Movies:
    def __init__(self):
        try:
            with open("movies.json", "r") as f:
                x = json.load(f)
                self.movies = sorted(x, key=lambda y: y['title'])
        except FileNotFoundError:
            self.movies = []

    def myFunc(e):
        return len(e)
            
    def all(self):
        return self.movies

    def get(self, id):
        return self.movies[id]

    def create(self, data):
        self.movies.append(data)
        self.save_all()

    def save_all(self):
        with open("movies.json", "w") as f:
            json.dump(self.movies, f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.movies[id] = data
        self.save_all()

    def delete(self, id):
            movie = self.get(id)
            if movie:
                self.movies.remove(movie)
                self.save_all()
                return True
            return False

movies = Movies()
