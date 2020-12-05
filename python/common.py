"""
Common classes for use in most modules.
"""

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
        pass
