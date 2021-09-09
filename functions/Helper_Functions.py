import math
import random
# Finding the coordinates to center an object in the x-axis
def x_center(screen_width, object_width):
    center_of_screen_horizontal = screen_width / 2
    half_of_object_width = object_width / 2
    horizontal_center = center_of_screen_horizontal - half_of_object_width
    return horizontal_center

# Finding the coordinates to center an object in the y-axis
def y_center(screen_heigth, object_height):
    center_of_screen_vertical = screen_heigth / 2
    half_of_object_height = object_height / 2
    vertical_center = center_of_screen_vertical - half_of_object_height
    return vertical_center

# Returns central coordinates of the object in tuple form
def center_coords(screen_wh : tuple, player_wh : tuple):
    center = (int(screen_wh[0]/2 - player_wh[0]/2), int(screen_wh[1]/2 - player_wh[1]/2))
    return center

# Returns the distance between two coordinates
def distance(object1: tuple, object2: tuple):
    return math.sqrt(((object2[0]-object1[0])**2) + ((object2[1]-object1[1])**2))

# Returns a random coordinate in a specified area // first_coords is the upper-left point of a rectange and second_coords is the lower-right point
def random_coords(first_coords: tuple, second_coords: tuple):
    random_x = random.randint(first_coords[0], second_coords[0])
    random_y = random.randint(first_coords[1], second_coords[1])
    return (random_x, random_y)


