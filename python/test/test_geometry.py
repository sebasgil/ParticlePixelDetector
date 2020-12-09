# pylint: disable=invalid-name
"""Testing for the geometry class."""
import numpy
import common


# NOTE: the method name needs to start with "test" to be recognized
# by the unittest test runner. unittest is from the python standard
# library
def test_geometry():
    """Test properties of the particle source."""
    g = common.DetectorGeometry()
    # test if source_postion is a numpy array
    assert isinstance(g.source_position, numpy.ndarray)
    # test if source_position is a 3d array
    assert g.source_position.shape == (3,)
    assert isinstance(g.source_direction, numpy.ndarray)
    assert g.source_direction.shape == (3,)
    assert numpy.linalg.norm(g.source_direction) == 1
    assert isinstance(g.source_opening_angle, float)
    assert isinstance(g.panes, list)
    for pane in g.panes:
        assert isinstance(pane, common.Pane)


def test_pane():
    """Test properties of the detector panes."""
    p = common.Pane(0, 0.3)
    is_int(p.uid)
    is_float(p.width)
    is_float(p.height)
    is_float(p.z_offset)
    is_int(p.n_pixels_x)
    is_int(p.n_pixels_y)
    is3d(p.center)


def test_pixel():
    """Test properties of the pixel."""
    p = common.Pixel(numpy.array([5, 1, 8.3]), 0)
    is3d(p.position)
    is_int(p.pane_id)


def test_pixel_list():
    """Test the pixels function on Pane."""
    p = common.Pane(0, 0.3, n_pixels_x=20, n_pixels_y=20)
    pixels = p.pixels()
    assert isinstance(pixels, list)
    assert isinstance(pixels[0], common.Pixel)


def test_pixel_array():
    """Test the pixel_positions function on Pane."""
    p = common.Pane(0, 0.3)
    pixel_positions = p.pixel_positions()
    assert isinstance(pixel_positions, numpy.ndarray)
    assert pixel_positions.shape == (4_000_000, 3)


def is_float(f):
    """Assert that the argument is a floating point number."""
    assert isinstance(f, float)


def is_int(f):
    """Assert that the argument is an integer."""
    assert isinstance(f, int)


def is3d(a):
    """Assert that the argument is a 3d numpy array.

    i.e. a valid point in the detector coordinate system.
    """
    assert isinstance(a, numpy.ndarray)
    assert a.shape == (3,)
