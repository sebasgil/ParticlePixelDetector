# pylint: disable=too-few-public-methods
"""Event generation."""
from typing import Optional
import numpy  # type: ignore
from common import DetectorGeometry


class ParticlePath:
    """A single path that a particle takes through the detector."""

    def __init__(self, origin, velocity):
        """
        Create an instance of ParticlePath.

        Parameters
        ----------
        origin: 3d numpy array
            The Starting point of the particles path.
        velocity: 3d numpy array
            The partitcles velocity.
        """
        self._origin = origin
        self._velocity = velocity

    def get_position_at_time(self, time):
        """
        Get particle position along its path at a given point in time.

        Assuming the particles starts moving at time = 0
        """
        return self._origin + time * self._velocity


class PathGenerator:
    """Randomly generates trajectories for use in event simulation."""

    def __init__(self, geometry: DetectorGeometry):
        """Create an instance of PathGenerator.
        
        Parameters
        ----------
        geometry: DetectorGeometry
            Information about the detectors geometry, most importantly the position of the particle source.
        """
        # position of the particle source
        self._particle_source_position = geometry.source.position
        # mean direction of particles (center of the solid angle)
        self._particle_source_direction = geometry.source.direction
        # opening angle of the solid angle
        self._particle_source_opening_angle = geometry.source.opening_angle

    def generate_random_path(self) -> ParticlePath:
        """Return a randomly generated trajectory through the detector."""
        origin = self._particle_source_position
        velocity = generate_random_solid_angle_vector(
            self._particle_source_direction,
            self._particle_source_opening_angle
        )
        return ParticlePath(origin, velocity)

#
# RANDOM GENERATORS
#

def generate_random_unit_vector():
    # draw a random vector from the 3d normal distribution
    # which is spherically symmetric
    point = numpy.random.normal(size=3)
    # normalize the the vector to obtain a point on the unit sphere
    normalized_point = point / numpy.linalg.norm(point)
    return normalized_point

def generate_random_solid_angle_vector(direction, opening_angle):
    # TODO: validate parameters, omitted for simplicity
    while True:
        # generate a random point ont the unit sphere
        random_unit_vector = generate_random_unit_vector()
        # check if the point lies within the specified solid angle
        # dot product of two vectors = cos(angle between the two)
        if random_unit_vector.dot(direction) < numpy.cos(opening_angle):
            return random_unit_vector