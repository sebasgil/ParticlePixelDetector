"""Tests for the "generation" module."""

import numpy  as np # type: ignore
import pytest
import generation

def test_random_sphere_vector():
	"""Docstring"""
	# check it has non-zero components
	# check it's normalized
	# check it's on sphere surface
	
def test_solid_angle():
	"""Docstring"""
	# check while loop terminates
	# check that vector is inside desired interval
	# check that an Exception is raised for wrong vectors

def test_particle_path():
	"""Docstring"""
	# check that orientation found is inside desired interval
	# check that coordinates array is not empty
	# check that generated particle goes through all panes
