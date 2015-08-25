# -*- coding: utf-8 -*-

from server.repository.products_repository import ProductsRepository
import pytest
from uuid import UUID

shop_id = UUID('459af0c0e36d4ddf89e3a0b2a941fe1d')


@pytest.fixture(scope="module")
def sut():
    return ProductsRepository('data/products.csv')


def test_items_should_be_10000(sut):
    assert len(sut.dictionary.values()) == 10000


def test_dictionary_should_contain_shop_id(sut):
    assert shop_id in sut.dictionary


def test_get_products_list_by_shop_id_should_return_6_entries(sut):
    result = sut.get_products_list_by_shop_id(shop_id)
    assert len(result) == 6
