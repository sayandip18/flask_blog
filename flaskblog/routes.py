from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.forms import RegistrationForm, LoginForm
from flaskblog.models import User, Post

posts = [
    {
        'author': 'Sayandip Halder',
        'title': 'First post',
        'content': 'lorem ipsum'
    },
    {
        'author': 'Potai Halder',
        'title': 'Second post',
        'content': 'lorem ipsum'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'You have been logged in!', 'success')
        return redirect(url_for('home'))
    else:
        flash('Login unsuccessful. Please check email or password :(', 'danger')
    return render_template('login.html', title='Login', form=form)

