from uuid import UUID
import server.repository.tags_repository
import server.repository.tagging_repository
import server.service.tags_service
import pytest


@pytest.fixture()
def sut(monkeypatch):
    def return_mock_tags_repository_get_tag_id_by_name(rep, tagname):
        vals = dict()
        return vals[tagname]

    def return_mock_tags_repository_contains(rep, tagname):
        vals = dict()
        vals['scandinavian'] = False
        vals['underwear'] = False
        vals['books'] = False
        return vals[tagname]

    monkeypatch.setattr(server.repository.tags_repository.TagsRepository, 'get_tag_id_by_name',
                        return_mock_tags_repository_get_tag_id_by_name)
    monkeypatch.setattr(server.repository.tags_repository.TagsRepository, 'contains',
                        return_mock_tags_repository_contains)

    mock_tags_repository = server.repository.tags_repository.TagsRepository('')

    def return_mock_tagging_repository_get_shop_ids_list_by_tag_id(rep, tag_id):
        vals = dict()
        return vals[tag_id]

    monkeypatch.setattr(server.repository.tagging_repository.TaggingRepository, 'get_shop_ids_list_by_tag_id',
                        return_mock_tagging_repository_get_shop_ids_list_by_tag_id)
    mock_tagging_repository = server.repository.tagging_repository.TaggingRepository('')

    return server.service.tags_service.TagsService(mock_tags_repository, mock_tagging_repository)


def test_result_should_be_empty(sut):
    result = sut.get_shop_ids_list_by_tag_names(['scandinavian', 'underwear', 'books'])
    assert len(result) == 0
