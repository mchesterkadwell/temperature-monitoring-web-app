from flask import render_template
from app import cache
from . import main, weather_api, cache_timeout
from app.models import Reading
from config import Config


@main.route('/')
@main.route('/index')
def index():
    """
    Main index page showing the weather station dashboard.
    :return: html of the rendered index template
    """
    return render_template('index.html',
                           name=Config.PERSON_NAME,
                           )


@main.route('/weather')
@cache_timeout.modify(timeout=10800, begin='22:00:00', end='06:00:00')
@cache.cached(timeout=3600)  # 1 hour
def weather():
    """
    Called on page load by ajax in index.html and periodically thereafter. The
    result is cached to prevent excessive calls to the weather API, regardless
    of the frequency with which it is requested.
    :return: html of the rendered weather template
    """
    current_conditions = weather_api.get_current_conditions()
    forecast = weather_api.get_forecast()

    return render_template('weather.html',
                           location=Config.LOCATION,
                           current_conditions=current_conditions,
                           forecast=forecast,
                           )


@main.route('/room/<name>')
def room(name):
    reading = Reading.query.filter_by(
        topic='house/thermometers/{}'.format(name)).first_or_404()
    return render_template('room.html', name=name, reading=reading)
