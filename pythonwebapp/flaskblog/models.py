from datetime import datetime
from flaskblog import db, login_manager
from flask_login import UserMixin
from flask_table import LinkCol




@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)
    

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    book_id = db.Column(db.Integer, db.ForeignKey('book.id'), nullable = True)
    rating = db.Column(db.Integer, nullable = False)
    books = db.relationship('Book',backref = 'post',lazy = True)

    def __repr__(self):
        return f"Post('{self.title}', '{self.date_posted}')"


class Book (db.Model):
    id = db.Column(db.Integer, primary_key = True)
    isbn = db.Column(db.String, unique = True, nullable = False)
    title = db.Column(db.String, nullable=False)
    author = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable = False)
    publisher = db.Column(db.String, nullable = False)
    price = db.Column(db.Integer, nullable = False)
    copies_sold = db.Column(db.Integer, nullable = False)
    genre = db.Column(db.String, nullable = False)
    publicationyear = db.Column(db.Integer, nullable=False)
    reviews = db.relationship('Post', backref="book", lazy=True)


    def add_review(self, user_id, text, rating):
        r = Post(user_id = user_id, book_id = self.id, text = text, rating = rating)
        db.session.add(r)
        db.session.commit()




