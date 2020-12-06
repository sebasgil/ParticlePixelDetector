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
