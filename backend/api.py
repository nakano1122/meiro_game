from flask import Blueprint
from flask_restful import Api, Resource

api_bp = Blueprint('api', __name__, url_prefix='/api')

class NoviceModeGet(Resource):
    def get(self):
        return "hello";

api = Api(api_bp)
api.add_resource(NoviceModeGet, '/start/novice')