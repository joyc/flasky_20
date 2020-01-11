from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>Hello Flask!</h1>"

def top():
    return "<h2>Ni hao Flask世界！<br> 我是%s</h2>" % "言言"

app.add_url_rule('/top', 'top', top)


@app.route('/user/<name>')
def user(name):
    return '<h3>Hello, {}!<h3>'.format(name)


if __name__ == '__main__':
    app.run(debug=True)
