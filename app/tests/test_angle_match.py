import pytest
import app.tests.test_angle_match_data as data
from app.angle_match2 import (convert_cartesian_coords_to_polar_coords)

# Shapely is (lon, lat)
# geod is (lon, lat)

class TestAngleMatch:

    @pytest.mark.parametrize(*data.test_convert_cartesian_coords_to_polar_coords_data())
    def test_convert_cartesian_coords_to_polar_coords(self, start_coord,
                                                      end_coord,
                                                      expected_polar_coord):
        # Act
        polar_coord = convert_cartesian_coords_to_polar_coords(start_coord, end_coord)
        
        # Assert
        assert polar_coord.bearing == expected_polar_coord.bearing


