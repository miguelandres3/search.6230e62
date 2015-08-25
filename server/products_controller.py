__author__ = 'miguelandres'

from flask import current_app
import time

class ProductsController:
    def __init__(self, shops_service, products_service):
        self.shops_service = shops_service
        self.products_service = products_service

    def get_products_list(self, lat, long, range, tags, ammount):

        # get shops based on the current location, range and tags
        start_time = time.clock()
        shop_ids = self.shops_service.get_shop_ids_list_by_location_and_tags(lat, long, range, tags)
        print('*time get shops: ' + str(time.clock() - start_time) + " seconds")

        start_time = time.clock()
        list_products = self.products_service.get_ordered_products_by_shop_ids(shop_ids, ammount)
        print('*time get products: ' + str(time.clock() - start_time) + " seconds")
        return list_products
