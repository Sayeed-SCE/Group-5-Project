from app import app
from flask import Flask, render_template, flash, redirect
from app.forms import userLogin, userRegistry

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
    form = userRegistry()
    title = 'Register New User'
    usernameList = {
        'user1', 'user2', 'David'
    }
    return render_template('registry.html', title = title, form = form, usernameList = usernameList)


