"""Tests for the "generation" module."""

import numpy  as np # type: ignore
import pytest
import generation
from common import DetectorGeometry

def test_random_sphere_vector():
	"""Test generate_random_sphere_vector to verify that the object 
	normalized_vector is a 3D array with non-zero components and a norm of one."""
	# make instances
	geom_instance = DetectorGeometry()
	o_gen_instance = generation.OrientationGenerator(geom_instance, 0)
	test_vector = o_gen_instance.generate_random_sphere_vector()
	# test assertions
	assert isinstance(test_vector, np.ndarray)
	assert test_vector.shape == (3,)
	for component in test_vector:
		assert component != 0.
	assert np.isclose(np.linalg.norm(test_vector), 1.0)
	
def test_orientation_vector():
	"""Test generate_solid_angle to verify that the x and y components of
	the object orientation_vector are within the opening angle size by
	computing the rejection vector of the projection with the line of sight."""
	geom_instance = DetectorGeometry()
	o_gen_instance = generation.OrientationGenerator(geom_instance, 0)
	opening_angle = geom_instance.source_opening_angle # * np.pi / 180
	line_of_sight = geom_instance.source_direction
	test_orientation = o_gen_instance.generate_orientation_vector()
	cone_radius = np.linalg.norm(test_orientation)*np.tan(opening_angle)
	test_orientation = o_gen_instance.generate_orientation_vector()
	orientation_rejection = test_orientation - test_orientation.dot(line_of_sight)
	assert np.linalg.norm(orientation_rejection) != 0.
	assert np.abs(orientation_rejection[0]) < cone_radius
	assert np.abs(orientation_rejection[1]) < cone_radius

def test_particle_path():
	"""Test"""
	# check that number of samples is sufficient
	# check that orientation found is inside desired interval
	# check that coordinates array is not empty
	# check that generated particle goes through all panes
	# max(map(lambda p: np.linalgo.norm(p.center - geometry.source_position), geometry.panes))

def test_source_on():
	"""Test that the source can generate particle trajectories in a Poisson process"""
	
def test_path_intersections():
	"""Test that particle events are not simultaneously instantiated
	and that particle paths do not intersect each other."""
