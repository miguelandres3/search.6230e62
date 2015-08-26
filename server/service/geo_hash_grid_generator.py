__author__ = 'miguelandres'
from collections import defaultdict

import geohash

"""
    geo hash grid generator

    Generates the grid of geo hashes levels indicates how many
    layers of surroundings are desired depending on the radius

    """


# gets the surroundings of the hash and the surroundings of the surrounding depending on the radius
def get_surroundings_grid(geo_hash, levels):
    # should at least return one geo hash and its surroundings
    if levels == 0:
        levels = 1
    grid_hashes = dict()
    grid_hashes[geo_hash] = True
    count = 1
    # levels is proportional to the radius to get the size of the patch
    while (count <= levels):

        grid_hashes_new = dict()
        for cell in grid_hashes.keys():
            surroundings = geohash.expand(cell)
            grid_hashes_new[cell] = True
            for newcell in surroundings:
                grid_hashes_new[newcell] = True
        grid_hashes = grid_hashes_new
        count = count + 1
    return grid_hashes.keys()
