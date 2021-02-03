"""Event generation."""
import numpy  as np
from common import DetectorGeometry

class OrientationGenerator:
    """Generates a random orientation to initialize a particle path"""

    def __init__(self, geometry: DetectorGeometry, seed: int):
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
        """Generate a random sphere vector and check whether its orientation
        aligns with that of the opening angle."""
        while True:
            orientation_vector = self.generate_random_sphere_vector()
            if orientation_vector.dot(self._direction) < np.cos(self._opening_angle  * np.pi/ 180):
                return orientation_vector

class PathGenerator:
    """Generates the path that a single particle takes through the detector."""

    def __init__(self, orientation, velocity, samples):
        """
        Set the initial orientation and velocity for a particle path 
          ParticlePath.

        Parameters
        ----------
    orientation: array
        The initial orientation of the particle drawn
        velocity: array
            The initial velocity of the particle stored as a vector
            Because the detector is massless, velocity remains constant
        samples: integer
            the number of time-steps in a particle trajectory
        """
        
        self._orientation_generator = OrientationGenerator()
        self._velocity = velocity # how is this generated? from where?
        self._samples = samples # how is this generated? from where?

    def generate_coordinates(self, seed):
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
        self.coordinates = np.zeroes([self._samples,3])
        for time_step in np.arange(self._samples):
            self.coordinates[time_step + 1] = self.coordinates[time_step] + np.array(self._velocity)
            # TO-DO: test that this works, especially for final time-steps
        return self.coordinates