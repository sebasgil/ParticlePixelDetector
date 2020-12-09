"""
Common classes for use in most modules.
"""
import numpy

EventId = int

# TODO: employ singleton pattern
class EventIdGenerator:
    """
    Generate event ids.

    Used to generate unique identifiers for events. These unique
    identifiers might be used for example in saving events to external
    storage (e.g. a file, a database).
    """
    def __init__(self):
        self.__counter = 0

    def new_id(self) -> EventId:
        """
        Returns a new unique id.
        """
        # save old counter state, to be returned
        # this ensures the ids start at 0
        new_id = self.__counter
        # increment the counter
        self.__counter += 1
        return new_id

class Event:
    """
    A detector event.

    An event is the result of a single particle passing through the
    detector. It contains all of the detectors measurements.
    """
    def __init__(self):
        pass

    def get_id(self) -> EventId:
        """
        Returns the events unique id.
        """

class DetectorGeometry:
    """
    Information about the detectors geometry.

    This includes the positioning and orientation of all pixels.
    """
    def __init__(self):
        self.source_position = numpy.array([0,0,0])
        self.source_direction = numpy.array([0,0,1])
        # 10°
        self.source_opening_angle = 10 / 180 * numpy.pi

class Pane:
    """
    A panel, pane, layer
    """
    def __init__(
        self, uid: int, z_offset: float,
        width: float = 0.2, height: float = 0.2,
        n_pixels_x: int = 2000, n_pixels_y: int = 2000
    ):
        self.uid = uid
        self.width = width
        self.height = height
        self.z_offset = z_offset
        self.n_pixels_x = n_pixels_x
        self.n_pixels_y = n_pixels_y
        self.center = numpy.array([0, 0, self.z_offset])
