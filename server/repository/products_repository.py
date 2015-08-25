import csv
from server.entity.product import Product
from uuid import UUID
from collections import defaultdict


class ProductsRepository:
    def __init__(self, filename):

        if filename:

            self.filename = filename
            self.dictionary = defaultdict(list)

            with open(filename, "rb") as csvfile:
                datareader = csv.reader(csvfile)
                next(datareader, None)  # skip the headers
                for row in datareader:
                    id = UUID(row[Column.id])
                    shop_id = UUID(row[Column.shop_id])
                    title = row[Column.title]
                    popularity = float(row[Column.popularity])
                    quantity = int(row[Column.quantity])

                    product = Product(id, title, popularity, quantity, shop_id)

                    self.dictionary[shop_id].append(product)

    def get_products_list_by_shop_id(self, shop_id):

        return self.dictionary[shop_id]


class Column:
    id = 0
    shop_id = 1
    title = 2
    popularity = 3
    quantity = 4
