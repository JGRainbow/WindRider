# from osm_api import get_road_nodes_from_bbox, get_road_ways_from_bbox
# from app import get_all_node_ids_on_way, convert_node_list_to_coord_list, select_nodes_from_node_ids
from typing import List

from shapely.geometry import LineString
import overpy

from geojson import Feature, FeatureCollection

# nodes = get_road_nodes_from_bbox(51.1040,0.9455,51.1206,0.9964)
# ways = get_road_ways_from_bbox(51.1040,0.9455,51.1206,0.9964)


# way = ways[10]

def create_linestring_from_way(way: overpy.Way, nodes):
    node_id_list = get_all_node_ids_on_way(way)
    node_list = select_nodes_from_node_ids(nodes, node_id_list)
    coord_list = convert_node_list_to_coord_list(node_list)
    linestring = LineString(coord_list)
    return linestring


# l = create_linestring_from_way(way, nodes)

def create_feature_collection(ways, nodes, crs="EPSG:4326"):
    features = []
    for way in ways:
        linestring = create_linestring_from_way(way, nodes)
        feature = Feature(geometry=linestring)
        features.append(feature)
    fc = FeatureCollection(features, crs=crs)
    return fc

# fc = create_feature_collection(ways, nodes)
# print(fc)



def select_nodes_from_node_ids(nodes: List[overpy.Node], node_ids):
    return [node for node in nodes if node.id in node_ids]


def convert_node_list_to_coord_list(node_list):
    return [(node.lon, node.lat) for node in node_list]


def get_all_node_ids_on_way(way: overpy.Way):
    return way._node_ids
