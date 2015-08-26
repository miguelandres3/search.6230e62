__author__ = 'miguelandres'

from server.dto.product_dto import Product
from server.dto.shop_dto import Shop
import time

"""

    ProductsService

    Gets a list of DTO objects to transfer to the controller based on a list of shops ids

    """


class ProductsService:
    def __init__(self, products_repository, shops_repository):
        self.products_repository = products_repository
        self.shops_repository = shops_repository


    def get_ordered_products_by_shop_ids(self, shop_ids, amount):

        # put products from stores together
        all_products = self.join_products_from_shops(shop_ids)

        # sort
        all_products.sort(key=lambda x: x.popularity, reverse=True)
        trunk_products = all_products[:amount]

        # build transfer entities
        list_products_DTO = self.map_entities_to_DTO(trunk_products)
        return list_products_DTO



    def map_entities_to_DTO(self, trunk_products):
        list_products_DTO = list()
        for product in trunk_products:
            shop = self.shops_repository.get_shop_by_id(product.shop_id)
            shopDto = Shop(shop.id, shop.lat, shop.long)
            productDTO = Product(product.id, product.title, product.popularity, product.quantity, shopDto)
            list_products_DTO.append(productDTO)
        return list_products_DTO


    def join_products_from_shops(self, shop_ids):
        all_products = list()
        for shop_id in shop_ids:
            products = self.products_repository.get_products_list_by_shop_id(shop_id)
            all_products.extend(products)
        return all_products
