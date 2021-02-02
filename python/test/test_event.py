"""
Testing for the Event class.
"""

from typing import List
import common

# NOTE: the method name needs to start with "test" to be recognized
# by the unittest test runner. unittest is from the python standard
# library
def test_thousand_ids_unique():
    """
    Verify the uniqueness of ids generated by EventIdGenerator by
    requesting a thousand ids and checking that they are all distinct.
    """
    generator = common.EventManager()
    events: List[common.Event] = list()
    for _ in range(1000):
        # event without time and pixel, only to check if event's id is unique
        events.append(generator.generate_event(None, None))

    ids = list(map(lambda e: e.get_id(), events))
    # Check if ids as a list contains the same number of elements as
    # ids as a set.
    assert len(ids) == len(set(ids))

def test_return_type():
    """
    Checks if the generator generates EventIds
    """
    one_id = common.EventIdGenerator().new_id()
    assert isinstance(one_id, common.EventId)
#    self.assertIsInstance(
#            one_id,
#            common.EventId,
#            msg="Generated ids should be of type EventId but are of type {}"
#                .format(type(one_id))
#    )
