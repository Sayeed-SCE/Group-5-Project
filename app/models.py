from app import db, login
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index = True, unique = True)
    email = db.Column(db.String(128), index = True, unique = True)
    password_hash = db.Column(db.String(128))
    def __repr__(self):
        return '<User {}>'.format(self.username)
    messages = db.relationship('Message', backref = 'author')
    friendsList = db.relationship('Friend', backref = 'requestee')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def is_active(self):
        return UserMixin.is_active(self)

    def is_authenticated(self):
        return UserMixin.is_authenticated(self)
    
    def get_id(self):
        return UserMixin.get_id(self)


class Message(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index=True, default = datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<Messages: {}>'.format(self.body)

class directMessage(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, index = True, default = datetime.utcnow)
    sent_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    receive_user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sent = db.relationship(User, foreign_keys=[sent_user_id])
    receive = db.relationship(User, foreign_keys=[receive_user_id])
    def __repr__(self):
        return '<Messages between users: {}>'.format(self.body)

class Friend(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    friendUsername = db.Column(db.String(256))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    def __repr__(self):
        return '<Friends: {}>'.format(self.friendUsername)
    
