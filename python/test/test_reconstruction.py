# pylint: disable=invalid-name
"""Testing for the geometry class."""
import numpy as np # type: ignore
import reconstruction as recon
import pytest

# NOTE: the method name needs to start with "test" to be recognized
# by the unittest test runner. unittest is from the python standard
# library

def test_line(): 
    """Find best fit for points on a straight line."""

    # You can test the program with there points that lie on a line passing 
    # through the origin and (1,1,10) 
    
    pixel_info = np.zeros((5,3))

    pixel_info[0,0] = 3.0
    pixel_info[0,1] = 3.0
    pixel_info[0,2] = 30.0
    pixel_info[1,0] = 3.5
    pixel_info[1,1] = 3.5
    pixel_info[1,2] = 35.0
    pixel_info[2,0] = 4.0
    pixel_info[2,1] = 4.0
    pixel_info[2,2] = 40.0
    pixel_info[3,0] = 4.5
    pixel_info[3,1] = 4.5
    pixel_info[3,2] = 45.0
    pixel_info[4,0] = 5.0
    pixel_info[4,1] = 5.0
    pixel_info[4,2] = 50.0

    # start and end point of the line
    start_point = pixel_info[0]
    end_point = pixel_info[-1]

    # caculate centroid "analytically"
    centroid = (start_point + end_point) / 2

    # compare numerically computed centroid to "analytically" computed centroid
    assert (centroid == recon.find_centroid(pixel_info)).all()

    # direction = endpoint - startpoint
    direction_non_normalized = end_point - start_point
    # normalize direction to prepare for comparison
    direction = direction_non_normalized / np.linalg.norm(direction_non_normalized)

    # compare numerically computed direction to "analytically" computed direction
    assert (direction == recon.find_direction(pixel_info, 10)).all()



def test_distance_func(): 
    """tests to determine if distance_func and measure are working alright"""

    assert 0.5 == recon.distance_func(np.array([0.5, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 1.0, 0.0]))
    assert 0.0 == recon.distance_func(np.array([2.0, 2.0, 20.0]), np.array([0.0, 0.0, 0.0]), np.array([1.0, 1.0, 10]))

    pixel_info = np.zeros((5,3))

    #These points (pixel_info) lie on a straight line

    pixel_info[0,0] = 3.0
    pixel_info[0,1] = 3.0
    pixel_info[0,2] = 30.0
    pixel_info[1,0] = 3.5
    pixel_info[1,1] = 3.5
    pixel_info[1,2] = 35.0
    pixel_info[2,0] = 4.0
    pixel_info[2,1] = 4.0
    pixel_info[2,2] = 40.0
    pixel_info[3,0] = 4.5
    pixel_info[3,1] = 4.5
    pixel_info[3,2] = 45.0
    pixel_info[4,0] = 5.0
    pixel_info[4,1] = 5.0
    pixel_info[4,2] = 50.0

    assert 0.0 == recon.distance_func(np.array([2.0, 2.0, 20.0]), recon.find_centroid(pixel_info), recon.find_direction(pixel_info, 10))
    assert 0.0 == recon.measure_error(pixel_info, pixel_info, 10)

    #Another test, this time all the points do not lie on a straight line. 4 of the 5
    # are offset by 0.25 in the +ve and -ve x and y directions 

    pixel_info_2 = np.zeros((5,3))

    #Another test, this time all the points do not lie on a straight line. 4 of the 5
    # are offset by 0.25 in the +ve and -ve x and y directions 

    pixel_info_2[0,0] = 3.25
    pixel_info_2[0,1] = 3.0
    pixel_info_2[0,2] = 30.0
    pixel_info_2[1,0] = 3.5
    pixel_info_2[1,1] = 3.75
    pixel_info_2[1,2] = 35.0
    pixel_info_2[2,0] = 3.75
    pixel_info_2[2,1] = 4.0
    pixel_info_2[2,2] = 40.0
    pixel_info_2[3,0] = 4.5
    pixel_info_2[3,1] = 4.25
    pixel_info_2[3,2] = 45.0
    pixel_info_2[4,0] = 5.0
    pixel_info_2[4,1] = 5.0
    pixel_info_2[4,2] = 50.0

    assert 0.0 != recon.distance_func(pixel_info_2[1], recon.find_centroid(pixel_info_2), recon.find_direction(pixel_info_2, 10))
    assert 0.0 != recon.measure_error(pixel_info_2, pixel_info_2, 10)

    def test_measure_error(): 
        """Simple test to check if measure_error() is working"""

        import numpy as np
        pixel_info = np.zeros((5,3))

        pixel_info[0,0] = 1.0
        pixel_info[0,1] = 0.0
        pixel_info[0,2] = 30.0
        pixel_info[1,0] = np.cos((2/5)*np.pi)
        pixel_info[1,1] = np.sin((2/5)*np.pi)
        pixel_info[1,2] = 35.0
        pixel_info[2,0] = np.cos((4/5)*np.pi)
        pixel_info[2,1] = np.sin((4/5)*np.pi)
        pixel_info[2,2] = 40.0
        pixel_info[3,0] = np.cos((6/5)*np.pi)
        pixel_info[3,1] = np.sin((6/5)*np.pi)
        pixel_info[3,2] = 45.0
        pixel_info[4,0] = np.cos((8/5)*np.pi)
        pixel_info[4,1] = np.sin((8/5)*np.pi)
        pixel_info[4,2] = 50.0

        pixel_info2 = np.zeros((5,3))

        pixel_info2[0,0] = 0.0
        pixel_info2[0,1] = 0.0
        pixel_info2[0,2] = 30.0
        pixel_info2[1,0] = 0.0
        pixel_info2[1,1] = 0.0
        pixel_info2[1,2] = 35.0
        pixel_info2[2,0] = 0.0
        pixel_info2[2,1] = 0.0
        pixel_info2[2,2] = 40.0
        pixel_info2[3,0] = 0.0
        pixel_info2[3,1] = 0.0
        pixel_info2[3,2] = 45.0
        pixel_info2[4,0] = 0.0
        pixel_info2[4,1] = 0.0
        pixel_info2[4,2] = 50.0

        assert 5.0 == recon.measure_error(pixel_info, pixel_info2, 10)

    

    def test_relative_error(): 
        """Simple test to check if relative_error() is working"""

        #These points (pixel_info) lie on a straight line
        pixel_info = np.zeros((5,3))

        pixel_info[0,0] = 3.0
        pixel_info[0,1] = 3.0
        pixel_info[0,2] = 30.0
        pixel_info[1,0] = 3.5
        pixel_info[1,1] = 3.5
        pixel_info[1,2] = 35.0
        pixel_info[2,0] = 4.0
        pixel_info[2,1] = 4.0
        pixel_info[2,2] = 40.0
        pixel_info[3,0] = 4.5
        pixel_info[3,1] = 4.5
        pixel_info[3,2] = 45.0
        pixel_info[4,0] = 5.0
        pixel_info[4,1] = 5.0
        pixel_info[4,2] = 50.0

        assert 0.0 == recon.relative_error(pixel_info, 10)



def test_line_degenerate():
    """Test behaviour on a degenerate line, i.e. a series of identical points."""
    # direction is 0, so all the lines points are the same
    direction = np.array([0., 0., 0.])
    starting_point = np.array([5., 1.23, np.pi])
    pixel_info = create_line_test_case(starting_point, direction, 11)

    # allclose is actually needed here, probably because of the use of np.pi in the starting_point, causing rounding errors
    assert np.allclose(starting_point, recon.find_centroid(pixel_info))

    # see https://docs.pytest.org/en/stable/assert.html about how `pytest.raises` works
    with pytest.raises(ValueError):
        # expect this to fail, rasing a ValueError, since no direction can be found.
        recon.find_direction(pixel_info, 10)

def test_line_two_directions():
    """Test behaviour when the input data consists of multiple lines in different direction."""
    direction_1 = np.array([1., 0., 0.])
    direction_2 = np.array([1.1, 0., 0.])
    starting_point = np.array([0., 0., 0.])
    line_1 = create_line_test_case(starting_point, direction_1, 10)
    line_2 = create_line_test_case(starting_point, direction_2, 10)

    # union of the points of line_1 and line_2
    both_lines = np.concatenate((line_1, line_2))
    assert both_lines.shape == (20, 3)
    
    reconstructed_direction = recon.find_direction(both_lines, 10)

    # the reconstructed direction should lie in between the two lines' directions
    # which leads to two condition

    # first (necessary) condition:
    # this means it should lie in their span (a 2d plane)
    # this means it should be orthogonal to their cross product
    span_normal = np.cross(direction_1, direction_2)
    assert np.dot(reconstructed_direction, span_normal) == 0

    # second (now sufficient) condition: (maybe the first isn't even necessary?)
    # the sum of the two angles that the reconstructed direction makes with the two line directions
    # should be equal to the angle between the two lines' directions

    def angle_between(a, b):
        return np.arccos(
            np.dot(a, b)
            / np.linalg.norm(a)
            / np.linalg.norm(b)
        )

    angle_1 = angle_between(reconstructed_direction, direction_1)
    angle_2 = angle_between(reconstructed_direction, direction_1)
    angle_between_1_and_2 = angle_between(direction_1, direction_2)
    assert angle_1 + angle_2 == angle_between_1_and_2


def test_inconvenient_line():
    """Due to the peculiarites in how the starting_value of the iterative reconstruction algorithm is defined it might fail when the line is pointing in a specific direction"""
    # lines that go only in x, y, z direction respectively
    x_line = create_line_test_case(np.zeros(3), np.array([1, 0, 0]), 10)
    y_line = create_line_test_case(np.zeros(3), np.array([0, 1, 0]), 10)
    z_line = create_line_test_case(np.zeros(3), np.array([0, 0, 1]), 10)

    assert np.isfinite(recon.find_direction(x_line, 10)).all()
    assert np.isfinite(recon.find_direction(y_line, 10)).all()
    assert np.isfinite(recon.find_direction(z_line, 10)).all()


def create_line_test_case(starting_point, direction, number_of_points):
    """Create a bunch of evenly spaced points along a line to use as test cases."""
    pixel_info = np.array([starting_point + (direction * i) for i in range(number_of_points)])
    assert pixel_info.shape == (number_of_points, 3)
    return pixel_info