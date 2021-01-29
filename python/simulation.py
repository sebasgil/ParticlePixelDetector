"""
Simulation of events.
"""

import numpy as np
from scipy.spatial.distance import cdist  # package to calculate the euclidean distance

from common import EventGenerator, EventIdGenerator, DetectorGeometry, Pixel
from gerenation import PathGenerator

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

        self.EventGenerator = self.common.EventManager()

    def simulate(self):
        """Does the main simulation work. It calculates the intersection points,
       validates them and returns a list of triggered pixels.
       """
        particle_path, time_path = self.generate_random_path()
        events = []

        for pane in self.panes:
            pane_pixel_positions = pane.pixel_positions()
            intersection_idxs = self.search_for_intersections(particle_path, pane_pixel_positions)

            pane_intersection_point = pane_pixel_positions[intersection_idxs[0]]
            path_intersection_point = particle_path[intersection_idxs[1]]
            intersection_time = time_path[intersection_idxs[1]]

            triggered_pixel = pane.get_pixel_from_position(pane_intersection_point)
            if self.check_if_intersection_valid(pane_intersection_point, triggered_pixel):

                event = self.EventGenerator.generate_event(triggered_pixel, intersection_time)
                events.append(event)

            return events


    def check_if_intersection_valid(self, pane_intersection_point, pixel: Pixel):
        """
        Forgot how we were going to do it
        """
        return True

    def search_for_intersections(self, detector_pane, random_path):
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

    def generate_random_path(self):
        """Generates the random path by means of the PathGenerator class

        Return
        ----------
        partical_path: the physical randomly generated path
        time_path: the time sequence for the path
        """
        particle_path, time_path = PathGenerator.generate_random_path()
        return particle_path, time_path
