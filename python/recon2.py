import numpy as np

#the activated pixel information is converted into points in space and time using the detector germoetry 
#read https://zalo.github.io/blog/line-fitting/ for how we are itteratively finding the direction



pixel_info =  np.zeros((5,3))
centroid = np.zeros((3))
direction = np.zeros((3))
direction[0] = 1  #initial guess direction is (1,0,0)
point_vec = np.empty((3)) #the vector that points to different points from centroid
next_direction = np.empty((3))
dot = 0.0
#norm = 0.0

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

def find_centroid(): #finds the centroid
    for i in range(3):
        for j in range (5):
            centroid [i] += pixel_info[j,i]
        centroid[i] = centroid[i]/5
    #print(centroid)    working fine


def find_direction(): 
    for i in range(5):
        norm = 0.0
        dot = 0.0
        for j in range(3):  #creating the pointing vector
            point_vec[j] = pixel_info[i,j] - centroid[j]

        #print(point_vec) working fine

        for k in range(3):  #finding the dot product
            dot  += direction[k]*point_vec[k]
        
        print("dot product: ", dot)

        for n in range(3):  #adding contribuition of the ith point to next direction
            next_direction[n] += dot*point_vec[n]
    
    
         
    print("norm before calculation: ", norm)
    print("next direction: ", next_direction)
    for m in range(3):  #finding norm of next_direction
        print("adding: ", (next_direction[m])*(next_direction[m]))
        norm += (next_direction[m])*(next_direction[m])

    norm = norm**(0.5)
    
    
    
    for q in range(3):  #normalizing next direction 
        print("normalizing with norm: ", norm)
        next_direction[q] = next_direction[q]/norm
    
    for a in range(3): #updating direction
        direction[a] = next_direction[a]
        
        
    print(direction)

    


if __name__ == "__main__":
    find_centroid()
    find_direction()





        

            





