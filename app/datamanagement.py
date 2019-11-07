from app import db
from app.models import *

def deleteAllUsers():
    for u in User.query.all():
        db.session.delete(u)
    db.session.commit()

def deleteDirectMessage(directMessage):
    db.session.delete(directMessage)
    db.session.commit()

def deleteAllMessages():
    for p in Message.query.all():
        db.session.delete(p)
    db.session.commit()

def deleteAllUserMessages(user):
    for p in user.messages:
        db.session.delete(p)
    db.session.commit()

def deleteUser(user):
    db.session.delete(user)
    db.session.commit()

def deleteMessage(message):
    db.session.delete(message)
    db.session.commit()

def deleteFriend(friend):
    db.session.delete(friend)
    db.session.commit()
