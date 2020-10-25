from flask import render_template, request
from app import app
from app.osm_api import get_road_ways_from_bbox, get_road_nodes_from_bbox
from app.angle_match import create_feature_collection, get_centre_and_zoom_of_bbox
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


# http://127.0.0.1:5000/mapbox/?s=50.93816400806824&w=0.747428527832767&n=51.094104887057256&e=1.084571472168534
# @app.route('/mapbox')
@app.route('/mapbox', methods=['GET', 'POST'])
def mapbox():
    TARGET_BEARING = 90
    south = request.args.get('s', default=50.96928265860532, type=float)
    west = request.args.get('w', default=0.8317945347608031, type=float)
    north = request.args.get('n', default=51.06107512796291, type=float)
    east = request.args.get('e', default=1.030244874246165, type=float)
    centre, zoom = get_centre_and_zoom_of_bbox(south, west, north, east)
    # print(f'New Centre: \t {centre}')
    payload = get_open_roads_geojson_from_bbox(south, west, north, east)
    geojson = convert_payload_to_geojson(payload, target_bearing=TARGET_BEARING)
    return render_template('mapbox.html', south=south, west=west, north=north, east=east,
                           centre=centre, zoom=zoom, geojson=geojson, debug=True)


@app.route('/test')
def get_position():
    lon = request.args.get('lon', default=0.9, type=float)
    lat = request.args.get('lat', default=51, type=float)
    zoom = request.args.get('zoom', default=5, type=int)
    return render_template('test.html', lon=lon, lat=lat, zoom=zoom)


