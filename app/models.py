from app import db
from datetime import datetime
from flask.ext.login import UserMixin, AnonymousUserMixin
from . import db, login_manager


class BaseModel(db.Model):
    __abstract__ = True


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True)
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))
    date_joined = db.Column(db.DateTime(), default=datetime.utcnow)
    games = db.relationship('Game', backref='user', lazy='dynamic')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class AnonymousUser(AnonymousUserMixin):
    def can(self, permissions):
        return False

    def is_administrator(self):
        return False

login_manager.anonymous_user = AnonymousUser


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    creator = db.Column(db.Integer, db.ForeignKey('users.id'))
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    players = db.relationship('Player', backref='game', lazy='dynamic')


class Player(db.Model):
    __tablename__ = 'players'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(64))
    game = db.Column(db.Integer, db.ForeignKey('games.id'))

    def __repr__(self):
        return '<Player %s>' % self.username

