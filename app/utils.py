def buffer(lat_south, lon_west, lat_north, lon_east):
    pass

import overpy

api = overpy.Overpass()
result_ways = api.query("way(51.1040,0.9455,51.1206,0.9964)['highway'~'(primary|secondary|tertiary)$'];out;")
result_nodes = api.query("way(51.1040,0.9455,51.1206,0.9964)['highway'~'(primary|secondary|tertiary)$'];node(w);out;")

ways = result_ways.ways
nodes = result_nodes.nodes

# way = ways[10]
# print(way)
nodes_in_ways = set()
for way in w:
    try:
        nodes = way._node_ids
        print('found nodes')
        for node in nodes:
            nodes_in_ways.add(node)
    except overpy.exception.DataIncomplete:
        print('Data Incomplete')
        continue    

        