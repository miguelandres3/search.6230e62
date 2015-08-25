# -*- coding: utf-8 -*-

from server.repository.tagging_repository import TaggingRepository
import pytest
from uuid import UUID

id_scandinavian = UUID('4202dd8da64d4ebea7577f0f2b2e991b')


@pytest.fixture(scope="module")
def sut():
    return TaggingRepository('data/taggings.csv')


def test_items_should_be_26(sut):
    assert len(sut.dictionary.values()) == 26


def test_dictionary_should_contain_UUID(sut):
    assert id_scandinavian in sut.dictionary


def test_get_shop_ids_should_return_1205_entries_given_scandinavian(sut):
    result = sut.get_shop_ids_list_by_tag_id(id_scandinavian)
    assert len(result) == 1205
