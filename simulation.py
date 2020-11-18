"""
Simulation of events.
"""

from common import Event, DetectorGeometry

class EventGenerator:
    """
    Randomly generates events.
    """
    def __init__(self, geometry: DetectorGeometry):
        pass

    def get_random_event(self) -> Event:
        """Return an randomly generated Event."""
