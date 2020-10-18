# import cProfile
# from time import perf_counter

import overpy
# from tqdm import tqdm

# from angle_match import calculate_way_geometry, get_angle_match

# SELLINDGE = '(51.0862,0.9360,51.1188,1.0677)'
# SMEETH = '(51.1040,0.9455,51.1206,0.9964)'

# REGIONS = (SMEETH, SELLINDGE)
# REGION = REGIONS[1]

# print('Calling API...')
# api = overpy.Overpass()
# result_ways = api.query(f"way{REGION}['highway'~'(primary|secondary|tertiary)$'];out;")
# result_nodes = api.query(f"way{REGION}['highway'~'(primary|secondary|tertiary)$'];node(w);out;")
# print('Data received.')

# ways = result_ways.ways
# nodes = result_nodes.nodes
# TARGET_ANGLE = 90
# start_time = perf_counter()
# for way in tqdm(ways):
#     way_geometry = calculate_way_geometry(way, nodes)
#     match = get_angle_match(way_geometry, TARGET_ANGLE)
#     print(f'Match: {100 * match:0.2f}%')
# end_time = perf_counter()
# print(f'Analysed {len(ways)} roads in {end_time - start_time:0.2f} seconds.')


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


def get_road_ways_json_from_bbox(lat_south,
                                 lon_west,
                                 lat_north,
                                 lon_east):
    api = overpy.Overpass()
    result_ways = api.query(f"way({lat_south},{lon_west},{lat_north},{lon_east})['highway'~'(primary|secondary|tertiary)$'];out;")
    pass


# api = overpy.Overpass()
# result = api.query("[out:json];node(50.745,7.17,50.75,7.18);out;")
# # result_ways = api.query(f"[out:json];way(51.1040,0.9455,51.1206,0.9964)['highway'~'(primary|secondary|tertiary)$'];out;")
# # result = api.parse_json(r'https://www.overpass-api.de/api/interpreter?data=[out:json];node[highway=speed_camera](43.46669501043081,-5.708215989569187,43.588927989569186,-5.605835010430813);out%20meta;')
# result.nodes
import requests

api = overpy.Overpass()
url = r"https://www.overpass-api.de/api/interpreter?data=[out:json];way(51.1040,0.9455,51.1206,0.9964)['highway'~'(primary|secondary|tertiary)$'];out;"
response = requests.get(url)
json = response.json()
print(len(json))
