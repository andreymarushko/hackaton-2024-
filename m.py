from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    goals = db.relationship('Goal', backref='owner', lazy=True)
    challenges = db.relationship('Challenge', secondary='team_users', backref='participants')

    def __repr__(self):
        return f'<User {self.username}>'


class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    description = db.Column(db.String(200), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    achieved = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<Goal {self.description}>'


class Challenge(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)
    teams = db.relationship('Team', backref='challenge', lazy=True)

    def __repr__(self):
        return f'<Challenge {self.title}>'


class Team(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    challenge_id = db.Column(db.Integer, db.ForeignKey('challenge.id'), nullable=False)
    users = db.relationship('User', secondary='team_users', backref='teams')

    def __repr__(self):
        return f'<Team {self.name}>'


class TeamUsers(db.Model):
    __tablename__ = 'team_users'
    team_id = db.Column(db.Integer, db.ForeignKey('team.id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), primary_key=True)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    description = db.Column(db.String(500), nullable=True)

    def __repr__(self):
        return f'<Event {self.title}>'
