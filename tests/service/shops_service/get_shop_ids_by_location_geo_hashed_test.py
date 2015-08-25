from uuid import UUID
import server.repository.tags_repository
import server.repository.tagging_repository
import server.service.tags_service
from server.entity.shop import Shop
import pytest


@pytest.fixture()
def sut(monkeypatch):
    def return_mock_shops_repository_get_shops_by_geohashes(rep, geo_hashes):
        return [Shop(UUID('000000000000000000000000000000A1'), 59.32411133542461, 18.087289244632373, ""),
                Shop(UUID('000000000000000000000000000000A2'), 59.32493295518423, 18.08621391001444, ""),
                Shop(UUID('000000000000000000000000000000A3'), 59.324664699340794, 18.085411555995464, ""),
                Shop(UUID('000000000000000000000000000000A4'), 59.32395620198659, 18.0857458099434, ""),
                Shop(UUID('000000000000000000000000000000A5'), 59.32429349213489, 18.08419198843006, "")]

    monkeypatch.setattr(server.repository.shops_repository.ShopsRepository, 'get_shops_by_geohashes',
                        return_mock_shops_repository_get_shops_by_geohashes)

    mock_shops_repository = server.repository.shops_repository.ShopsRepository('', 6)

    def return_mock_tagging_service_get_shop_ids_list_by_tag_names(rep, tag_id):
        return []

    monkeypatch.setattr(server.service.tags_service.TagsService, 'get_shop_ids_list_by_tag_names',
                        return_mock_tagging_service_get_shop_ids_list_by_tag_names)
    mock_tags_service = server.service.tags_service.TagsService('', '')

    return server.service.shops_service.ShopsService(mock_shops_repository, mock_tags_service, 6)


def test_result_should_be_shop_ids_in_range(sut):
    result = sut.get_shop_ids_by_location_geo_hashed(59.3248050025, 18.0865430832, 100)
    assert len(result) == 3
    assert result[0] == UUID('000000000000000000000000000000A1')
    assert result[1] == UUID('000000000000000000000000000000A2')
    assert result[2] == UUID('000000000000000000000000000000A3')
