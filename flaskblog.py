from flask import Flask, render_template, url_for

app = Flask(__name__)

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

if __name__ == "__main__":
    app.run(debug=True)