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


def convert_cartesian_coords_to_polar_coords(start_coord, end_coord,
                                             geodesic: pyproj.Geod = GEODESIC):
    fwd_bearing, _, distance = geodesic.inv(*start_coord, *end_coord)
    return PolarCoord(fwd_bearing % 360, distance)
