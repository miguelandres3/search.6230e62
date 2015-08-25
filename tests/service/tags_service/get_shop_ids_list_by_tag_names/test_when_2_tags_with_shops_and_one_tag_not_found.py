from uuid import UUID
import server.repository.tags_repository
import server.repository.tagging_repository
import server.service.tags_service
import pytest

tagnames = ['scandinavian', 'underwear', 'books']
scandinavian_id = UUID('32323232323232323232323232323232')
underwear_id = UUID('32323232323232323232323232323234')


@pytest.fixture()
def sut(monkeypatch):
    def return_mock_tags_repository_get_tag_id_by_name(rep, tagname):
        vals = dict()
        vals['scandinavian'] = scandinavian_id
        vals['underwear'] = underwear_id
        return vals[tagname]

    def return_mock_tags_repository_contains(rep, tagname):
        vals = dict()
        vals['scandinavian'] = True
        vals['underwear'] = True
        vals['books'] = False
        return vals[tagname]

    monkeypatch.setattr(server.repository.tags_repository.TagsRepository, 'get_tag_id_by_name',
                        return_mock_tags_repository_get_tag_id_by_name)
    monkeypatch.setattr(server.repository.tags_repository.TagsRepository, 'contains',
                        return_mock_tags_repository_contains)

    mock_tags_repository = server.repository.tags_repository.TagsRepository('')

    def return_mock_tagging_repository_get_shop_ids_list_by_tag_id(rep, tag_id):
        vals = dict()
        vals[scandinavian_id] = [UUID('44443232323232323232323232323231'),
                                 UUID('44443232323232323232323232323232'),
                                 UUID('44443232323232323232323232323233')]
        vals[underwear_id] = [UUID('55553232323232323232323232323231'),
                              UUID('55553232323232323232323232323232')]
        return vals[tag_id]

    monkeypatch.setattr(server.repository.tagging_repository.TaggingRepository, 'get_shop_ids_list_by_tag_id',
                        return_mock_tagging_repository_get_shop_ids_list_by_tag_id)
    mock_tagging_repository = server.repository.tagging_repository.TaggingRepository('')

    return server.service.tags_service.TagsService(mock_tags_repository, mock_tagging_repository)


def test_result_should_be_5_entries(sut):
    result = sut.get_shop_ids_list_by_tag_names(tagnames)
    assert len(result) == 5
