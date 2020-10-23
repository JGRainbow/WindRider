from flask import Flask

app = Flask(__name__)

from app import routes, osm_api, angle_match, angle_match2, os_api