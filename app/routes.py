from app import app, db
from flask import Flask, render_template, flash, redirect, url_for
from app.forms import userLogin, userRegistry
from app.models import User

@app.route('/index')
def index():
    user = {'username': 'David'}
    return render_template('index.html', title = 'Home', user = user)

@app.route('/login')
def login():
    form = userLogin()
    title = 'Log in'
    if form.validate_on_submit():
        flash('Login requested for user {}, remember me={}'.format(form.susername.data, form.remember_me))
        return redirect('/index')
    return render_template('login.html', form = form, title = title)

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
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = userRegistry()
    title = 'Register New User'
    if form.validate_on_submit():
        user = User(username = form.username.data, email = form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('registry.html', title = title, form = form)