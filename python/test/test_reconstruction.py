# pylint: disable=invalid-name
"""Testing for the geometry class."""
import numpy as np # type: ignore
import reconstruction as recon

# NOTE: the method name needs to start with "test" to be recognized
# by the unittest test runner. unittest is from the python standard
# library


#def test_geometry():
#    """Test properties of the particle source."""
#    g = common.DetectorGeometry()
#    # test if source_postion is a numpy array
#    assert isinstance(g.source_position, numpy.ndarray)
#    # test if source_position is a 3d array
#    assert g.source_position.shape == (3,)
#    assert isinstance(g.source_direction, numpy.ndarray)
#    assert g.source_direction.shape == (3,)
#    assert numpy.linalg.norm(g.source_direction) == 1
#    assert isinstance(g.source_opening_angle, float)
#    assert isinstance(g.panes, list)
#    for pane in g.panes:
#        assert isinstance(pane, common.Pane)


def test_line(): 
    """Find best fit for points on a straight line."""

    # You can test the program with there points that lie on a line passing 
    # through the origin and (1,1,10) 
    
    pixel_info = np.zeros((5,3))

    pixel_info[0,0] = 3.0
    pixel_info[0,1] = 3.0
    pixel_info[0,2] = 30.0
    pixel_info[1,0] = 3.5
    pixel_info[1,1] = 3.5
    pixel_info[1,2] = 35.0
    pixel_info[2,0] = 4.0
    pixel_info[2,1] = 4.0
    pixel_info[2,2] = 40.0
    pixel_info[3,0] = 4.5
    pixel_info[3,1] = 4.5
    pixel_info[3,2] = 45.0
    pixel_info[4,0] = 5.0
    pixel_info[4,1] = 5.0
    pixel_info[4,2] = 50.0

    a = np.array([3,3,30])
    b = np.array([5,5,50])

    c = np.array([1,1,10]) 

    centroid = (a + b)/2
    direction = (c/(102)**(0.5))
    point = np.array([2,2,20])

    assert (centroid == recon.find_centroid(pixel_info)).all()
    assert (direction == recon.find_direction(pixel_info)).all()



def test_distance_func(): 
    """tests to determine if distance_func and measure are working """

    assert 0.5 == recon.distance_func(np.array([0.5, 0.0, 0.0]), np.array([0.0, 1.0, 0.0]), np.array([0.0, 1.0, 0.0]))
    assert 0.0 == recon.distance_func(np.array([2.0, 2.0, 20.0]), np.array([0.0, 0.0, 0.0]), np.array([1.0, 1.0, 10]))

    pixel_info = np.zeros((5,3))

    #These points (pixel_info) lie on a straight line

    pixel_info[0,0] = 3.0
    pixel_info[0,1] = 3.0
    pixel_info[0,2] = 30.0
    pixel_info[1,0] = 3.5
    pixel_info[1,1] = 3.5
    pixel_info[1,2] = 35.0
    pixel_info[2,0] = 4.0
    pixel_info[2,1] = 4.0
    pixel_info[2,2] = 40.0
    pixel_info[3,0] = 4.5
    pixel_info[3,1] = 4.5
    pixel_info[3,2] = 45.0
    pixel_info[4,0] = 5.0
    pixel_info[4,1] = 5.0
    pixel_info[4,2] = 50.0

    assert 0.0 == recon.distance_func(np.array([2.0, 2.0, 20.0]), recon.find_centroid(pixel_info), recon.find_direction(pixel_info))
    assert 0.0 == recon.measure(pixel_info)

    #Another test, this time all the points do not lie on a straight line. 4 of the 5
    # are offset by 0.25 in the +ve and -ve x and y directions 

    pixel_info_2 = np.zeros((5,3))

    #Another test, this time all the points do not lie on a straight line. 4 of the 5
    # are offset by 0.25 in the +ve and -ve x and y directions 

    pixel_info_2[0,0] = 3.25
    pixel_info_2[0,1] = 3.0
    pixel_info_2[0,2] = 30.0
    pixel_info_2[1,0] = 3.5
    pixel_info_2[1,1] = 3.75
    pixel_info_2[1,2] = 35.0
    pixel_info_2[2,0] = 3.75
    pixel_info_2[2,1] = 4.0
    pixel_info_2[2,2] = 40.0
    pixel_info_2[3,0] = 4.5
    pixel_info_2[3,1] = 4.25
    pixel_info_2[3,2] = 45.0
    pixel_info_2[4,0] = 5.0
    pixel_info_2[4,1] = 5.0
    pixel_info_2[4,2] = 50.0

    assert 0.0 != recon.distance_func(pixel_info_2[1], recon.find_centroid(pixel_info_2), recon.find_direction(pixel_info_2))
    assert 0.0 != recon.measure(pixel_info_2)



    