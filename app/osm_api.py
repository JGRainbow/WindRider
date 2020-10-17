import overpy

api = overpy.Overpass()

result_ways = api.query("way(51.0693,0.9103,51.1359,1.1139);out;")


