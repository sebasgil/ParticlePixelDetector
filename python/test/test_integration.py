"""
Test all components working together.
"""

import pytest
import common
import simulation
import reconstruction


# For now this just serves as an example of how the library is
# intended to be used.
def test_implementated():
    """
    An example of how the program is to be used.

    Will succeed once the most important functions have been
    implemented.
    """
    # Setup
    # a detector geometry, passed to all compoents as configuration
    geometry = common.DetectorGeometry(n_pixels=20)
    # initialize a new event generator
    event_generator = simulation.EventGenerator(geometry)
    # initialize a new event reconstructor with 10 iterations for the internal algorithm
    reconstructor = reconstruction.Reconstructor(10)

    # generate a single event
    event = event_generator.get_random_event() # pylint: disable=assignment-from-no-return
    # reconstruct the originial path
    path = reconstructor.reconstruct_from_event(event) # pylint: disable=assignment-from-no-return

    # Check if the the event and path are not None If they are non,
    # that means the functions that generated them have not yet been
    # implemented and the test fails.
    assert event is not  None
    assert path is not None
