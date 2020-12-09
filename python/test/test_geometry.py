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

def test_pane():
    """
    Test properties of the detector panes.
    """
    p = common.Pane(0, 0.3)
    is_int(p.uid)
    is_float(p.width)
    is_float(p.height)
    is_float(p.z_offset)
    is_int(p.n_pixels_x)
    is_int(p.n_pixels_y)
    is3d(p.center)

def is_float(f):
    assert isinstance(f, float)

def is_int(f):
    assert isinstance(f, int)

def is3d(a):
    assert isinstance(a, numpy.ndarray)
    assert a.shape == (3,)