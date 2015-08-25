__author__ = 'miguelandres'
import server.repository.shops_repository
import server.service.shops_service
from server.entity.shop import Shop
import pytest
# from geopy.distance import vincenty
import geopy.distance


@pytest.fixture()
def sut(monkeypatch):
    def return_mock_tags_repository_contains(rep, tagname):
        vals = dict()
        vals['scandinavian'] = False
        vals['underwear'] = False
        vals['books'] = False
        return vals[tagname]

    geo_hash_size = 6
    mock_shops_repository = server.repository.shops_repository.ShopsRepository('', geo_hash_size)
    mock_tags_service = server.service.tags_service.TagsService(server.repository.tags_repository.TagsRepository(''),
                                                                server.repository.tagging_repository.TaggingRepository(
                                                                    ''))

    return server.service.shops_service.ShopsService(mock_shops_repository, mock_tags_service, geo_hash_size)


def test_when_3_in_range_result_should_be_3(sut):
    shops = [Shop(12, 59.324441428304176, 18.08207055956655, ""),
             Shop(13, 59.32565044794671, 18.083440945216633, ""),
             Shop(14, 59.32430265413899, 18.081846962844146, "")]

    result = sut.filter_brute_force(59.3250732047, 18.0823266506, 100, shops)
    assert len(result) == 3


def test_when_2_in_range_and_2_not_result_should_be_2(sut):
    shops = [Shop(12, 59.324441428304176, 18.08207055956655, ""),
             Shop(13, 59.32430265413899, 18.081846962844146, ""),
             Shop(14, 59.32621032422528, 18.08444425361356, ""),
             Shop(15, 59.324664699340794, 18.085411555995464, "")
             ]

    result = sut.filter_brute_force(59.3250732047, 18.0823266506, 100, shops)
    assert len(result) == 2