from os import getenv
from urllib.parse import urlparse

import requests

from .classes import Product
from .constants import shopify as _
from .utils import from_html, img_url_generator


def validate():
    return True

def get_products():
    ...

def get_product(name:str):

    query = {
        'title':name,
        'limit':250,
        'fields':'id,title,body_html,handle,image'
    }
    _r = requests.get(
        url = _.PRODUCTS_URL,
        headers = _.HEADERS,
        params = query
    ).json().get('products')

    if len(_r) == 0:
        return Product(
            id = -1,
            name = 'not found',
            description = 'not found',
            buy_url = 'not found',
            image_url = 'not found'
        )

    _r = _r[0]

    return Product(
        id = _r['id'],
        name = _r['title'],
        description = from_html(_r['body_html']),
        buy_url = f'https://{urlparse(_.PRODUCTS_URL).netloc}/products/{_r["handle"]}',
        image_url = f'{next(img_url_generator) if getenv("USE_SAMPLE_IMAGE_URLS") else _r["image"]["src"] if _r["image"] is not None else "NO_IMAGE_URL"}',
    )
