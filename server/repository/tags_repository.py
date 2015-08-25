import csv
from uuid import UUID


class TagsRepository:
    def __init__(self, filename):
        if filename:
            with open(filename, "rb") as csvfile:
                datareader = csv.reader(csvfile)
                self.dictionary = dict()
                next(datareader, None)  # skip the headers
                for row in datareader:
                    id = UUID(row[Column.id])
                    name = row[Column.name]

                    self.dictionary[name.lower()] = id

    def get_tag_id_by_name(self, name):
        return self.dictionary[name.lower()]

    def contains(self, name):
        return name.lower() in self.dictionary


class Column:
    id = 0
    name = 1
