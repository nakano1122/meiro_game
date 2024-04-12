from flask import Blueprint, jsonify, request
import random
from flask_restful import Api, Resource
from models import add_user

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

class AddUser(Resource):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        if name:
            add_user(name=name)
            return {'message': 'ユーザー名が正常に登録されました。'}
        else:
            return {'error', '登録に失敗しました。'}, 400

api = Api(api_bp)
api.add_resource(NoviceModeGet, '/start/novice')
api.add_resource(IntermediateModeGet, '/start/intermediate')
api.add_resource(AdvanceModeGet, '/start/advance')
api.add_resource(AddUser, '/addUser')