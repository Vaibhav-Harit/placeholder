import pygame as pg
import os 

class map_renderer():
    def __init__(self, map_dir : list, tile_dir : str, render_position : tuple, tile_length : int, map_user = None):
        self.user = map_user
        self.map_set = map_renderer.map_loader(map_dir)
        self.tile_set = map_renderer.tile_loader(tile_dir, tile_length)
        self.t_width = tile_length
        self.x = render_position[0]
        self.y = render_position[1]

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
                    print(line)
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
            print(len(map_sets), len(map_sets[0]), len(map_sets[1]))
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

    def render(self, screen : pg.display):
        for layer in self.map_set:
            y = self.y
            for tiles in layer:
                x = self.x
                for tile in tiles:
                    if not tile:
                        x += 1
                        continue
                    screen.blit(self.tile_set[tile], (x * self.t_width, y * self.t_width))
                    x += 1
                y += 1

    def move_map(self, x_diff : int, y_diff : int):
        self.x += x_diff
        self.y += y_diff

map_machine = map_renderer('assets//maps//test0.tmx', 'assets//tiles', (0, 0), 32)