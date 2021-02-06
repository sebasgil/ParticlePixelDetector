"""Tests for the "generation" module."""

import numpy  as np # type: ignore
import pytest
import generation
from common import DetectorGeometry, Pane

# Define class instances required for tests
geom_instance = DetectorGeometry()
o_gen_instance = generation.OrientationGenerator(geom_instance, 0)
test_samples = 10
path_instance = generation.PathGenerator(o_gen_instance, test_samples)

def test_random_sphere_vector():
	"""Test generate_random_sphere_vector to verify that the object 
	normalized_vector is a 3D array with non-zero components and a norm of one."""
	test_vector = o_gen_instance.generate_random_sphere_vector()
	assert isinstance(test_vector, np.ndarray)
	assert test_vector.shape == (3,)
	for component in test_vector:
		assert component != 0.
	assert np.isclose(np.linalg.norm(test_vector), 1.0)
	
def test_orientation_vector():
	"""Test generate_solid_angle to verify that the x and y components of
	the object orientation_vector are within the opening angle size."""
	opening_angle = geom_instance.source_opening_angle
	test_orientation = o_gen_instance.generate_orientation_vector()
	assert test_orientation[0] < np.cos(opening_angle)
	assert test_orientation[1] < np.sin(opening_angle)
	
def test_particle_velocity():
	"""Test generate_speed to ensure the number of samples at a given speed
	is enough to reach the end of the detector."""
	test_orientation = o_gen_instance.generate_orientation_vector()
	test_speed = path_instance.generate_velocity(test_samples).dot(geom_instance.source_direction)
	detector_length = 0.3 + 5*0.5
	assert test_speed*test_samples > detector_length

def test_path_coordinates():
	"""Test bla"""
	# check that coordinates array is not empty
	test_coordinates = path_instance.generate_coordinates(test_samples)
	assert test_coordinates.any() != 0.
	# check that generated particle goes through all panes
	# max(map(lambda p: np.linalg.norm(p.center - geom_instance.source_position), pane_instance.z_offset))

def test_source_on():
	"""Test that the source can generate particle trajectories in a Poisson process"""
	
def test_path_intersections():
	"""Test that particle events are not simultaneously instantiated
	and that particle paths do not intersect each other."""
