"""testing for the geometry class"""
from typing import List
import common
import numpy

# NOTE: the method name needs to start with "test" to be recognized
# by the unittest test runner. unittest is from the python standard
# library
def test_source():
    """

    """
    g = common.DetectorGeometry()
    assert isinstance(g.source_position, numpy.ndarray)

