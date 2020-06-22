from datetime import datetime
from flask import Flask, render_template, url_for,flash, redirect
from flask_sqlalchemy import SQLAlchemy
from forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = 'ce9a6ed38bc685d74b46bdb13f38e7db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), unique=True, nullable=False, default='default.jpeg')
    password = db.Column(db.String(60), nullable=False)
    posts = db.relationship('Post', backref='author', lazy=True)

    # def __init__(self, id,username,email,image_file,password):
    #     self.id = id
    #     self.username = username
    #     self.email = email
    #     self.image_file = image_file
    #     self.password = password

    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    published_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),  nullable=False)

    def __repr__(self):
        return f"Post('{self.title}', '{self.published_date}')"

posts = [
    {
        'author':'dilshanka',
        'title':'OctoberCMS',
        'content' :'dummy content',
        'published_date':'June 10th 20'
    },
    {
        'author':'araliya',
        'title':'Wordpress',
        'content' :'dummy content',
        'published_date':'June 5th 20'
    },
    {
        'author':'dilshanka',
        'title':'SPOJ',
        'content' :'dummy content',
        'published_date':'April 10th 20'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html', title="About Us")

@app.route('/register', methods=['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title="Register", form=form)

@app.route('/login', methods=['POST','GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if ((form.email.data == 'admin@blog.com') and (form.password.data == 'password')):
            flash('You have been logged in', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Faild, Try Again', 'danger')
    return render_template('login.html', title="Login", form=form)


if (__name__ == '__main__'):
    app.run(debug=True)
