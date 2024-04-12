from flask import Blueprint, jsonify, request, views
from models import add_user
import random

api_bp = Blueprint('api', __name__, url_prefix='/api')

def generate_maze():
    board = [[random.choice([True, False]) for _ in range(7)] for _ in range(8)]
    return board

class MazeModeView(views.MethodView):
    def get(self, mode):
        maze = generate_maze()
        stepLimit = 20
        return jsonify({
            "mode": mode,
            "maze": maze,
            "stepLimit": stepLimit,
        })

class AddUserView(views.MethodView):
    def post(self):
        data = request.get_json()
        name = data.get('name')
        if name:
            add_user(name=name)
            return jsonify({'message': 'ユーザー名が正常に登録されました。'})
        else:
            return jsonify({'error': '登録に失敗しました。'}), 400

api_bp.add_url_rule('/start/<string:mode>', view_func=MazeModeView.as_view('maze_mode'))
api_bp.add_url_rule('/addUser', view_func=AddUserView.as_view('add_user'))