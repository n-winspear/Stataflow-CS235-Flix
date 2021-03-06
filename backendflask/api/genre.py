from flask import make_response, jsonify
from flask_restful import Resource, reqparse
from backendflask.adapters.memoryrepository import MemoryRepository
from backendflask.adapters.gcloudrepository import GCloudRepository
from backendflask.domain_models.genre import Genre
import json

# DB Connection
db = MemoryRepository()
#db = GCloudRepository()

# Request Parser
parser = reqparse.RequestParser()

parser.add_argument('genreName', type=str,
                    help="Name of the genre")


class Genre(Resource):
    def get(self, genreID: str) -> str:
        genre = db.get_genre(genreID=genreID)
        response = {
            "successful": True if genre else False,
            "genre": genre.toJSON(),
        }
        if response['successful']:
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 404)

    def put(self, genreID: str) -> str:
        args = parser.parse_args()
        response = {
            "successful": False,
            "genreName": args['genreName'],
        }
        response['successful'] = True if db.update_genre(
            Genre(
                genreID=genreID,
                genre_name=args['genreName'],
            )
        ) else False
        if response['successful']:
            return make_response(jsonify(response), 201)
        else:
            return make_response(jsonify(response), 400)

    def delete(self, genreID: str) -> str:
        response = {
            "successful": False,
        }
        response['successful'] = True if db.delete_genre(
            genreID=genreID) else False
        if response['successful']:
            return make_response(jsonify(response), 200)
        else:
            return make_response(jsonify(response), 404)
