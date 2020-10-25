from flask import render_template, request
from app import app
from app.angle_match import create_feature_collection, get_centre_and_zoom_of_bbox
from app.os_api import get_open_roads_geojson_from_bbox, convert_payload_to_geojson


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/data')
def map_data():
    TARGET_BEARING = 0
    payload = get_open_roads_geojson_from_bbox(51.0162,0.9360,51.1188,1.09977)
    geojson = convert_payload_to_geojson(payload, target_bearing=TARGET_BEARING)
    return geojson


@app.route('/mapbox')
def mapbox():
    TARGET_BEARING = 90
    south = request.args.get('s', default=50.96928265860532, type=float)
    west = request.args.get('w', default=0.8317945347608031, type=float)
    north = request.args.get('n', default=51.06107512796291, type=float)
    east = request.args.get('e', default=1.030244874246165, type=float)
    centre, zoom = get_centre_and_zoom_of_bbox(south, west, north, east)
    payload = get_open_roads_geojson_from_bbox(south, west, north, east)
    geojson = convert_payload_to_geojson(payload, target_bearing=TARGET_BEARING)
    return render_template('mapbox.html', south=south, west=west, north=north, east=east,
                           centre=centre, zoom=zoom, geojson=geojson, debug=True)

