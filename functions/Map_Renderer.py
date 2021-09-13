import pygame as pg
import os 

class map_renderer():
    def __init__(self, map_dir : list, tile_dir : str, render_position : tuple, tile_length : int, screen_wh : tuple,  map_user = None):
        self.user = map_user
        self.map_set = map_renderer.map_loader(map_dir)
        self.layer_num = len(self.map_set)
        self.cur_map = []
        self.tile_set = map_renderer.tile_loader(tile_dir, tile_length)
        self.t_width = tile_length
        self.x = render_position[0]
        self.y = render_position[1]
        self.temp_x = 0
        self.temp_y = 0
        self.tiles_x = (screen_wh[0] + tile_length)//tile_length
        self.tiles_y = (screen_wh[1] + tile_length)//tile_length
        self.optimize(0, 0)
        self.true_scroll = [0, 0]

    @staticmethod
    def map_loader(map_dir : str):
        map_sets = []
        layer_count = 0
        with open(map_dir, 'r') as f:
            layer = ''
            line_num = 0
            while True:
                line = f.readline()

                if line_num == 3:
                    line = line.split('"')
                    width = int(line[-4])
                    height = int(line[-2])
                    f.readline()
                    line = f.readline()
                    layer_count += 1
                line_num += 1
                
                if layer_count:
                    # print(line)
                    try:
                        if line[0].isdigit():
                                layer += line.strip()
                        else:
                            map_sets.append(layer)
                            layer = ''
                            layer_count += 1
                            f.readline()
                            f.readline()
                            f.readline()
                    except:
                        break

            for count, layer in enumerate(map_sets):
                layer = layer.split(',')
                layer = [int(tile) for tile in layer]
                layer = map_renderer.map_organizer(layer, width, height)
                map_sets[count] = layer
            return map_sets
    @staticmethod
    def map_organizer(map_set : list, width : int, height : int):
        new_set = [[] for i in range(height)]
        row_count = 0
        for count, tile in enumerate(map_set):
            count += 1
            new_set[row_count].append(tile)
            if not count % width:
                row_count += 1
        return new_set
    @staticmethod
    def tile_loader(tile_dir : str, tile_length):
        path = tile_dir
        tile_keys = {}
        for root, dirs, files in os.walk(path):
            for file in files:
                key =  int(file[:-4]) # gets key from file name
                tile_sprite =  pg.image.load(os.path.join(root,file)) # converts to pygame surface
                tile_sprite = pg.transform.scale(tile_sprite, (tile_length, tile_length))
                tile_keys[key] = tile_sprite # adds to dictionary
        return tile_keys
    def optimize(self, scroll_x : int, scroll_y : int):
        seed_x = scroll_x//self.t_width
        seed_y = scroll_y//self.t_width
        seed_postion = (seed_x, seed_y)
        seed_end = seed_x + self.tiles_x
        if __name__ == '__main__':
                print(f'''
            Seed :  {seed_postion} 
            Seed End :  {seed_end}''')
        map_getter = []
        for layer in range(self.layer_num):
            map_getter.append([])
            for row in range(self.tiles_y):
                try:
                    tile_row = self.map_set[layer][seed_y + row][seed_x : seed_end]
                    map_getter[layer].append(tile_row)
                except:
                    break
        self.cur_map = map_getter
        if __name__ == '__main__':
            print(self.cur_map)
            pass
    def render(self, screen : pg.display, scroll_x : int, scroll_y : int):
        # if not scroll_x % self.t_width and scroll_x: 
            # self.optimize(scroll_x, scroll_y)
        # for layer in self.map_set:
        for layer in self.cur_map:
            y = 0
            for tiles in layer:
                x = 0
                for tile in tiles:
                    if not tile:
                        x += 1
                        continue
                    screen.blit(self.tile_set[tile], (x * self.t_width - scroll_x, y * self.t_width - scroll_y))
                    x += 1
                y += 1

    def move_map(self, x_diff : int, y_diff : int):
        self.x += x_diff
        # self.temp_x += x_diff
        self.y += y_diff
        # self.temp_y += y_diff

if __name__ == '__main__':
    sc_width = 500
    sc_height = 500


    map_machine = map_renderer('assets//maps//test1.tmx', 'assets//tiles', (0, 0), 64, (sc_width, sc_height))
    map_machine.x -= 8

    map_machine.y -= 16

    map_machine.optimize()











# '''

# MAP = map_set
# SW, WH = screen width, screen height
# TW = tile width


# screen_area = (SW + TW) * (SH + TW)
# tile_area = TW*TW
# total_tiles = screen_area / tile_area
# tiles_x = (SW + TW)/TW
# tiles_y = (SH + TW)/TW

# tile_position_getter(cur_point : tuple):
#     seed_x = cur_point//TW
#     seed_y = cur_point//tw
#     seed_postion = (seed_x, seed_y)
#     seed_end = seed_x + tiles_x

#     map_getter = []
#     for row in range(tiles_y)
#         try:
#             tile_rows = MAP[seed_y + row][seed_x : seed_end]
#             tile_rows.append(map_getter())
#         except:
#             break
        

# tille drawer