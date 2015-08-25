import csv
from server.entity.shop import Shop
from uuid import UUID
import geohash
from collections import defaultdict


class ShopsRepository:
    def __init__(self, filename, geohashSize):
        if filename:
            self.dictionary = dict()
            self.geodictionary = defaultdict(list)
            with open(filename, "rb") as csvfile:
                datareader = csv.reader(csvfile)

                next(datareader, None)  # skip the headers
                for row in datareader:
                    id = UUID(row[Column.id])
                    name = row[Column.name]
                    lat = float(row[Column.lat])
                    long = float(row[Column.long])
                    geo_hash64 = geohash.encode_uint64(lat, long)
                    geo_hash = geohash.encode(lat, long, 20)

                    shop = Shop(id, lat, long, geo_hash)
                    self.dictionary[id] = shop
                    self.geodictionary[geo_hash[:geohashSize]].append(shop)

    def get_shop_by_id(self, shop_id):
        return self.dictionary[shop_id]

    def get_all(self):
        return self.dictionary.values()

    def get_shops_by_geohash(self, geo_hash):
        shops = list()
        if geo_hash in self.geodictionary:
            shops = self.geodictionary[geo_hash]
        return shops

    def get_shops_by_geohashes(self, geo_hashes):
        shops = list()
        for hash in geo_hashes:
            setshops = self.get_shops_by_geohash(hash)
            shops.extend(setshops)
        return shops

class Column:
    id = 0
    name = 1
    lat = 2
    long = 3
