"""Tests for the "generation" module."""

import numpy  # type: ignore
import pytest
import generation


def test_unifrom_sphere_generator():
    """Verify properties of the UniformSphereGenerator."""
    rng = generation.UniformSphereGenerator(0)
    for _ in range(50):
        point = rng.generate_random_point()
        # verify it's a numpy array
        assert isinstance(point, numpy.ndarray)
        # verify it's 3d point
        assert point.shape == (3,)
        # verify it's on the surface of the unit sphere
        assert numpy.isclose(numpy.linalg.norm(point), 1)


def test_uniform_solid_angle_generator():
    """Verify properties of the UniformSolidAngleGenerator."""
    opening_angle = 5 / 360 * 2 * numpy.pi
    rng = (
        generation.UniformSolidAngleGenerator(
            0, numpy.array([1, 0, 0]), opening_angle
        )
    )
    for _ in range(50):
        point = rng.generate_random_point()
        # verify it's a numpy array
        assert isinstance(point, numpy.ndarray)
        # verify it's 3d point
        assert point.shape == (3,)
        # verify it's on the surface of the unit sphere
        assert numpy.isclose(numpy.linalg.norm(point), 1)
        # verify it's in the solid angle
        assert point[0] < numpy.cos(opening_angle)

    #
    # TEST CASES with initialization errors
    #

    # opening angles out of range
    for invalid_angle in [-5, 10, 7, numpy.inf]:
        with pytest.raises(ValueError):
            rng = (
                generation.UniformSolidAngleGenerator(
                    0, numpy.array([1, 0, 0]), invalid_angle
                )
            )

    # direction vectors to small to be normalized
    for small_number in [0, 5e-324]:
        with pytest.raises(ValueError):
            rng = (
                generation.UniformSolidAngleGenerator(
                    0, numpy.array([small_number, 0, 0]), 1
                )
            )


def test_path_plane_intersection_good():
    """Test path and plane intersection algorithm."""
    #
    # TEST CASES with an intersection
    #

    # xy-plane with z offset of 10
    plane_normal = numpy.array([0, 0, 1])
    plane_point = numpy.array([0, 0, 10])
    # path from in z direction with unit velocity
    path_origin = numpy.array([0, 0, 0])
    path_velocity = numpy.array([0, 0, 1])
    path = generation.ParticlePath(path_origin, path_velocity)
    intersection_time = (
        path.intersection_time_with_plane(plane_normal, plane_point)
    )
    assert intersection_time is not None
    intersection_point = path.get_position_at_time(intersection_time)
    assert intersection_point is not None
    assert (
        numpy.all(
            numpy.isclose(intersection_point, numpy.array([0, 0, 10]))
        )
    )

    #
    # TEST CASES with no intersection
    #

    # xy-plane with z offset of 10
    plane_normal = numpy.array([0, 0, 1])
    plane_point = numpy.array([0, 0, 10])
    # path from in z direction with unit velocity
    path_origin = numpy.array([0, 0, 0])
    # negative velocity -> no intersection
    path_velocity = numpy.array([0, 0, -1])
    path = generation.ParticlePath(path_origin, path_velocity)
    intersection_time = (
        path.intersection_time_with_plane(plane_normal, plane_point)
    )
    assert intersection_time is None


def test_path_generator():
    """Test the PathGenerator class, which has a public interface."""
    # pylint: disable=too-few-public-methods,missing-class-docstring
    class MockGeometry:
        """Small part of DetectorGeometry, for testing purposes."""

        def __init__(self, position, direction, opening_angle):
            class Source:
                def __init__(self):
                    pass
            self.source = Source()
            self.source.position = position
            self.source.direction = direction
            self.source.opening_angle = opening_angle

    geom = (
        MockGeometry(
            numpy.array([0, 0, 0]),
            numpy.array([0, 0, 1]),
            5 / 360 * 2 * numpy.pi
        )
    )
    gen = generation.PathGenerator(geom)
    path = gen.generate_random_path()

    # xy-plane with z offset of 10
    plane_normal = numpy.array([0, 0, 1])
    plane_point = numpy.array([0, 0, 10])
    intersection_time = (
        path.intersection_time_with_plane(plane_normal, plane_point)
    )
    print(intersection_time)
