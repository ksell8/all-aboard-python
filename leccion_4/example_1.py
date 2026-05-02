from datetime import datetime
from typing import List

from pydantic import BaseModel

class Director(BaseModel):
    name: str

    def __str__(self):
        return self.name

class Movie(BaseModel):
    director: Director
    name: str

    def __str__(self):
        return self.name

class Collection(BaseModel):
    movies: List[Movie]

    def get_movies_of_director(self, director: Director) -> List[Movie]:
        to_return = []
        for movie in self.movies:
            if movie.director.name == director.name:
                to_return.append(movie)
        return to_return

    def __str__(self):
        to_return = ""
        for movie in self.movies:
            to_return += f"{movie.name} - {movie.director.name}\n"
        return to_return

if __name__ == "__main__":
    kubrick = Director(name="Kubrick")
    clockwork = Movie(name="A Clockwork Orange", director=kubrick)
    odyssey = Movie(name="2001: A Space Odyssey", director=kubrick)
    strangelove = Movie(name="Dr. Strangelove: Or How I Learned to Stop Worrying and Love the Bomb", director=kubrick)

    cronenberg = Director(name="Cronenberg")
    fly = Movie(name="The Fly", director=cronenberg)
    brood = Movie(name="The Brood", director=cronenberg)
    existenz = Movie(name="Existenz", director=cronenberg)

    collection = Collection(movies=[clockwork, odyssey, strangelove, fly, brood, existenz])
    print(collection)
    print(f"kubrick: {collection.get_movies_of_director(director=kubrick)}")