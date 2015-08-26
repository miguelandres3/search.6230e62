__author__ = 'miguelandres'

"""
    TagsService

    Business layer class in charged of handling information from tags and taggings


    Attributes:
    ===========
    Instances of taggins repository and tags repository

    """

class TagsService:
    def __init__(self, tags_repository, taggings_repository):
        self.tags_repository = tags_repository
        self.taggings_repository = taggings_repository

    def get_shop_ids_list_by_tag_names(self, tagnames):

        listTagIds = list()
        for tag in tagnames:
            if self.tags_repository.contains(tag):
                listTagIds.append(self.tags_repository.get_tag_id_by_name(tag))
        print('tags found:' + str(len(listTagIds)))

        listShopIds = list()
        for tagId in listTagIds:
            listShopIds.extend(self.taggings_repository.get_shop_ids_list_by_tag_id(tagId))
            # remove duplicates
        listShopIds = list(set(listShopIds))
        print('shop ids found by tag:' + str(len(listShopIds)))

        return listShopIds
