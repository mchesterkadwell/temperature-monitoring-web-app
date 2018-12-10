from collections import namedtuple
import requests
from config import Config

dataservice = Config.WEATHER_DATASERVICE_URL
location_key = Config.WEATHER_LOCATION_KEY
api_key = Config.WEATHER_API_KEY

CurrentConditions = namedtuple('CurrentConditions', 'conditions_phrase icon is_day')
Forecast = namedtuple('Forecast', 'day_phrase night_phrase high_temp low_temp day_rain_percent night_rain_percent')

def get_current_conditions():
    url = f'{dataservice}/currentconditions/v1/{location_key}?apikey={api_key}&language=en-gb'
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()[0]
        return CurrentConditions(data['WeatherText'],
                                 data['WeatherIcon'],
                                 data['IsDayTime'],
                                 )

def get_forecast():
    url = f'{dataservice}/forecasts/v1/daily/1day/{location_key}?apikey={api_key}&language=en-gb&details=true&metric=true'
    resp = requests.get(url)
    if resp.status_code == 200:
        data = resp.json()
        return Forecast(data['DailyForecasts'][0]['Day']['LongPhrase'],
                        data['DailyForecasts'][0]['Night']['LongPhrase'],
                        data['DailyForecasts'][0]['Temperature']['Maximum']['Value'],
                        data['DailyForecasts'][0]['Temperature']['Minimum']['Value'],
                        data['DailyForecasts'][0]['Day']['PrecipitationProbability'],
                        data['DailyForecasts'][0]['Night']['PrecipitationProbability']
                        )