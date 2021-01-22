import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


#the activated pixel information is converted into points in space and time using the detector germoetry 
#read https://zalo.github.io/blog/line-fitting/ for how we are itteratively finding the direction



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
example_pixel_info = np.empty((5,3))
example_pixel_info[0,0] = 3.0
example_pixel_info[0,1] = 3.0
example_pixel_info[0,2] = 30.0
example_pixel_info[1,0] = 3.5
example_pixel_info[1,1] = 3.5
example_pixel_info[1,2] = 35.0
example_pixel_info[2,0] = 4.0
example_pixel_info[2,1] = 4.0
example_pixel_info[2,2] = 40.0
example_pixel_info[3,0] = 4.5
example_pixel_info[3,1] = 4.5
example_pixel_info[3,2] = 45.0
example_pixel_info[4,0] = 5.0
example_pixel_info[4,1] = 5.0
example_pixel_info[4,2] = 50.0

rng = np.random.default_rng()
noise = rng.normal(scale = 0.25 * np.tile(np.array([1., 1., 10.]), (5, 1)), size = (5,3))
example_pixel_info = example_pixel_info + noise

example_direction_2 = np.array([1., 3., 5.])
example_pixel_info_2 = np.array([example_direction_2 * t for t in [float(i) for i in range(10)]])
noise_2 = rng.normal(scale = 0.25 * np.tile(np.array([1., 3., 5.]), (len(example_pixel_info_2), 1)), size = (len(example_pixel_info_2),3))
example_pixel_info_2 = example_pixel_info_2 + noise_2


###########################################################

def find_centroid(pixel_info): #finds the centroid
    for i in range(3):
        for j in range (len(pixel_info)):
            centroid [i] += pixel_info[j,i]
        centroid[i] = centroid[i]/len(pixel_info)
    #print(centroid)    working fine


def find_direction(pixel_info): 
    for i in range(len(pixel_info)):
        norm = 0.0
        dot = 0.0
        for j in range(3):  #creating the pointing vector
            point_vec[j] = pixel_info[i,j] - centroid[j]

        #print(point_vec) working fine

        for k in range(3):  #finding the dot product
            dot  += direction[k]*point_vec[k]
        
        #print(dot) dot product working fine

        for n in range(3):  #adding contribuition of the ith point to next direction
            next_direction[n] += dot*point_vec[n]
    
    
         
    for m in range(3):  #finding norm of next_direction
        norm += (next_direction[m])*(next_direction[m])

    norm = norm**(0.5)
    
    
    
    for q in range(3):  #normalizing next direction 
        next_direction[q] = next_direction[q]/norm
    
    for a in range(3): #updating direction
        direction[a] = next_direction[a]
        
        
    print(direction)

# Plotting (see: https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html)

def plot_all(pixel_info):
    global centroid, direction
    fig = plt.figure()
    # plot pixels
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(pixel_info[:,0], pixel_info[:,1], 'bo', zs = pixel_info[:,2])
    # plot centroid point
    find_centroid(pixel_info)
    ax.plot([centroid[0]], [centroid[1]], 'r+', zs = [centroid[2]])
    # plot n iterations of direciton vector
    for iteration_number in range(5):
        find_direction(example_pixel_info)
        plot_centroid_direction(ax, label='direction {}: {}'.format(iteration_number+1, direction))
    ax.legend()
    plt.show(fig)
    
def plot_centroid_direction(ax, **kwargs):
    global centroid, direction
    arr_src = centroid
    arr_tgt = centroid + 10 * direction
    arrow = np.array([arr_src, arr_tgt])
    ax.plot(arrow[:,0], arrow[:,1], zs = arrow[:,2], **kwargs)


if __name__ == "__main__":
    plot_all(example_pixel_info_2)
    find_centroid(example_pixel_info)
    print("centroid:", centroid)
    find_direction(example_pixel_info)
