import csv
from backendflask.domain_models.movie import Movie
from backendflask.domain_models.genre import Genre
from backendflask.domain_models.director import Director
from backendflask.domain_models.actor import Actor
from backendflask.domain_models.rating import Rating
from backendflask.domain_models.review import Review


class MovieCSVParser:

    def __init__(self, file_name: str):
        self.__file_name = file_name
        self.__dataset_of_actors = []
        self.__dataset_of_directors = []
        self.__dataset_of_genres = []
        self.__dataset_of_movies = []
        self.__dataset_of_reviews = []
        self.__dataset_of_ratings = []

    def read_csv_file(self):
        with open(self.__file_name, mode='r', encoding='utf-8-sig') as csvfile:
            movie_file_reader = csv.DictReader(csvfile)

            for row in movie_file_reader:

                # Pulling Data
                title = row['Title']
                genres = [Genre(genre.strip())
                          for genre in (row['Genre'].split(','))]
                description = row['Description']
                directors = [Director(
                    full_name=director.strip()) for director in (row['Director'].split(','))]
                actors = [Actor(
                    full_name=actor.strip()) for actor in (row['Actors'].split(','))]
                release_year = int(row['Year'])
                runtime_minutes = int(row['Runtime (Minutes)'])
                average_rating = row['Rating']
                vote_count = int(row['Votes'])
                revenue = float(row['Revenue (Millions)']
                                ) if row['Revenue (Millions)'] != 'N/A' else 0.0
                metascore = int(
                    row['Metascore']) if row['Metascore'] != 'N/A' else 0.0

                # Creating Movie
                movie = Movie(
                    title=title,
                    genres=genres,
                    description=description,
                    directors=directors,
                    actors=actors,
                    release_year=release_year,
                    runtime_minutes=runtime_minutes,
                    average_rating=average_rating,
                    vote_count=vote_count,
                    revenue=revenue,
                    metascore=metascore
                )
                self.__dataset_of_movies.append(movie)

                # Populating Genres
                for genre in genres:
                    if genre not in self.__dataset_of_genres:
                        self.__dataset_of_genres.append(genre)

                # Populating Directors
                for director in directors:
                    if director not in self.__dataset_of_directors:
                        self.__dataset_of_directors.append(director)

                # Populating Actors
                for actor in actors:
                    if actor not in self.__dataset_of_actors:
                        self.__dataset_of_actors.append(actor)

    @property
    def dataset_of_movies(self):
        return self.__dataset_of_movies

    @property
    def dataset_of_reviews(self):
        return self.__dataset_of_reviews

    @property
    def dataset_of_genres(self):
        return self.__dataset_of_genres

    @property
    def dataset_of_directors(self):
        return self.__dataset_of_directors

    @property
    def dataset_of_actors(self):
        return self.__dataset_of_actors

    @property
    def dataset_of_ratings(self):
        return self.__dataset_of_ratings
