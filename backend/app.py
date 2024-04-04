from flask import Flask, send_from_directory
from api import api_bp

app = Flask(__name__, static_folder='/usr/src/app/frontend/dist', static_url_path="")
app.register_blueprint(api_bp)

@app.route("/", defaults={'path': ''})
@app.route('/<path:path>')
def index(path):
    return send_from_directory(app.static_folder, "index.html")

if __name__ == '__main__':
    app.run()