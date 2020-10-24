from flask import Flask

app = Flask(__name__)

from app import routes, osm_api, angle_match, angle_match2, os_api

def clever_function(name):
    return u'HELLO' + name

app.jinja_env.globals.update(clever_function=clever_function)