from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField,TextAreaField,IntegerField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from flaskblog.models import User



class RegistrationForm(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')
#WFORMS explains this in more detail 
    def validate_username(self,username):

        user = User.query.filter_by(username = username.data).first()
        if user:
            raise ValidationError('Username has already been taken, please choose another one ')
    def validate_email(self,email):

        user = User.query.filter_by(email = email.data).first()
        if user:
            raise ValidationError('Email has already been taken, please choose another one ')
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

class PostForm (FlaskForm):
    title = StringField ('Title',validators = [DataRequired()])
    content = TextAreaField('Content', validators =[DataRequired()])
    rating = IntegerField('Rating', validators = [DataRequired()])
    book_id = IntegerField('BookID', validators = [DataRequired()])
    submit = SubmitField('Post')

class InsertForm(FlaskForm):
    title = StringField('Title',validators = [DataRequired()])
    isbn = IntegerField('ISBN',validators = [DataRequired()])
    author = StringField('Author', validators = [DataRequired()])
    publicationyear = IntegerField('publicationyear',validators = [DataRequired()])
    description = StringField('Description',validators = [DataRequired()])
    price = IntegerField('Price',validators = [DataRequired()])
    copies_sold = IntegerField('Copies Sold',validators = [DataRequired()])
    publisher = StringField('Publisher', validators = [DataRequired()])
    genre = StringField('Genre',validators = [DataRequired()])
    submit = SubmitField('Insert')



    