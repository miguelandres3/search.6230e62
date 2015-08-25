__author__ = 'miguelandres'

from geopy.distance import vincenty
import time
import geohash
from server.service.geo_hash_grid_generator import get_surroundings_grid


class ShopsService:
    def __init__(self, shops_repository, tags_service, hash_size):
        self.shops_repository = shops_repository
        self.tags_service = tags_service
        self.hash_size = hash_size

    def get_shop_ids_list_by_location_and_tags(self, lat, long, range, tagnames):

        # filters the shops by location
        shop_ids = self.get_shop_ids_by_location_geo_hashed(lat, long, range)

        # if tags are provided intersects the tags with the location results
        if len(tagnames) > 0:
            shop_ids_by_tags = self.tags_service.get_shop_ids_list_by_tag_names(tagnames)
            shop_ids = set(shop_ids).intersection(shop_ids_by_tags)

        return shop_ids

    def get_shop_ids_by_location_geo_hashed(self, lat, long, range):

        # hash for the current location
        geo_hash = geohash.encode(lat, long, self.hash_size)

        # amount of rectangles around the geo_hash depending on the radius
        levels = int(range / 500)

        # gets the grid of geo hashes thay concerns the radius
        surroundings_hashes = get_surroundings_grid(geo_hash, levels)
        shops = self.shops_repository.get_shops_by_geohashes(surroundings_hashes)

        # refine search with brute force to increase accuracy, within the subset
        shopsfiltered = self.filter_brute_force(lat, long, range, shops)

        return shopsfiltered

    # filters a set of shops using brute force using the vicenty algorithm
    def filter_brute_force(self, lat, long, range, shops):
        start_time = time.clock()
        currentlocation = (lat, long)

        shopsfiltered = dict()
        print('shops to filter: ' + str(len(shops)))
        for shop in shops:
            shoplocation = (shop.lat, shop.long)
            # distance calculation
            distance = vincenty(currentlocation, shoplocation).meters
            if distance < range:
                shopsfiltered[shop.id] = shop
        print('time narrow filter: ' + str(time.clock() - start_time) + " seconds")
        return shopsfiltered.keys()
