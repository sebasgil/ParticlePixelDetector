"""Event generation."""
import numpy  as np


class ParticlePath:
    """The path that a single particle takes through the detector."""

    def __init__(self, orientation, velocity, samples):
        """
        Set the initial orientation and velocity for a particle path 
      	ParticlePath.

        Parameters
        ----------
	orientation: 3-tuple
		The initial orientation of the particle drawn
        velocity: 3-tuple
        	The initial velocity of the particle stored as a vector
        	Because the detector is massless, velocity remains constant
        	So the data type is a tuple
        samples: integer
        	the number of time-steps in a particle trajectory
        """
        
        self._orientation = GetOrientation.get_solid_angle()
        self._velocity = velocity
	self._samples = samples


    def get_coordinates(self, seed):
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
        self._coordinates = np.zeroes([samples,3])
        for time_step in np.arange(samples):
            self._coordinates[time_step + 1] = self._coordinates[time_step] + np.array(self._velocity)
            # TO-DO: test that this works, especially for final time-steps
        
        return self._coordinates
        
class GetOrientation:
	"""Create a random orientation to initialize a particle path"""


    def __init__(self, seed: int):
        """
	Initialize the random number generator      

        Parameters
        ---------
        seed: int
            Seed for the internal random generator.
        opening angle: float
            The fixed value for the source specified for the project
        direction:  3-tuple
            The direction along which the source points.
            Held constant at the positive z-axis line of sight.
            TO-DO: Should this be subsumed under Geometry?
        """s
        # store for debug purposes
        self._seed = seed
        # initialize random generator
        self._rng = numpy.random.default_rng(self._seed)
        self._opening_angle = 10.0
        self._direction = (0.,0.,1.0)
        
        
    def get_random_sphere_vector():
        '''Draw a random vector form the spherically symmetric 3D
	normal distribution and normalize to unit length'''
	vector = np.random.normal(size=3)
	normalized_vector = vector / np.linalg.norm(vector)
	return normalized_vector

    def get_solid_angle(direction, opening_angle):
	 '''Generate a random sphere vector and check whether its orientation
	 aligns with that of the opening angle.'''
	 opening_angle  = 10.0
	 direction = np.array([0.,0.,1.0])
	     while True:
		solid_angle = get_random_sphere_vector()
		if solid_angle.dot(self._direction) < np.cos(self._opening_angle): # note that the second is -0.83; is this a problem?
		    return random_unit_vector

    

