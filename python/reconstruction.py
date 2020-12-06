"""
Reconstruction of paths from events.
"""

from common import DetectorGeometry, Event


class ReconstructedPath:
    """
    A single reconstructed path through the Detector.
    """
    def __init__(self):
        pass


class Reconstructor:
    """
    Reconstructs paths from events.
    """
    def __init__(self, geometry: DetectorGeometry):
        pass

    def reconstruct_from_event(self, event: Event) -> ReconstructedPath:
        """
        Reconstruct a single path from a single event.

        Parameters
        ----------
        event:
            The event whose original path is to be reconstructed.
        """
        
    # NOTE: Moved from the generation module
    # REASON: We're assuming minimum deflection (no scattering), so particle paths should be generated
    # as if no detector panels were present
    def intersection_time_with_plane(
            self,
            plane_normal,
            plane_point
            ) -> Optional[float]:  # pylint: disable=unsubscriptable-object
        # TODO: consider exceptions instead of returning None
        """
        Compute intersection of path with a plane.

        Return the point in time, when the ray intersects the given plane.
        Return None if there is no intersection or the intersection time is
        too big.

        Warning
        -------
        This function may return None

        Parameters
        ----------
        plane_normal: 3d numpy array
            The planes normal vector.
        plane_point: 3d numpy array
            Any point on the plane.
        
        Returns
        -------
        float
            The intersection time.
        None
            In case there is no intersection
        """
        # plane specified via one point p and a normal vector n
        # solve the equation (r(t) - p) * n = 0 for t.
        # (t * v - p) * n = 0
        # t * v * n - p * n = 0
        # t = p * n / v * n
        # TODO: handle case where intersection time is very large
        # i.e. denominator very big
        # TODO: check if plan_normal is indeed normalized
        intersection_time = (
            plane_point.dot(plane_normal) / self._velocity.dot(plane_normal)
        )
        if intersection_time < 0:
            # wrong direction
            return None
        return intersection_time
