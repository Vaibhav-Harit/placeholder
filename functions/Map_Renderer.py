import pygame as pg
import os 

class map_renderer():
    def __init__(self, map_set : list, tile_dir : str, render_position : tuple, tile_length : int, map_user = None):
        self.user = map_user
        self.map_set = map_set
        self.tile_set = map_renderer.tile_loader(tile_dir, tile_length)
        self.t_width = tile_length
        self.x = render_position[0]
        self.y = render_position[1]

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
        y = self.y
        for tiles in self.map_set:
            x = self.x
            for tile in tiles:
                screen.blit(self.tile_set[tile], (x * self.t_width, y * self.t_width))
                x += 1
            y += 1

    def move_map(self, x_diff : int, y_diff : int):
        self.x += x_diff
        self.y += y_diff

