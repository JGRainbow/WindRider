from collections import namedtuple
from itertools import tee
from typing import List

import overpy
import pyproj
from geojson import Feature, FeatureCollection
from numpy import cos, pi
from shapely.geometry import LineString

PolarCoord = namedtuple('PolarCoord', 'bearing distance')
GEODESIC = pyproj.Geod(ellps='WGS84')


def create_linestring_from_way(way: overpy.Way, nodes):
    node_id_list = get_all_node_ids_on_way(way)
    node_list = select_nodes_from_node_ids(nodes, node_id_list)
    coord_list = convert_node_list_to_coord_list(node_list)
    linestring = LineString(coord_list)
    return linestring


def create_feature_collection(ways, nodes, target_bearing, crs="EPSG:4326"):
    # TODO: Make this a list comprehension
    features = []
    for way in ways:
        linestring = create_linestring_from_way(way, nodes)
        match = calculate_bearing_match_of_linestring(linestring, target_bearing)
        feature = Feature(geometry=linestring, properties={'match': match})
        features.append(feature)
    fc = FeatureCollection(features, crs=crs)
    return fc


def convert_cartesian_linestring_to_polar_linestring(linestring: LineString):
    polar_linestrings = [convert_cartesian_coords_to_polar_coords(start_coord, end_coord)
                         for (start_coord, end_coord) in pairwise(linestring.coords)]
    return polar_linestrings


def convert_cartesian_coords_to_polar_coords(start_coord, end_coord,
                                             geodesic: pyproj.Geod = GEODESIC):
    fwd_bearing, _, distance = geodesic.inv(*start_coord, *end_coord)
    return PolarCoord(fwd_bearing, distance)


def calculate_bearing_match_of_linestring(linestring: LineString, target_bearing):
    polar_linestrings = convert_cartesian_linestring_to_polar_linestring(linestring)
    weighted_bearing, total_distance = 0, 0
    for segment in polar_linestrings:
        weighted_bearing += abs(segment.distance * cos((180 * pi) * target_bearing - segment.bearing))
        total_distance += segment.distance
    return weighted_bearing / total_distance


def select_nodes_from_node_ids(nodes: List[overpy.Node], node_ids):
    return [node for node in nodes if node.id in node_ids]


def convert_node_list_to_coord_list(node_list):
    return [(node.lon, node.lat) for node in node_list]


def get_all_node_ids_on_way(way: overpy.Way):
    return way._node_ids


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)    
