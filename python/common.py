"""Common classes for use in most module."""

# python version > 3.7 is required for this import to work
# it enables postponed evalutation of type annotations
# which is needed for the `-> Pixel` type annotations since
# the Pixel class is defined only at the bottom of the file.
# -> see PEP 563
# It will be standard in upcoming python 3.10
from __future__ import annotations

from typing import List
import numpy  # type: ignore

# type alias for event ids
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
        """Create a new `EventId` generator."""
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

    def get_id(self) -> EventId:
        """Return the events unique id."""


class DetectorGeometry:
    """
    Information about the detectors geometry.

    This includes the positioning and orientation of all pixels.
    """

    # everything is hardcoded for now
    def __init__(self, n_pixels=2000):
        """Create a detector geometry object."""
        self.source_position = numpy.array([0, 0, 0])
        self.source_direction = numpy.array([0, 0, 1])
        # 10°
        self.source_opening_angle = 10 / 180 * numpy.pi
        panes = []
        for i in range(5):
            z = 0.3 + i * 0.05  # pylint: disable=invalid-name
            panes.append(Pane(i, z, n_pixels_x=n_pixels, n_pixels_y=n_pixels))
        self.panes = panes


class Pane:
    """A single panel / pane of pixels.

    Warning
    -------
    The implementation of this class heavily relies on the panes being oriented
    parallel to the xy axis and having their center lie on the z axis of the
    detector coordinate system.
    """

    def __init__(
        self, uid: int, z_offset: float, width: float = 0.2, height: float = 0.2,
        n_pixels_x: int = 2000, n_pixels_y: int = 2000, z_error: float = 0, 
        x_error: float = 0, y_error: float = 0, 
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
            The number of (equally spaced) pixels in the y direction.
        """
        self.uid = uid
        self.width = width
        self.height = height
        self.z_offset = z_offset
        self.n_pixels_x = n_pixels_x
        self.n_pixels_y = n_pixels_y
        self.install_error = numpy.array([x_error, y_error, z_error])
        self.center = numpy.array([0, 0, self.z_offset]) + self.install_error 
    

    def pixels(self) -> List[Pixel]:
        """Return all pixels of this pane.

        Warning
        -------
        This method is very computationally intensive. Use
        `Pane.pixel_positions` instead.

        Returns
        -------
        List[Pixel]
            The list of pixels.
        """
        pixel_width = self.width / self.n_pixels_x
        pixel_height = self.height / self.n_pixels_y
        lower_left_corner = (
            self.center - numpy.array([self.width/2, self.height/2, 0])
        )

        def pixel_center(n: int, m: int):
            # pylint: disable=invalid-name
            return (
                lower_left_corner
                + numpy.array([pixel_width / 2, pixel_height / 2, 0])
                + numpy.array([n * pixel_width, m * pixel_height, 0])
            )

        result = []
        for j in range(self.n_pixels_y):
            for i in range(self.n_pixels_x):
                pixel = Pixel(pixel_center(i, j), self.uid)
                result.append(pixel)
        return result

    def pixel_positions(self):
        # pylint: disable=invalid-name
        """Return a numpy array with all pixel position.

        >>> p = Pane(0, 0, n_pixels_x=5, n_pixels_y=4)
        >>> p.pixel_positions()[0].shape
        (3,)
        >>> p.pixel_positions().shape
        (20, 3)

        Returns
        -------
        numpy array
            All pixel positions in numpy array of shape
            (n_pixels_x * n_pixels_y, 3) which means the positions can be
            accesses by just indexing into this array.
        """
        pixel_width = self.width / self.n_pixels_x
        pixel_height = self.height / self.n_pixels_y
        lower_left_corner = (
            self.center - numpy.array([self.width/2, self.height/2, 0])
        )

        # [0, 1, 2, ... 1999]
        single_row_ns = numpy.arange(self.n_pixels_x)
        # [0, 1, ... 1999, 0, 1, ... 1999 ..... 0, 1, ... 1999]
        #          ------- n_pixels_y times -----
        ns = numpy.repeat(single_row_ns, self.n_pixels_y)

        # [0, 0, 0 ... 0, 1, 1, 1, ... 1, ........  1999, 1999, 1999, ... 1999]
        ms = numpy.concatenate(
            [numpy.full((self.n_pixels_y,), n) for n in range(self.n_pixels_x)]
        )

        xs = ns * pixel_width
        ys = ms * pixel_width
        zs = numpy.zeros(self.n_pixels_x * self.n_pixels_y)

        # [xs
        # ,ys
        # ,zs
        # ]

        # [[0, 0, 0],
        #  [1, 0, 0],
        #  [2, 0, 0]
        #  ... ...
        # ]
        offset_vectors = numpy.array([xs, ys, zs]).T

        return (
            lower_left_corner
            + numpy.array([pixel_width/2, pixel_height/2, 0])
            + offset_vectors
        )

    def get_pixel_from_position(self, position) -> Pixel:
        """Return the pixel at the given position, if there is one.

        Parameters
        ----------
        position: 3d numpy array
            The position whose pixel to return.

        Raises
        ------
        ValueError
            If there is no pixel at the given postion.

        Returns
        -------
        Pixel
            The pixel at the given position.
        """
        # verify the positions actually corresponds to a pixel
        if position in self.pixel_positions():
            return Pixel(position, self.uid)

        raise ValueError(
            "There is no pixel with given position {}".format(position)
        )


class Pixel:
    """A Pixel belonging to a spcific pane."""

    def __init__(self, position, pane_id: int):
        """Create a new pixel.

        Parameters
        ----------
        position : numpy 3d array
            Position of the pixel.
        pane_id: int
            The uid of the pane, which this pixel is a part of.
        """
        self.pane_id = pane_id
        self.position = position
