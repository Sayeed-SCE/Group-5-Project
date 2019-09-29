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

if __name__ == '__main__':
    app.run()