from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if (__name__ == '__main__'):
    app.run(debug=True)
