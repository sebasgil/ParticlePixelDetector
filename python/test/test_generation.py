"""Tests for the "generation" module."""

import numpy  as np # type: ignore
import pytest
import generation
from common import DetectorGeometry, Pane

# Define class instances required for tests
geom_instance = DetectorGeometry()
o_gen_instance = generation.OrientationGenerator(geom_instance, 0)
trial_samples = 10
trial_time_step = 0.1 # we don't know what this is.
path_instance = generation.PathGenerator(o_gen_instance, 420, trial_samples, trial_time_step)

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
	test_speed = path_instance.generate_velocity().dot(geom_instance.source_direction)
	detector_length = 0.3 + 5*0.5 # hard-coded for now
	assert test_speed*trial_samples > detector_length

def test_path_coordinates():
	"""Test generate_random_path to make sure that a non-empty array is returned and that the
	generated particle passes close enough to the panes to be detectable"""
	# check that coordinates array is not empty
	test_coordinates, _ = path_instance.generate_random_path(trial_samples)
	assert test_coordinates.any() != 0.
	# check that generated particle has enough samples to go close to panes
	# assert
	# max(map(lambda p: np.linalg.norm(p.center - geom_instance.source_position), pane_instance.z_offset))

#def test_source_on():
#	"""Test that the source can generate particle trajectories in a Poisson process"""
	
#def test_path_intersections():
#	"""Test that particle events are not simultaneously instantiated
#	and that particle paths do not intersect each other."""
