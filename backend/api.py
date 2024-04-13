from flask import Blueprint, jsonify, request, views
from models import add_user, get_ranking, result_post
import random

api_bp = Blueprint('api', __name__, url_prefix='/api')

def generate_maze():
    board = [[random.choice([True, False]) for _ in range(7)] for _ in range(8)]
    return board

class MazeView(views.MethodView):
    def get(self, level):
        maze = generate_maze()
        if level == 'novice':
            stepLimit = 20
        elif level == 'intermediate':
            stepLimit = 30
        elif level == 'advance':
            stepLimit = 50
        return jsonify({
            "level": level,
            "maze": maze,
            "stepLimit": stepLimit,
        })

class AddUserView(views.MethodView):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        try:
            add_user(username=username)
            return jsonify({'message', 'ユーザー登録に成功しました'})
        except Exception as e:
            return jsonify({'message': f'ユーザー登録に失敗しました。エラー内容: {str(e)}'})

class ResultPostView(views.MethodView):
    def post(self):
        data = request.get_json()
        username = data.get('username')
        level = data.get('level')
        collectedCoins = data.get('collectedCoins')
        clearTime = data.get('clearTime')
        try:
            result_post(
                username=username,
                level=level,
                collectedCoins=collectedCoins,
                clearTime=clearTime
            )
            return jsonify({'message': '結果の登録に成功しました'})
        except Exception as e:
            return jsonify({'message': f'結果の登録に失敗しました。エラー内容: {str(e)}'})

class ResultView(views.MethodView):
    def get(self, level):
        rank5 = get_ranking(level=level)
        if rank5:
            results_dict = [r._asdict() for r in rank5]
            return jsonify({
                'results': results_dict,
                'message': 'データ取得に成功しました。'
            })
        else:
            return jsonify({'error': 'データ取得に失敗しました。ランキングデータが存在しません。'}), 400

api_bp.add_url_rule('/start/<string:level>', view_func=MazeView.as_view('maze'))
api_bp.add_url_rule('/resultPost', view_func=ResultPostView.as_view('result_post'))
api_bp.add_url_rule('/result/<string:level>', view_func=ResultView.as_view('get_result_ranking'))
api_bp.add_url_rule('/addUser', view_func=AddUserView.as_view('add_user'))