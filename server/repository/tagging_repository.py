import csv
from collections import defaultdict
from uuid import UUID


class TaggingRepository:
    def __init__(self, filename):
        if filename:
            self.filename = filename
            self.dictionary = defaultdict(list)
            with open(self.filename, "rb") as csvfile:
                datareader = csv.reader(csvfile)
                next(datareader, None)  # skip the headers

                for row in datareader:
                    shop_id = UUID(row[Column.shop_id])
                    tag_id = UUID(row[Column.tag_id])

                    self.dictionary[tag_id].append(shop_id)

    def get_shop_ids_list_by_tag_id(self, id_tag):
        return self.dictionary[id_tag]


class Column:
    shop_id = 1
    tag_id = 2
