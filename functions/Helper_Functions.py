

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

# Divides the map_set from the tmx file into rows and columns
# ADD LAYERS
def map_organizer(map_set : list, width : int, height : int):
    new_set = [[] for i in range(height)]
    row_count = 0
    for count, tile in enumerate(map_set):
        count += 1
        new_set[row_count].append(tile)
        if not count % width:
            row_count += 1
    return new_set