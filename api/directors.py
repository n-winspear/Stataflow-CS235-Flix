from flask import make_response, jsonify, session
from flask_restful import Resource, reqparse
from domain_models.director import Director

# DB Connection
db = session['MEMORY_REPO']

# Request Parser
parser = reqparse.RequestParser()

parser.add_argument('personID', type=str,
                    help="Person Identifier")
parser.add_argument('fullName', type=str,
                    help="Persons full name")
parser.add_argument('gender', type=int,
                    help="Persons gender")
parser.add_argument('dateOfBirth', type=str,
                    help="Persons date of birth")
parser.add_argument('imdbPage', type=str,
                    help="Persons IMDB page")


class DirectorList(Resource):
    def get(self):
        response = {
            "directors":  db.get_all_directors()
        }
        return make_response(jsonify(response), 200)

    def post(self):
        args = parser.parse_args()
        response = {
            "successful": False,
            "fullName": args['fullName'],
            "gender": args['gender'],
            "dateOfBirth": args['dateOfBirth'],
            "imdbPage": args['imdbPage'],
        }
        response['successful'] = True if db.add_director(
            Director(
                full_name=args['fullName'],
                gender=args['gender'],
                date_of_birth=args['dateOfBirth'],
                imdb_page=args['imdbPage'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)


class Director(Resource):
    def get(self, personID: str) -> str:
        director = db.get_director(personID=personID)
        response = {
            "successful": True if director else False,
            "director": director,
        }
        if response['successful']:
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 404)

    def put(self, personID: str) -> str:
        args = parser.parse_args()
        response = {
            "successful": False,
            "fullName": args['fullName'],
            "gender": args['gender'],
            "dateOfBirth": args['dateOfBirth'],
            "imdbPage": args['imdbPage'],
        }
        response['successful'] = True if db.update_director(
            Director(
                personID=personID,
                full_name=args['fullName'],
                gender=args['gender'],
                date_of_birth=args['dateOfBirth'],
                imdb_page=args['imdbPage'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)

    def delete(self, personID: str) -> str:
        response = {
            "successful": False,
        }
        response['successful'] = True if db.delete_genre(
            personID=personID) else False
        if response['successful']:
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 404)
