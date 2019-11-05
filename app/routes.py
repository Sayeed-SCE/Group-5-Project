from app import app, db, LoginManager
from flask import Flask, render_template, flash, redirect, url_for
from flask_login import current_user, login_user, logout_user, login_required
from app.forms import userLogin, userRegistry
from app.models import User

@app.route('/index')
@login_required
def index():
    user = {'username': 'David'}
    return render_template('index.html', title = 'Home', user = user)

@app.route('/login', methods = ['GET', 'POST']) #return a message that login was unsuccessful
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
        login_user(user, remember = form.rememberMe.data)
        return redirect(url_for('index'))
    return render_template('login.html', form = form, title = title)

@app.route('/logout') #make this option unavailable when no one is logged in
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/friends')
@login_required
def friends():
    form = userLogin()
    title = 'Friends'
    friend_list = [ 'friend1', 'friend2', 'friend2', 'friendetc' ]
    return render_template('friends.html', title = title, form = form, friends = friend_list)

@app.route('/groups')
@login_required
def groups():
    form = userLogin()
    title = 'Groups'
    group_list = {
        'Group1' : [ 'member1', 'member2', 'member3' ],
        'Group2' : [ 'member1', 'member2', 'member3' ],
        'Groupetc' : 'membersetc'
    }
    return render_template('groups.html', title = title, form = form, groups = group_list)

@app.route('/register', methods = ['GET', 'POST']) #return error messages if register wasnt complete
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


