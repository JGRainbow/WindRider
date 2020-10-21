from flask import render_template, request
from app import app
from app.osm_api import get_road_ways_from_bbox, get_road_nodes_from_bbox
from app.angle_match import create_feature_collection
from app.angle_match import create_test_feature_collections, create_linestring_star


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
    TARGET_BEARING = 90
    nodes = get_road_nodes_from_bbox(51.0362,0.9360,51.1188,1.1677)
    ways = get_road_ways_from_bbox(51.0362,0.9360,51.1188,1.1677)
    # geojson = create_feature_collection(ways, nodes, TARGET_BEARING)
    star = create_linestring_star(20)
    geojson = create_test_feature_collections(star, TARGET_BEARING)
    return geojson


@app.route('/map2')
def map_func2():
    lat = request.args.get('lat', default=51.1, type=float)
    lon = request.args.get('lon', default=1, type=float)
    print(f'Lat: {lat} \t Lon: {lon}')
    return render_template('map2.html', lat=lat, lon=lon, debug=True)   
