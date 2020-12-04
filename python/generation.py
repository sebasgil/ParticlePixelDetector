"""
Event generation.
"""
import numpy
from common import DetectorGeometry

# functional description?
class ParticlePath:
    """
    A single path that a particle takes through the detector.
    """
    def __init__(self):
        pass


class PathGenerator:
    """
    Randomly generates trajectories for use in event simulation.
    """
    def __init__(self, geometry: DetectorGeometry):
        pass

    def generate_random_path(self) -> ParticlePath:
        """
        Return a randomly generated trajectory through the detector.
        """
class UniformSphereGenerator:
    """
    Allows to randomly sample from a uniform distribution on the unit
    sphere.
    """
    def __init__(self, seed):
        # store for debug purposes
        self._seed = seed
        # initialize random generator
        self._rng = numpy.random.default_rng(self._seed)

    def generate_random_point(self):
        """
        Return a random point on the surface of the unit sphere.
        """
        while True:
            # generate random point in the unit cube
            point_in_cube = self._rng.uniform(low=0.0, high=1.0, size=3)
            # check if point lies in the unit sphere
            if numpy.linalg.norm(point_in_cube) < 1:
                # project onto sphere surface i.e. normalize
                point_on_sphere = point_in_cube / numpy.linalg.norm(point_in_cube)
                return point_on_sphere
