from flask import Blueprint, jsonify
import random
from flask_restful import Api, Resource

api_bp = Blueprint('api', __name__, url_prefix='/api')

def generate_maze():
    board = [[random.choice([True, False]) for _ in range(7)] for _ in range(8)]
    return board

class NoviceModeGet(Resource):
    def get(self):
        maze = generate_maze()
        stepLimit = 20
        return jsonify({
            "maze": maze,
            "stepLimit": stepLimit,
        })
class IntermediateModeGet(Resource):
    def get(self):
        maze = generate_maze()
        stepLimit = 20
        return jsonify({
            "maze": maze,
            "stepLimit": stepLimit,
        })
class AdvanceModeGet(Resource):
    def get(self):
        maze = generate_maze()
        stepLimit = 20
        return jsonify({
            "maze": maze,
            "stepLimit": stepLimit,
        })

api = Api(api_bp)
api.add_resource(NoviceModeGet, '/start/novice')
api.add_resource(IntermediateModeGet, '/start/intermediate')
api.add_resource(AdvanceModeGet, '/start/advance')