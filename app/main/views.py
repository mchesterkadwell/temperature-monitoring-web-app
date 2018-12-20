from datetime import datetime
from flask import render_template
from flask import jsonify
from app import cache
from . import main, weather_api, cache_timeout
from app.models import Reading
from config import Config

@main.route('/')
@main.route('/index')
def index():
    current_conditions = weather_api.get_current_conditions()
    forecast = weather_api.get_forecast()

    return render_template('index.html',
                           name=Config.PERSON_NAME,
                           location=Config.LOCATION,
                           current_time=datetime.utcnow(),
                           current_conditions=current_conditions,
                           forecast=forecast,
                           )

@main.route('/weather')
@cache_timeout.modify(timeout=10800, begin='22:00:00', end='06:00:00')
@cache.cached(timeout=3600) # 1 hour
def weather():
    current_conditions = weather_api.get_current_conditions()._asdict()
    forecast = weather_api.get_forecast()._asdict()
    return jsonify(current_conditions, forecast)


@main.route('/room/<name>')
def room(name):
    reading = Reading.query.filter_by(
        topic='house/thermometers/{}'.format(name)).first_or_404()
    return render_template('room.html', name=name, reading=reading)
