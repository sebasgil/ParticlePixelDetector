"""Common classes for use in most modules."""
import numpy
from typing import List

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
        """Create a new EventId Generator."""
        self.__counter = 0

    def new_id(self) -> EventId:
        """Return a new unique id."""
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
        """Create a new Event."""
        pass

    def get_id(self) -> EventId:
        """Return the events unique id."""

class DetectorGeometry:
    """
    Information about the detectors geometry.

    This includes the positioning and orientation of all pixels.
    """

    def __init__(self):
        """Create a detector geometry object."""
        self.source_position = numpy.array([0,0,0])
        self.source_direction = numpy.array([0,0,1])
        # 10°
        self.source_opening_angle = 10 / 180 * numpy.pi
        panes = []
        for i in range(5):
            z = 0.3 + i*0.05
            panes.append(Pane(i, z))
        self.panes = panes
        
class Pane:
    """A panel, pane, layer."""

    def __init__(
        self, uid: int, z_offset: float,
        width: float = 0.2, height: float = 0.2,
        n_pixels_x: int = 2000, n_pixels_y: int = 2000
    ):
        """Create a new pane.

        Parameters
        ----------
        uid: int
            A unique id used to refer to this pane.
        z_offset: float
            The panes z-intercept.
        width: float
            The panes width (in the x direction).
        height: float
            The panes height (in the y direction).
        n_pixels_x: int
            The number of (equally spaced) pixels in the x direction.
        n_piyels_x: int
            The number of (equally spaced) piyels in the y direction.
        """
        self.uid = uid
        self.width = width
        self.height = height
        self.z_offset = z_offset
        self.n_pixels_x = n_pixels_x
        self.n_pixels_y = n_pixels_y
        self.center = numpy.array([0, 0, self.z_offset])
        
    def pixels(self):
        """Return all pixels of this pane."""
        pixel_width = self.width / self.n_pixels_x
        pixel_height = self.height / self.n_pixels_y
        lower_left_corner = (
            self.center - numpy.array([self.width/2, self.height/2, 0])
        )
        def pixel_center(n: int, m: int):
            return (
                lower_left_corner + 
                numpy.array([pixel_width/2, pixel_height/2, 0]) +
                numpy.array([n*pixel_width, m*pixel_height, 0])
            )
        
        result = []
        for j in range(self.n_pixels_y):
            for i in range(self.n_pixels_x):
                pixel = Pixel(pixel_center(i,j), self.uid)
                result.append(pixel)
        return result
        
class Pixel:
    """A Pixel belonging to the n_th pane."""
   
    def __init__(self, position, pane_id: int):
        """Create a new pixel.
        Parameters
        ----------
        position : numpy 3d array 
            position of the pixel.
        pane_id: int
            an id which refers to the pane in which the pixel lies (Pane.uid).
        """
        self.pane_id = pane_id
        self.position = position
        
        
        
