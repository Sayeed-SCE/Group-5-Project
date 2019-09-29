from flask import Flask
from flask import render_template
from loginform import userLogin

app = Flask(__name__)
app.config['SECRET_KEY'] = 'some-key'

@app.route('/login')
def login():
    form = userLogin()
    title = 'Chatit WebChat'
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

if __name__ == '__main__':
    app.run()