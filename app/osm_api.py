import overpy


def get_road_ways_from_bbox(lat_south,
                            lon_west,
                            lat_north,
                            lon_east):
    api = overpy.Overpass()
    result_ways = api.query(f"way({lat_south},{lon_west},{lat_north},{lon_east})['highway'~'(primary|secondary|tertiary)$'];out;")
    return result_ways.ways


def get_road_nodes_from_bbox(lat_south,
                             lon_west,
                             lat_north,
                             lon_east):
    api = overpy.Overpass()
    result_nodes = api.query(f"way({lat_south},{lon_west},{lat_north},{lon_east})['highway'~'(primary|secondary|tertiary)$'];node(w);out;")
    return result_nodes.nodes


def create_output_json():
    pass
