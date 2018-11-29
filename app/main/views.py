from datetime import datetime
from flask import render_template
from . import main
from app.models import Reading


@main.route('/')
@main.route('/index')
def index():
    return render_template('index.html', current_time=datetime.utcnow())


@main.route('/room/<name>')
def room(name):
    reading = Reading.query.filter_by(
        topic='house/thermometers/{}'.format(name)).first_or_404()
    return render_template('room.html', name=name, reading=reading)
