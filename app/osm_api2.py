import requests
import overpy

API = overpy.Overpass()
URL = r"https://www.overpass-api.de/api/interpreter?data=[out:json];way({},{},{},{})['highway'~'(primary|secondary|tertiary)$'];{}"


def get_road_ways_json_from_bbox(lat_south,
                                 lon_west,
                                 lat_north,
                                 lon_east):
    url = URL.format(lat_south, lon_west, lat_north, lon_east, 'out;')
    response = requests.get(url)
    return response.json()


def get_road_nodes_json_from_bbox(lat_south,
                                  lon_west,
                                  lat_north,
                                  lon_east):
    url = URL.format(lat_south, lon_west, lat_north, lon_east, 'node(w);out;')
    response = requests.get(url)
    return response.json()

