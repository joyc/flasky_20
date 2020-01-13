from datetime import datetime
from flask import Flask
from flask import request
from flask import render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
app.config['SECRET_KEY'] = 'add SECRET_KEY for Flask-WTF'
bootstrap = Bootstrap(app)
moment = Moment(app)


class NameForm(FlaskForm):
    name = StringField('What is your name?', validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def index():
    name = None
    form = NameForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
    return render_template('index.html', form=form, name=name, current_time=datetime.utcnow())

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
