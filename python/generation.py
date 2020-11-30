"""
Event generation.
"""
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
