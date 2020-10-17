import cProfile
from time import perf_counter

import overpy
from tqdm import tqdm

from angle_match import calculate_way_geometry, get_angle_match

SELLINDGE = '(51.0862,0.9360,51.1188,1.0677)'
SMEETH = '(51.1040,0.9455,51.1206,0.9964)'

REGIONS = (SMEETH, SELLINDGE)
REGION = REGIONS[1]

print('Calling API...')
api = overpy.Overpass()
result_ways = api.query(f"way{REGION}['highway'~'(primary|secondary|tertiary)$'];out;")
result_nodes = api.query(f"way{REGION}['highway'~'(primary|secondary|tertiary)$'];node(w);out;")
print('Data received.')

ways = result_ways.ways
nodes = result_nodes.nodes
TARGET_ANGLE = 90
start_time = perf_counter()
for way in tqdm(ways):
    way_geometry = calculate_way_geometry(way, nodes)
    match = get_angle_match(way_geometry, TARGET_ANGLE)
    print(f'Match: {100 * match:0.2f}%')
end_time = perf_counter()
print(f'Analysed {len(ways)} roads in {end_time - start_time:0.2f} seconds.')
