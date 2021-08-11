from os import environ

from .shopify import validate as shopify_validate


def validate_credentials(api:str):

    if api == 'shopify':
        return shopify_validate()


def load(instance):

    environ['API'] = instance.api
    API = instance.api.upper()
    if API == 'SHOPIFY':
        environ[f'{API}_API_KEY'] = instance.api_key
        environ[f'{API}_API_PWD'] = instance.api_pwd
        environ[f'{API}_SHOP'] = instance.shop
