from uuid import UUID
import server.service.shops_service
import server.service.products_service
import pytest


@pytest.fixture()
def sut(monkeypatch):
    def return_mock_get_shop_ids_list_by_location_and_tags(rep, lat, long, range, tags):
        list = [11, 12, 13, 14, 15]
        return list

    monkeypatch.setattr(server.service.shops_service.ShopsService, 'get_shop_ids_list_by_location_and_tags',
                        return_mock_get_shop_ids_list_by_location_and_tags)

    mock_shops_service = server.service.shops_service.ShopsService('', None, 6)

    def return_mock_get_ordered_products_by_shop_ids(rep, list, ammount):
        return [1, 2, 3, 4, 5, 6, 7, 8, 9]

    monkeypatch.setattr(server.service.products_service.ProductsService, 'get_ordered_products_by_shop_ids',
                        return_mock_get_ordered_products_by_shop_ids)
    mock_products_service = server.service.products_service.ProductsService('', '')

    return server.products_controller.ProductsController(mock_shops_service, mock_products_service)


def test_result_items_should_be_same_from_product_service(sut):
    result = sut.get_products_list(20, 20, 100, [], 10)
    assert len(result) == 9
