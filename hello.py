from flask import Flask
from flask import request
from flask import render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def top():
    return "<h2>Ni hao Flask世界！<br> 我是%s</h2>" % "言言"

app.add_url_rule('/top', 'top', top)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
