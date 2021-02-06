"""Event generation."""
import numpy  as np
from common import DetectorGeometry

class OrientationGenerator:
	"""Generates a random orientation to initialize a particle path"""
	def __init__(self, geometry: DetectorGeometry, seed:int):
		"""
		Initialize the random number generator      

		Parameters
		---------
		seed: int
		    Seed for the internal random generator.
		opening angle: float
		    The fixed value for the source specified for the project
		direction:  array
		    The direction along which the source points.
		    Held constant at the positive z-axis line of sight.
		"""
		# store for debug purposes
		self._seed = seed
		# initialize random generator
		self._rng = np.random.default_rng(self._seed)
		self._opening_angle = geometry.source_opening_angle
		self._direction = geometry.source_direction
        
	def generate_random_sphere_vector(self):
		'''Draw a random vector form the spherically symmetric 3D
		normal distribution and normalize to unit length'''
		vector = np.random.normal(size=3)
		normalized_vector = vector / np.linalg.norm(vector)
		return normalized_vector

	def generate_orientation_vector(self):
		'''Generate a random sphere vector and check whether its orientation aligns with that of the opening angle.'''
		while True:
			orientation_vector = self.generate_random_sphere_vector()
			if orientation_vector.dot(self._direction) > np.cos(self._opening_angle):
				return orientation_vector

class PathGenerator:
	"""Generates the path that a single particle takes through the detector."""
	def __init__(self, geometry: DetectorGeometry, samples: int, time_step: float):
		"""
		Set the initial orientation and velocity for a particle path 
	      	ParticlePath.

		Parameters
		----------
		orientation: array
			The initial orientation of the particle drawn
		samples: integer
			The number of time-steps for the particle path as chosen by the user
		time_step: float
			The elapsed time between samples of the path
		"""    
		self._geometry = DetectorGeometry()
		self._orientation_instance = OrientationGenerator(self._geometry, 0)
		self._samples = samples
		self._time_step = time_step

	def generate_velocity(self):
		"""
		Return the initial velocity of the particle stored as a vector
		Because the detector is massless, velocity remains constant
		We are interested in particle physics applications, so
		the particle velocity will be taken to be between 5% and 99%
		the speed of light

		Output
		----------

			velocity: array
		"""
		percentage = np.random.uniform(0.05,0.99)
		speed = 2.99792e8*percentage
		geometry_instance = DetectorGeometry()
		particle_instance = OrientationGenerator(geometry_instance, 0)
		particle_orientation = particle_instance.generate_orientation_vector()
		velocity = speed*particle_orientation
		return velocity
		
	def generate_coordinates(self, samples):
		"""
		Fill in an array of the particle's coordinates for the number
		of samples given
		
		Output
		----------
		coordinates: samples x 3d array
			an array containing the spatial coordinates of the particle
			for the number of samples given
		"""
		# initialize array of the correct shape and number of time steps
		coordinates = np.zeros([samples,3])
		coordinates[0] = self._geometry.source_position
		particle_velocity = self.generate_velocity()
		for index in range(samples - 1):		
#		for index in enumerate(np.arange(0., samples, self._time_step)):
			coordinates[index + 1] = coordinates[index] + particle_velocity*self._time_step
		return coordinates
