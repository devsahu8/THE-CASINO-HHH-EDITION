from flask_wtf import FlaskForm
from wtforms import SubmitField,StringField,PasswordField,BooleanField,IntegerField
from wtforms.validators import DataRequired,Email,EqualTo,ValidationError
import sqlalchemy as sa
from app import db
from app.models import User

class IndexForm(FlaskForm):
    submit=SubmitField("Enter the Loby!")


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self,username):
        user=db.session.scalar(sa.select(User).where(User.username==username.data))
        if user is not None:
            raise ValidationError("Use a diffrent username.")
        
    def validate_email(self,email):
        user=db.session.scalar(sa.select(User).where(User.email==email.data))
        if user is not None:
            raise ValidationError("Use a diffrent Email.")
        
class GameForm(FlaskForm):
    bet=IntegerField("BET AMOUNT")
    submit=SubmitField("ROLL")


class UserForm(FlaskForm):
    deposit=IntegerField("You can get free credits for now.")
    submit=SubmitField("GET")