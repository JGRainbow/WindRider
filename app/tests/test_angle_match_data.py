from collections import namedtuple

from pytest import param
from shapely.geometry import LineString
import pyproj

# (Lon, Lat)

PolarCoord = namedtuple('PolarCoord', 'bearing distance')

def test_convert_cartesian_coords_to_polar_coords_data():
    test_variables = "start_coord, end_coord, expected_polar_coord"
    test_data = [
        param(
            (0, 0),
            (0, 1),
            PolarCoord(0, 1),
            id='North Line'
        ),
        param(
            (0, 0),
            (1, 0),
            PolarCoord(90, 1),
            id='East Line'
        ),
        param(
            (0, 0),
            (0, -1),
            PolarCoord(180, 1),
            id='South Line'
        ),
        param(
            (0, 0),
            (-1, 0),
            PolarCoord(270, 1),
            id='West Line'
        )
    ]
    return test_variables, test_data


