from flask import render_template, url_for, flash, redirect
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm, LoginForm,PostForm,InsertForm
from flaskblog.models import User, Post,Book
from flask_login import login_user,current_user,logout_user,login_required
from sqlalchemy.sql import func





@app.route("/")
@app.route("/home")
def home():
    posts = Post.query.all()
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', books=books)

# wtforms explains this 
@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username = form.username.data,email=form.email.data,password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created ', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check your email and password', 'danger')
    return render_template('login.html', title='Login', form=form)
@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))


@app.route("/post/new/",methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title = form.title.data,content = form.content.data,author = current_user,rating = form.rating.data,book_id =form.book_id.data)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!','success')
        return redirect(url_for('home'))
    return render_template('create_post.html', title='New Post',form = form)

@app.route("/insert_book",methods=['GET', 'POST'])
@login_required
def new_book():
    form = InsertForm()
    if form.validate_on_submit():
        book = Book(title = form.title.data,isbn = form.isbn.data,author = form.author.data,publicationyear = form.publicationyear.data,description = form.description.data, price = form.price.data,copies_sold = form.copies_sold.data,publisher = form.publisher.data, genre = form.genre.data)
        db.session.add(book)
        db.session.commit()
        flash('Your Book has been created!','success')
        return redirect(url_for('home'))
    return render_template('insert_book.html', title='New Book',form = form)

@app.route("/books")
@login_required
def index():
    #posts = Post.query.order_by(Post.rating.desc())
    posts = Post.query.func.avg(Post.rating).all()
    return render_template('books.html', posts = posts)






    


