from backendflask.domain_models.person import Person
import re
import phonenumbers
from password_validator import PasswordValidator
import datetime as datetime


class User(Person):

    def __init__(self, first_name: str, last_name: str, personID: str = None, email_address: str = None, password: str = None, phone_number: str = None, gender: int = None, date_of_birth: str = None, watchlist: list = [], watched_movies: list = [], reviews: list = []):

        # First Name
        self.__first_name = first_name.strip() if type(first_name) == str else ""

        # Last Name
        self.__last_name = last_name.strip() if type(last_name) == str else ""

        # Parent Class Call
        super(User, self).__init__(
            f"{self.__first_name} {self.__last_name}", personID, gender, date_of_birth)

        # Email Address
        self.__email_address = email_address.strip() if self.__valid_email_address(
            email_address) else None

        # Password
        self.__password = password if self.__valid_password(
            password) else None

        # Phone Number
        self.__phone_number = phone_number if self.__valid_phone_number(
            phone_number) else None

        # Watchlist
        self.__watchlist = watchlist if self.__valid_watchlist(
            watchlist) else self.__cleaned_watchlist(watchlist)

        # Watched Movies
        self.__watched_movies = watched_movies if self.__valid_watched_movies(
            watched_movies) else self.__cleaned_watched_movies(watched_movies)

        # Reviews
        self.__reviews = reviews if self.__valid_reviews(
            reviews) else self.__cleaned_reviews(reviews)

    def __str__(self):
        return f"{self.__first_name} {self.__last_name}"

    def __repr__(self):
        return f"User <{self.__last_name}, {self.__first_name}>"

    def toJSON(self):
        json_dump = {
            'personID': str(self._personID),
            'firstName': self.__first_name,
            'lastName': self.__last_name,
            'gender': self._gender,
            'emailAddress': self.__email_address,
            'password': self.__password,
            'phoneNumber': self.__phone_number,
            'dateOfBirth': self._date_of_birth,
            'watchlist': [movie.toJSON() for movie in self.__watchlist],
            'watchedMovies': [movie.toJSON() for movie in self.__watched_movies],
            'reviews': [review.toJSON() for review in self.__reviews]
        }
        return json_dump

    # Properties
    @property
    def personID(self):
        return self._personID

    @property
    def first_name(self):
        return self.__first_name

    @first_name.setter
    def first_name(self, first_name: str = None) -> str:
        self.__first_name = first_name.strip().lower(
        ).capitalize() if type(first_name) == str else ""

    @property
    def last_name(self):
        return self.__last_name

    @last_name.setter
    def last_name(self, last_name: str = None) -> str:
        self.__last_name = last_name.strip().lower(
        ).capitalize() if type(last_name) == str else ""

    @property
    def email_address(self):
        return self.__email_address

    @email_address.setter
    def email_address(self, email_address: str = None) -> str:
        self.__email_address = email_address.strip() if self.__valid_email_address(
            email_address.strip()) else None

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password: str = None) -> str:
        self.__password = password if self.__valid_password(
            password) else None

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, phone_number: str = None) -> str:
        self.__phone_number = phone_number if self.__valid_phone_number(
            phone_number) else None

    @property
    def watchlist(self):
        return self.__watchlist

    @watchlist.setter
    def watchlist(self, watchlist: list = []) -> list:
        self.__watchlist = watchlist if self.__valid_watchlist(
            watchlist) else self.__cleaned_watchlist(watchlist)

    @property
    def watched_movies(self):
        return self.__watched_movies

    @watched_movies.setter
    def watched_movies(self, watched_movies: list = []) -> list:
        self.__watched_movies = watched_movies if self.__valid_watched_movies(
            watched_movies) else self.__cleaned_watched_movies(watched_movies)

    @property
    def reviews(self):
        return self.__reviews

    @reviews.setter
    def reviews(self, reviews: list = []) -> list:
        self.__reviews = reviews if self.__valid_reviews(
            reviews) else self.__cleaned_reviews(reviews)

    # Validators
    # Phone Number Check
    def __valid_phone_number(self, phone_number: str):
        # None means no specific country
        try:
            parsed_number = phonenumbers.parse(phone_number, None)
            if phonenumbers.is_valid_number(parsed_number):
                return parsed_number
            else:
                return None
        except Exception as e:
            return None

    # Email Address Check
    def __valid_email_address(self, email_address: str) -> str:
        if email_address:
            return (re.match("^[a-zA-Z0-9_+&*-]+(?:\\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\\.)+[a-zA-Z]{2,7}$", email_address) != None)
        return False

    # Password Check
    def __valid_password(self, password: str) -> str:

        if type(password) == str:

            schema = PasswordValidator()

            schema\
                .min(8)\
                .max(100)\
                .has().uppercase()\
                .has().lowercase()\
                .has().digits()\
                .has().no().spaces()\
                .has().symbols()\

            return schema.validate(password)

        else:
            return False

    # Watchlist Check
    def __valid_watchlist(self, watchlist: list) -> list:
        from backendflask.domain_models.movie import Movie
        for movie in watchlist:
            if isinstance(movie, Movie):
                return False
        return True

    # Watchlist Cleaner
    def __cleaned_watchlist(self, watchlist: list) -> list:
        from backendflask.domain_models.movie import Movie

        cleaned_list = []

        for movie in watchlist:
            if isinstance(movie, Movie):
                cleaned_list.append(movie)

        return cleaned_list

    # Watched Movies Check
    def __valid_watched_movies(self, watched_movies: list) -> list:
        from backendflask.domain_models.movie import Movie

        for movie in watched_movies:
            if isinstance(movie, Movie):
                return False
        return True

    # Watched Movies Cleaner
    def __cleaned_watched_movies(self, watched_movies: list) -> list:
        from backendflask.domain_models.movie import Movie

        cleaned_list = []

        for movie in watched_movies:
            if isinstance(movie, Movie):
                cleaned_list.append(movie)

        return cleaned_list

    # Reviews Check
    def __valid_reviews(self, reviews: list) -> list:
        from backendflask.domain_models.review import Review

        for review in reviews:
            if isinstance(review, Review):
                return False
        return True

    # Reviews Cleaner
    def __cleaned_reviews(self, reviews: list) -> list:
        from backendflask.domain_models.review import Review

        cleaned_list = []

        for review in reviews:
            if isinstance(review, Review):
                cleaned_list.append(review)

        return cleaned_list
