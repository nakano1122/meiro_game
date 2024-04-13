from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from collections import namedtuple

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    results = db.relationship('Results', backref='user', lazy=True)

class Results(db.Model):
    __tablename__ = 'results'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    level = db.Column(db.Text, nullable=False)
    clearTime = db.Column(db.Integer, nullable=False)
    collectedCoins = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, index=True, default=datetime.now)

def init_db(app):
    db.init_app(app)
    with app.app_context():
        db.create_all()

def add_user(username):
    already = db.session.query(Users).filter(Users.username == username).first()
    if not already:
        model = Users(username=username)
        db.session.add(model)
        db.session.commit()


def result_post(username, level, collectedCoins, clearTime):
    user = db.session.query(Users).filter(Users.username == username).first()
    model = Results(
        user_id=user.id,
        level=level,
        clearTime=clearTime,
        collectedCoins=collectedCoins
    )
    db.session.add(model)
    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e


Ranking = namedtuple('Ranking', [
    'result_id',
    'username',
    'clear_time',
    'collected_coins',
    'timestamp'
])
def get_ranking(level):
    rank5_init = db.session.query(
        Results.id,
        Users.username,
        Results.clearTime,
        Results.collectedCoins,
        Results.timestamp
    ).join(Users, Users.id == Results.user_id
    ).filter(Results.level == level).order_by(
    desc(Results.collectedCoins),
    Results.clearTime
    ).limit(5).all()

    rank5 = [Ranking(
        result_id=row[0],
        username=row[1],
        clear_time=row[2],
        collected_coins=row[3],
        timestamp=row[4]
    ) for row in rank5_init]
    
    # デバッグ用コード
    print(f"Retrieved rankings: {rank5}")
    return rank5