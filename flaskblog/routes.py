from flask import render_template, url_for,flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

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
