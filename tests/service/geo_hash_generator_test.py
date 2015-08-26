from server.service.geo_hash_grid_generator import get_surroundings_grid


def test_get_shops_dictionary_hashed_500radius_should_be_9():
    result = get_surroundings_grid("u6sc9f", 1)
    assert len(result) == 9


def test_get_shops_dictionary_hashed_1000radius_should_be_25():
    result = get_surroundings_grid("u6sc9f", 2)
    assert len(result) == 25


def test_get_shops_dictionary_hashed_2000radius_should_be_81():
    result = get_surroundings_grid("u6sc9f", 4)
    assert len(result) == 81
