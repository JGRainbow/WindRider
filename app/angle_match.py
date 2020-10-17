import pyproj
from collections import namedtuple
from itertools import tee
import overpy
from typing import List
from numpy import cos, pi


SegmentGeometry = namedtuple('SegmentGeometry', 'angle distance')
GEODESIC = pyproj.Geod(ellps='WGS84')


def calculate_segment_geometry(start_coord, end_coord,
                               geodesic: pyproj.Geod = GEODESIC):
    fwd_bearing, _, distance = geodesic.inv(*start_coord, *end_coord)
    return SegmentGeometry(fwd_bearing, distance)


def calculate_way_geometry_from_coord_list(coord_list, 
                                           geodesic: pyproj.Geod = GEODESIC):
    way_geometry =  [calculate_segment_geometry(start_coord, end_coord)
                          for (start_coord, end_coord) in pairwise(coord_list)]
    return way_geometry


def calculate_way_geometry(way: overpy.Way,
                           nodes: List[overpy.Node],
                           geodesic: pyproj.Geod = GEODESIC):
    node_id_list = get_all_node_ids_on_way(way)
    node_list = select_nodes_from_node_ids(nodes, node_id_list)
    coord_list = convert_node_list_to_coord_list(node_list)
    return calculate_way_geometry_from_coord_list(coord_list, 
                                                  geodesic=geodesic)
       

def get_angle_match(segment_list: List[SegmentGeometry], target_angle):
    weighted_angle, total_distance = 0, 0
    for segment in segment_list:
        weighted_angle += abs(segment.distance * cos((180 / pi) * target_angle - segment.angle))
        total_distance += segment.distance
    return weighted_angle / total_distance


def select_nodes_from_node_ids(nodes: List[overpy.Node], node_ids):
    return [node for node in nodes if node.id in node_ids]


def convert_node_list_to_coord_list(node_list):
    return [(node.lat, node.lon) for node in node_list]


def get_all_node_ids_on_way(way: overpy.Way):
    return way._node_ids


def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)    


if __name__ == '__main__':
    import overpy

    WAY_NUM = 12

    api = overpy.Overpass()
    result_ways = api.query("way(51.1040,0.9455,51.1206,0.9964)['highway'~'(primary|secondary|tertiary)$'];out;")
    result_nodes = api.query("way(51.1040,0.9455,51.1206,0.9964)['highway'~'(primary|secondary|tertiary)$'];node(w);out;")
    ways = result_ways.ways
    nodes = result_nodes.nodes

    way = ways[WAY_NUM]
    way_geometry = calculate_way_geometry(way, nodes)
    print(way_geometry)
    angle_match = get_angle_match(way_geometry, 50)
    print(angle_match)