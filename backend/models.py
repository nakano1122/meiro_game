from datetime import datetime
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
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
    db.create_all()

def add_user(name):
    model = Users(name=name)
    db.session.add(model)
    db.session.commit()