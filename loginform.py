from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField

class userLogin(FlaskForm):
    username = StringField('Enter Username')
    password = PasswordField('Enter Password')
    submit = SubmitField('Submit')
    message = SubmitField('Message')
    remove = SubmitField('Remove')
    leave = SubmitField('Leave Group')