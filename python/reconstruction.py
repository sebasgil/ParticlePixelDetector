"""
Reconstruction of paths from events.
"""

import numpy as np
from common import DetectorGeometry, Event


class ReconstructedPath:
    """
    A single reconstructed path through the Detector.
    """
    def __init__(self, event_id, direction, centeroid):
        self.event_id = event_id
        self.direction = direction
        self.centeroid = centeroid


class Reconstructor:
    """
    Reconstructs paths from events.
    """
    def __init__(self, number_of_iterations):
        self.number_of_iterations = number_of_iterations

    def reconstruct_from_event(self, event: Event) -> ReconstructedPath:
        """
        Reconstruct a single path from a single event.

        Parameters
        ----------
        # TODO: wording
        event: The event whose original path is to be reconstructed.
        """
        reconstructed_path = ReconstructedPath(
            event.get_id(),
            find_direction(
                event.activated_pixel_positions(),
                self.number_of_iterations
            ),
            find_centroid(event.activated_pixel_positions())
        )

        return reconstructed_path


def find_centroid(pixel_info):  # returns centroid
    centroid = np.mean(pixel_info, axis=0)
    return centroid


def find_direction(pixel_info, number_of_iterations):  # returns direction
    centroid = find_centroid(pixel_info)
    direction = np.array([1.0, 0.0, 0.0])
    for _ in range(number_of_iterations):
        next_direction = np.array([0.0, 0.0, 0.0])

        for point in pixel_info:
            point_vec = point - centroid

            dot = np.dot(direction, point_vec)

            next_direction += dot*point_vec

        norm = np.dot(next_direction, next_direction)

        direction = (1/(norm**(0.5)))*next_direction

    return direction


def distance_func(point, point_on_line, dcs_of_line):
    centroid = point_on_line  # any point on the line
    direction = dcs_of_line  # direction cosines of the line
    vector_to_centroid = centroid - point
    area_of_parallelogram = np.cross(vector_to_centroid, direction)

    distance = (
        np.dot(area_of_parallelogram, area_of_parallelogram)
        / np.dot(direction, direction)
    )

    distance = (abs(distance))**(0.5)

    return distance


def measure(pixel_info):
    sum_distances = 0.0
    for point in pixel_info:
        sum_distances += distance_func(
            point,
            find_centroid(pixel_info),
            find_direction(pixel_info, 10)
        )

    return sum_distances
