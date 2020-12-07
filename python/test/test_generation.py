"""Tests for the "generation" module."""

import numpy  # type: ignore
import pytest
import generation


def test_unifrom_sphere_generator():
    """Verify properties of the generate_random_unit_vector."""
    for _ in range(50):
        point = generation.generate_random_unit_vector()
        # verify it's a numpy array
        assert isinstance(point, numpy.ndarray)
        # verify it's 3d point
        assert point.shape == (3,)
        # verify it's on the surface of the unit sphere
        assert numpy.isclose(numpy.linalg.norm(point), 1)


def test_uniform_solid_angle_generator():
    """Verify properties of the generate_random_solid_angle_vector."""
    opening_angle = 5 / 360 * 2 * numpy.pi
    numpy.array([1, 0, 0]), opening_angle
    for _ in range(50):
        point = generation.generate_random_solid_angle_vector(numpy.array([1, 0, 0]), opening_angle)
        # verify it's a numpy array
        assert isinstance(point, numpy.ndarray)
        # verify it's 3d point
        assert point.shape == (3,)
        # verify it's on the surface of the unit sphere
        assert numpy.isclose(numpy.linalg.norm(point), 1)
        # verify it's in the solid angle
        assert point[0] < numpy.cos(opening_angle)