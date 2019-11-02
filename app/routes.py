from app import app
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import userLogin, userRegistry
from app.models import User

@app.route('/index')
@login_required
def index():
    user = {'username': 'David'}
    return render_template('index.html', title = 'Home', user = user)

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = userLogin()
    title = 'Log in'
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember = form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('login.html', form = form, title = title)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/friends')
def friends():
    form = userLogin()
    title = 'Friends'
    friend_list = [ 'friend1', 'friend2', 'friend2', 'friendetc' ]
    return render_template('friends.html', title = title, form = form, friends = friend_list)

@app.route('/groups')
def groups():
    form = userLogin()
    title = 'Groups'
    group_list = {
        'Group1' : [ 'member1', 'member2', 'member3' ],
        'Group2' : [ 'member1', 'member2', 'member3' ],
        'Groupetc' : 'membersetc'
    }
    return render_template('groups.html', title = title, form = form, groups = group_list)

@app.route('/register')
def register():
    form = userRegistry()
    title = 'Register New User'
    usernameList = {
        'user1', 'user2', 'David'
    }
    return render_template('registry.html', title = title, form = form, usernameList = usernameList)


