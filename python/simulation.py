"""
Simulation of events.
"""

import numpy as np
from scipy.spatial.distance import cdist  # package to calculate the euclidean distance

from common import EventFactory, DetectorGeometry, Pixel
from generation import PathGenerator

class EventGenerator:
    """
    Randomly generates events.

    Used to generates a random path with help of PathGenerator and calculate
    the intersection of this path with the detector panes.

    Initial parameters
    ----------
    geometry: the DetectorGeometry class, which includes the information about the detector
    panes.
    """
    def __init__(self, geometry: DetectorGeometry):
        self.geometry = geometry
        self.panes = self.geometry.panes
        self.path_generator = PathGenerator(geometry, geometry.source_speed, 'auto', 'auto')
        self.event_factory = EventFactory()

    def get_random_event(self):
        """Does the main simulation work. It calculates the intersection points,
       validates them and returns a list of triggered pixels.
       """
        particle_path, time_path = self._generate_random_path()
        # TODO: remove
        # print("particle_path: {}".format(particle_path))

        # arrays for storing the hits' data
        activation_times = np.array([])
        pixel_positions = []

        for pane in self.panes:
            pane_pixel_positions = pane.pixel_positions()
            intersection_idxs = self._search_for_intersections(particle_path, pane_pixel_positions)

            pane_intersection_point = pane_pixel_positions[intersection_idxs[1]]
            path_intersection_point = particle_path[intersection_idxs[0]]
            intersection_time: float = time_path[intersection_idxs[0]]

            triggered_pixel = pane.get_pixel_from_position(pane_intersection_point)
            heuristic_max_pixel_radius = pane.heuristic_max_pixel_radius

            if self._check_if_intersection_valid(path_intersection_point, triggered_pixel, heuristic_max_pixel_radius):
                # hit is valid save activation time and pixel position
                # TODO: improve performance: np.append always copies the array
                activation_times = np.append(activation_times, intersection_time)
                pixel_positions.append(path_intersection_point)

        event = self.event_factory.new_event(activation_times, np.array(pixel_positions))
        return event


    def _check_if_intersection_valid(self, path_intersection_point, pixel: Pixel, max_radius):
        dist = np.linalg.norm(path_intersection_point - pixel.position)
        # TODO: remove
        # if dist > max_radius:
        #     print("intersection invalid:")
        #     print("path_intersection_point: ", path_intersection_point)
        #     print("pixel position:", pixel.position)
        #     print("max_radius: ", max_radius)
        # else:
        #     print("intersection valid")
        return dist <= max_radius

    def _search_for_intersections(self, detector_pane, random_path):
        """Calculates the euclidean distance for each point of the particle path and returns the indicies
        of the points with the minimal distance (for the path and for the pane)

        Parameters
        ----------
        detector_pane: the whole span of detector pane coordinates
        random_path: the path of the particle
        """
        dist = cdist(detector_pane, random_path, metric='euclidean')
        min_dist_index = np.unravel_index(dist.argmin(), dist.shape)  # find the pixel pair with min. distance
        return min_dist_index

    def _generate_random_path(self):
        """Generates the random path by means of the PathGenerator class

        Return
        ----------
        partical_path: the physical randomly generated path
        time_path: the time sequence for the path
        """
        particle_path, time_path = self.path_generator.generate_random_path()
        return particle_path, time_path
