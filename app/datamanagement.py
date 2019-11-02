from app import db
from app.models import User, Post

def deleteAllUsers():
    for u in User.query.all():
        db.session.delete(u)
    db.session.commit()

def deleteAllPosts():
    for p in Post.query.all():
        db.session.delete(p)
    db.session.commit()

def deleteAllUserPosts(user):
    for p in user.posts:
        db.session.delete(p)
    db.session.commit()

def deleteUser(user):
    db.session.delete(user)
    db.session.commit()

def deletePost(post):
    db.session.delete(post)
    db.session.commit()