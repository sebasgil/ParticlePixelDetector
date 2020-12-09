"""testing for the geometry class"""
from typing import List
import common
import numpy

# NOTE: the method name needs to start with "test" to be recognized
# by the unittest test runner. unittest is from the python standard
# library
def test_source():
    """
    Test properties of the particle source
    """
    g = common.DetectorGeometry()
    # test if source_postion is a numpy array
    assert isinstance(g.source_position, numpy.ndarray)
    # test if source_position is a 3d array
    assert g.source_position.shape == (3,)
    assert isinstance(g.source_direction, numpy.ndarray)
    assert g.source_direction.shape == (3,)
    assert numpy.linalg.norm(g.source_direction) == 1
    assert isinstance(g.source_opening_angle, float)