__author__ = 'miguelandres'
import conftest
from werkzeug.test import EnvironBuilder
import json


# -*- coding: utf-8 -*-
url = '/search'
headers = {'Content-Type': 'application/json'}
testlat = "59.3276073378"
testlng = "18.0819940567"


def test_area_with_less_products_than_requested(client):
    data = {"count": "200", "lat": testlat, "lng": testlng, "radius": "100", "tags": ""}

    response = client.post(url, data=json.dumps(data), headers=headers)
    result = json.loads(response.data)

    assert response.status_code == 200
    assert len(result["products"]) == 107


def test_area_with_one_tag_should_filter_results(client):
    data = {"count": "200", "lat": testlat, "lng": testlng, "radius": "100",
            "tags": ["scandinavian"]}

    response = client.post(url, data=json.dumps(data), headers=headers)
    result = json.loads(response.data)

    assert response.status_code == 200
    assert len(result["products"]) == 18


def test_area_with_one_upper_case_tag_should_not_be_sensitive(client):
    data = {"count": "200", "lat": testlat, "lng": testlng, "radius": "100",
            "tags": ["Scandinavian"]}

    response = client.post(url, data=json.dumps(data), headers=headers)
    result = json.loads(response.data)

    assert response.status_code == 200
    assert len(result["products"]) == 18


def test_area_with_multiple_tags_should_increase_results(client):
    data = {"count": "200", "lat": testlat, "lng": testlng, "radius": "100",
            "tags": ["scandinavian", "women", "plates"]}

    response = client.post(url, data=json.dumps(data), headers=headers)
    result = json.loads(response.data)

    assert response.status_code == 200
    assert len(result["products"]) == 33


def test_area_with_only_tags_unknown_returns_empty(client):
    data = {"count": "200", "lat": testlat, "lng": testlng, "radius": "100",
            "tags": ["norwegian", "danish", "books"]}

    response = client.post(url, data=json.dumps(data), headers=headers)
    result = json.loads(response.data)

    assert response.status_code == 200
    assert len(result["products"]) == 0


def test_area_with_tags_unknown_returns_products_with_tags_found(client):
    data = {"count": "200", "lat": testlat, "lng": testlng, "radius": "100",
            "tags": ["scandinavian", "danish"]}

    response = client.post(url, data=json.dumps(data), headers=headers)
    result = json.loads(response.data)

    assert response.status_code == 200
    assert len(result["products"]) == 18


def test_area_with_multiple_tags_should_increase_results(client):
    data = {"count": "200", "lat": testlat, "lng": testlng, "radius": "100",
            "tags": ["scandinavian", "women", "plates"]}

    response = client.post(url, data=json.dumps(data), headers=headers)
    result = json.loads(response.data)

    assert response.status_code == 200
    assert len(result["products"]) == 33


def test_when_products_count_is_limited_results_should_be_limited(client):
    data = {"count": "50", "lat": testlat, "lng": testlng, "radius": "2000", "tags": ""}

    response = client.post(url, data=json.dumps(data), headers=headers)
    result = json.loads(response.data)

    assert response.status_code == 200
    assert len(result["products"]) == 50


def test_area_with_no_products(client):
    data = {"count": "50", "lat": "59.331788518", "lng": "17.843170166", "radius": "1000", "tags": ""}

    response = client.post(url, data=json.dumps(data), headers=headers)
    result = json.loads(response.data)
    assert response.status_code == 200
    assert len(result["products"]) == 0


def test_product_properties_most_popular_product_in_area(client):
    data = {"count": "50", "lat": "59.3390386904", "lng": "18.1733071804", "radius": "100", "tags": ""}

    response = client.post(url, data=json.dumps(data), headers=headers)
    result = json.loads(response.data)
    product = result["products"][0]
    assert product["popularity"] == 0.838
    assert product["quantity"] == 1
    assert product["id"] == 'f5d39fa3-ae58-4b4e-afd8-cbf57374718c'
    assert product["shop"]["id"] == '83e19a2f-4e45-40cb-83c9-eed127145bb3'

    assert response.status_code == 200
    assert len(result["products"]) == 8


def test_error_no_json(client):
    response = client.post(url, headers=headers)
    print response
    assert response.status_code == 400


def test_error_malformed_json(client):
    data = {"lng": "18.1733071804", "radius": "100", "tags": ""}
    response = client.post(url, data=json.dumps(data), headers=headers)
    assert response.status_code == 400
