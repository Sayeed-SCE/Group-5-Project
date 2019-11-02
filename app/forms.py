from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Email, EqualTo

class userLogin(FlaskForm):
    username = StringField('Enter Username')
    password = PasswordField('Enter Password')
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class userRegistry(FlaskForm):
    username = StringField('Enter Username', validators = [DataRequired()])
    email =StringField('Enter Email',validators=[DataRequired(), Email()])
    password =PasswordField('Enter Password',validators=[DataRequired()])
    password2 =PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')