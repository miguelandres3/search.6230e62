# -*- coding: utf-8 -*-

from server.repository.shops_repository import ShopsRepository
import pytest
from uuid import UUID

id_shop = UUID('ac69bcc197894e01bd9f9f6995fc891f')


@pytest.fixture(scope="module")
def sut():
    return ShopsRepository('data/shops.csv',6)


def test_items_should_be_10000(sut):
    assert len(sut.dictionary.values()) == 10000


def test_dictionary_should_contain_id_shop(sut):
    assert id_shop in sut.dictionary


def test_get_shop_by_id_should_correspond(sut):
    result = sut.get_shop_by_id(id_shop)
    assert result.id == UUID('ac69bcc197894e01bd9f9f6995fc891f')
    assert result.lat == float('59.36716393488899')
    assert result.long == float('18.15592735214583')


def test_get_all_should_be_10000(sut):
    result = sut.get_all()
    assert len(result) == 10000

def test_get_shops_by_geohash_u6sc9f_should_be_11(sut):
    result = sut.get_shops_by_geohash("u6sc9f")
    assert len(result) == 11

def test_get_shops_by_three_geohashes_should_be_19(sut):
    result = sut.get_shops_by_geohashes(["u6sc9f","u6sc92","u6sc96"])
    assert len(result) == 19