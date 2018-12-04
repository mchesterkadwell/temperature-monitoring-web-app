import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'tamar.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MQTT_BROKER_URL = os.environ.get('MQTT_BROKER_URL') or 'localhost'
    MQTT_BROKER_PORT = int(os.environ.get('MQTT_BROKER_PORT')) or 1883
    MQTT_CLIENT_ID = os.environ.get('MQTT_CLIENT_ID') or 'flask_mqtt'

    PERSON_NAME = os.environ.get('PERSON_NAME') or 'Nemo'
    LOCATION = os.environ.get('LOCATION') or 'London'
