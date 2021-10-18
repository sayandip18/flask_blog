from flask import Flask, render_template, url_for
from flask.templating import render_template_string
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = '70ad1cc4f66ff8fab0c7e40b0715aaac'

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
def hello_world():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register")
def register():
    form = RegistrationForm()
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)