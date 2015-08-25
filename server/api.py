# -*- coding: utf-8 -*-

import time
from flask import Blueprint, current_app, jsonify
from flask import request, current_app
from products_controller import ProductsController
from server.service.products_service import ProductsService
from server.service.shops_service import ShopsService
from server.service.tags_service import TagsService
from server.repository.products_repository import ProductsRepository
from server.repository.shops_repository import ShopsRepository
from server.repository.tags_repository import TagsRepository
from server.repository.tagging_repository import TaggingRepository
from werkzeug.exceptions import abort

api = Blueprint('api', __name__)


def data_path(filename):
    data_path = current_app.config['DATA_PATH']
    return u"%s/%s" % (data_path, filename)


geo_hash_size = 6
tags_service = TagsService(TagsRepository('data/tags.csv'), TaggingRepository('data/taggings.csv'))
shops_repository = ShopsRepository('data/shops.csv', geo_hash_size)
shops_service = ShopsService(shops_repository, tags_service, geo_hash_size)
products_service = ProductsService(ProductsRepository('data/products.csv'), shops_repository)

controller = ProductsController(shops_service, products_service)


@api.route('/search', methods=['POST'])
def search():
    if not request.json or not 'lat' in request.json or not 'lng' in request.json or not 'radius' in request.json:
        print 'malformed json'
        abort(400, 'malformed json request in search service')

    requestdata = request.get_json()
    count = int(requestdata['count'])
    lat = float(requestdata['lat'])
    long = float(requestdata['lng'])
    rangesearch = int(requestdata['radius'])
    tags = requestdata['tags']

    start_time = time.clock()
    products_list = controller.get_products_list(lat, long, rangesearch, tags, count)
    print('*total time: ' + str(time.clock() - start_time) + " seconds")
    print('*items found: ' + str(len(products_list)))

    return jsonify({
        'time': str(time.clock() - start_time) + " seconds",
        'products': [e.serialize() for e in products_list]})
