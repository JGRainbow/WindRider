from flask import render_template, request
from app import app
from app.osm_api import get_road_ways_from_bbox, get_road_nodes_from_bbox
from app.angle_match import create_feature_collection
from app.angle_match import create_test_feature_collections, create_linestring_star
from app.os_api import get_open_roads_geojson_from_bbox, convert_payload_to_geojson


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/map')
def map_func():
    lat = request.args.get('lat', default=51.1, type=float)
    lon = request.args.get('lon', default=1, type=float)
    print(f'Lat: {lat} \t Lon: {lon}')
    return render_template('map.html', lat=lat, lon=lon, debug=True)   


@app.route('/data')
def map_data():
    TARGET_BEARING = 0
    payload = get_open_roads_geojson_from_bbox(51.0162,0.9360,51.1188,1.09977)
    geojson = convert_payload_to_geojson(payload, target_bearing=TARGET_BEARING)
    return geojson


@app.route('/mapbox')
def mapbox():
    return render_template('mapbox.html', convert_payload_to_geojson=convert_payload_to_geojson)

# Feed mapbox the coords of bbox, then generate geojson, then pass that to render_template?
# What happens when map moves?