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
	orientation: 2-tuple
		The initial orientation of the particle drawn
        velocity: 3-tuple
        	The initial velocity of the particle stored as a vector
        	Because the detector is massless, velocity remains constant
        	So the data type is a tuple
        samples: integer
        	the number of time-steps in a particle trajectory
        """
        
        self._orientation = orientation
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
        # iterate finite difference mesh
        for time_step in np.arange(samples):
        	
        # forgot how to do this
        
        return self._coordinates
        
class GetRandomOrientation:
	"""Create a random orientation to initialize a particle path"""


	opening_angle = 10.0 # fixed degree value specified for project 


    def __init__(self, seed: int):
        """
	Initialize the random number generator      

        Parameters
        ---------
        seed: int
            Seed for the internal random generator.
        """
        # store for debug purposes
        self._seed = seed
        # initialize random generator
        self._rng = numpy.random.default_rng(self._seed)
        
        
    def get_sphere_point(self):
        """Return a random point on the surface of the unit sphere.
        This is a necessary intermediate step to draw a random solid angle."""
        while True:
            # generate random point in the bounding box of the unit sphere
            cube_point = self._rng.uniform(low=-1.0, high=1.0, size=3)
            # check if point lies in the unit sphere
            if numpy.linalg.norm(point_in_cube) < 1:
                # project onto sphere surface i.e. normalize
                sphere_point = (
                )
                return sphere_point
            # try again
            
    def get_solid_angle(sphere_point):
    		# fill in
    		return orientation

#1. orient unit sphere so it's aligned with optical axis
#2. define area of spherical cap subtended by opening angle
#	area = (2*pi*r**2)*(1 - cos(theta))
#	     = 2*pi*(1-cos(opening_angle)) 
#3. draw uniformly distributed random variables u and v from (0,1)
#4. compute
#	theta = 2*pi*u
#	phi = arccos(2*v - 1)
#5. check whether drawn angles are inside spherical cap
#	?
    
    

