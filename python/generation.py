# pylint: disable=too-few-public-methods
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
    def __init__(self, origin, velocity):
        self._origin = origin
        self._velocity = velocity

    def get_position_at_time(self, time):
        """
        Get particle position along it's path at a given point in time
        Assuming the particles starts moving at time = 0
        """
        return self._origin + time * self._velocity

    def intersection_time_with_plane(self, plane_normal, plane_point):
        # TODO: consider exceptions instead of returning None
        """
        WARNING: This function may return None

        Return the point in time, when the ray intersects the given plane.
        Return None if there is no intersection or the intersection time is too big.
        """
        # plane specified via one point p and a normal vector n
        # solve the equation (r(t) - p) * n = 0 for t.
        # (t * v - p) * n = 0
        # t * v * n - p * n = 0
        # t = p * n / v * n
        # TODO: handle case where there is no intersection
        #       or intersection time is astronomical
        return plane_point.dot(plane_normal) / self._velocity.dot(plane_normal)

class PathGenerator:
    """
    Randomly generates trajectories for use in event simulation.
    """
    def __init__(self, geometry: DetectorGeometry):
        self._speed_distribution = 1.0
        self._origin_distribution = numpy.array([0.0, 0.0, 0.0])
        # hardcoded seed for now TODO: chan0ge
        self._rng = UniformSolidAngleGenerator(0, geometry.source.direction, geometry.source.opening_angle)
        self._particle_source = geometry.source.position

    def generate_random_path(self) -> ParticlePath:
        """
        Return a randomly generated trajectory through the detector.
        """
        origin = self._generate_random_origin()
        velocity = self._generate_random_speed() * self._rng.generate_random_point()
        return ParticlePath(origin, velocity)

    # random generator for the sake of completeness (?)
    def _generate_random_speed(self) -> float:
        if isinstance(self._speed_distribution, float):
            return self._speed_distribution
        # error
        raise NotImplementedError("Only delta distributions are supported for velocities currently.")

    # random generator for the sake of completeness (?)
    def _generate_random_origin(self) -> float:
        if isinstance(self._origin_distribution, numpy.ndarray) and self._origin_distribution.shape == (3,):
            return self._origin_distribution
        # error
        raise NotImplementedError("Only delta distributions are supported for origins currently.")


##
## RANDOM GENERATORS
##
## using lots of monte carlo because it's fun and simple
##


class UniformSphereGenerator:
    """
    Allows to randomly sample from a uniform distribution on the surface of the unit sphere.
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
            # generate random point in the bounding box of the unit sphere
            point_in_cube = self._rng.uniform(low=-1.0, high=1.0, size=3)
            # check if point lies in the unit sphere
            if numpy.linalg.norm(point_in_cube) < 1:
                # project onto sphere surface i.e. normalize
                point_on_sphere = point_in_cube / numpy.linalg.norm(point_in_cube)
                return point_on_sphere
            # try again

class UniformSolidAngleGenerator:
    """
    Allows to randomly sample from a uniform distribution on a solid
    angle cutout of the surphace of the unit sphere.  Solid angle cutout
    means the region bounded by the spheres surfaces' intersection with a
    cone, whose tip is centered at the spheres center.

    Paramters:
    ----------
    seed: Seed for the random generator
    direction: direction of the solid angles center axis (vector is normalized internally)
    opening_angle: opening angle from center axis to rim of solid angle cutout (0 < opening_angle < 2 PI)
    """
    def __init__(self, seed, direction, opening_angle):
        # check if opening_angle values are ok
        if opening_angle < 0 or opening_angle > 2 * numpy.pi:
            raise ValueError("opening_angle has to be between 0 and 2 PI but is {}.".format(opening_angle))
        if opening_angle > numpy.pi:
            raise NotImplementedError("Given opening_angle {} is greater than PI (180°). Only solid angles smaller than half the sphere work right now.".format(opening_angle))
        self._opening_angle = opening_angle
        # normalize direction
        self._direction = direction / numpy.linalg.norm(direction)
        # initialize inner rng
        self._seed = seed
        self._sphere_rng = UniformSphereGenerator(seed)

    def generate_random_point(self):
        """
        Return a random point in the on the unit sphere surface and inside the solid angle
        """
        while True:
            # random point on the sphere surface
            point_on_sphere = self._sphere_rng.generate_random_point()
            # check if point lies in opening angle, note both point_on_sphere and direction are normalized
            if point_on_sphere.dot(self._direction) < numpy.cos(self._opening_angle):
                # point_on_sphere is good
                return point_on_sphere
            # try again
