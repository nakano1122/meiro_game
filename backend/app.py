from flask import Flask, send_from_directory
from api import api_bp
from flask_sqlalchemy import SQLAlchemy
from models import init_db

app = Flask(__name__, static_folder='/usr/src/app/frontend/dist', static_url_path="")
app.register_blueprint(api_bp)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maze.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    with app.app_context():
        init_db(app)
    app.run(host='0.0.0.0')