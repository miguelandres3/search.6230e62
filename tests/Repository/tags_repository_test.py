# -*- coding: utf-8 -*-

from server.repository.tags_repository import TagsRepository
import pytest
from uuid import UUID


@pytest.fixture(scope="module")
def sut():
    return TagsRepository('data/tags.csv')


def test_items_should_be_26(sut):
    assert len(sut.dictionary.values()) == 26


def test_repository_should_contain_scandinavian(sut):
    assert sut.contains('scandinavian')


def test_repository_should_not_contain_scandinavian_random(sut):
    assert not sut.contains('scandinavian_random')


def test_get_tag_id_by_name_should_correspond(sut):
    result = sut.get_tag_id_by_name('scandinavian')
    assert result == UUID('4202dd8da64d4ebea7577f0f2b2e991b')


def test_get_tag_id_by_name_should_not_be_case_sensitive(sut):
    result = sut.get_tag_id_by_name('SCANDINAVIAN')
    assert result == UUID('4202dd8da64d4ebea7577f0f2b2e991b')
