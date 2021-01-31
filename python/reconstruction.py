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
        # TODO: wording
        event: The event whose original path is to be reconstructed.
        """












################################################################################################

import numpy as np


#here we have to import some functions from common which can read the activated pixels
# and convert them into coordinates. This would be the coordinates of the point at 
# which each pixel would be centered.

pixel_info = np.zeros((5,3))

def find_centroid(pixel_info): #returns centroid
    centroid = np.mean(pixel_info, axis=0)
    return centroid



def find_direction(pixel_info): #returns direction
    centroid = find_centroid(pixel_info)
    direction = np.array([1.0, 0.0, 0.0])

    for j in range(10):
        next_direction = np.array([0.0, 0.0, 0.0])
        for i in range(5):
            point_vec = pixel_info[i] - centroid

            dot = np.dot(direction, point_vec)

            next_direction += dot*point_vec

        norm = np.dot(next_direction, next_direction)
    
        direction = (1/(norm**(0.5)))*next_direction
        #print(direction)
        

    #print(direction)
    return direction

def distance_func(point, point_on_line, dcs_of_line):
    centroid = point_on_line #any point on the line
    direction = dcs_of_line #direction cosines of the line
    vector_to_centroid = centroid - point
    area_of_parallelogram = np.cross(vector_to_centroid, direction)

    distance = (np.dot(area_of_parallelogram,area_of_parallelogram))/(np.dot(direction,direction))
    distance = (abs(distance))**(0.5)
    return distance


def measure(pixel_info):
    sum_distances = 0.0
    for i in range(5):
        sum_distances += distance_func(pixel_info[i], find_centroid(pixel_info), find_direction(pixel_info))

    return sum_distances

 


#print(find_direction())
#print(measure())





#print("##############################################")



#######################################################################
#Another test, this time all the points do not lie on a straight line. 4 of the 5
# are offset by 0.25 in the +ve and -ve x and y directions 

pixel_info[0,0] = 3.25
pixel_info[0,1] = 3.0
pixel_info[0,2] = 30.0
pixel_info[1,0] = 3.5
pixel_info[1,1] = 3.75
pixel_info[1,2] = 35.0
pixel_info[2,0] = 3.75
pixel_info[2,1] = 4.0
pixel_info[2,2] = 40.0
pixel_info[3,0] = 4.5
pixel_info[3,1] = 4.25
pixel_info[3,2] = 45.0
pixel_info[4,0] = 5.0
pixel_info[4,1] = 5.0
pixel_info[4,2] = 50.0





#print(find_direction())
#print(measure())

#################################################################
# You can test the program with there points that lie on a line passing 
# through the origin and (1,1,10) 
#pixel_info[0,0] = 3.0
#pixel_info[0,1] = 3.0
#pixel_info[0,2] = 30.0
#pixel_info[1,0] = 3.5
#pixel_info[1,1] = 3.5
#pixel_info[1,2] = 35.0
#pixel_info[2,0] = 4.0
#pixel_info[2,1] = 4.0
#pixel_info[2,2] = 40.0
#pixel_info[3,0] = 4.5
#pixel_info[3,1] = 4.5
#pixel_info[3,2] = 45.0
#pixel_info[4,0] = 5.0
#pixel_info[4,1] = 5.0
#pixel_info[4,2] = 50.0

###########################################################

#######################################################################
#Another test, this time all the points do not lie on a straight line. 4 of the 5
# are offset by 0.25 in the +ve and -ve x and y directions 

#pixel_info_2 = np.zeros((5,3))


#pixel_info_2[0,0] = 3.25
#pixel_info_2[0,1] = 3.0
#pixel_info_2[0,2] = 30.0
#pixel_info_2[1,0] = 3.5
#pixel_info_2[1,1] = 3.75
#pixel_info_2[1,2] = 35.0
#pixel_info_2[2,0] = 3.75
#pixel_info_2[2,1] = 4.0
#pixel_info_2[2,2] = 40.0
#pixel_info_2[3,0] = 4.5
#pixel_info_2[3,1] = 4.25
#pixel_info_2[3,2] = 45.0
#pixel_info_2[4,0] = 5.0
#pixel_info_2[4,1] = 5.0
#pixel_info_2[4,2] = 50.0

###########################################################

#def distance_func_2():

#def measure_2():
#   sum_distances = 0.0
#    for i in range(5):
#        sum_distances += distance_func(pixel_info_2[i])
#
#    return sum_distances

#print(measure_2())
