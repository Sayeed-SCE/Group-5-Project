from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, validators
from wtforms.validators import DataRequired, Email, EqualTo
from app.models import User

class userLogin(FlaskForm):
    username = StringField('Enter Username')
    password = PasswordField('Enter Password')
    rememberMe = BooleanField('Remember Me')
    submit = SubmitField('Submit')


class userRegistry(FlaskForm):
    username = StringField('Enter Username', validators = [DataRequired()])
    email = StringField('Enter Email',validators=[DataRequired(), Email()])
    password = PasswordField('Enter Password',validators=[DataRequired()])
    password2 = PasswordField('Repeat Password',validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Submit')

    def validate_username(self,username):
        user = User.query.filter_by(username = username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')
    
    def validate_email(self,email):
        user = User.query.filter_by(email = email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
