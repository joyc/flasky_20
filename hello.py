from flask import Flask
from flask import request
from flask import render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)

@app.route('/')
def index():
    return render_template('index.html')

def top():
    return "<h2>Ni hao Flask世界！<br> 我是%s</h2>" % "言言"

app.add_url_rule('/top', 'top', top)


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_server_error(e):
    return render_template('404.html'), 500

if __name__ == '__main__':
    app.run(debug=True)
