from base64 import b64encode
from collections import namedtuple

from django.conf import settings


def constant(f):
    def fset(self, value):
        raise TypeError('cannot assign to constants')
    def fget(self):
        return f(self)
    return property(fget, fset)


class _gupshup(object):

    @constant
    def SEND_MSG_URL(self):
        return 'https://api.gupshup.io/sm/api/v1/msg'
    
    @constant
    def HEADERS(self):
        return {
            'Cache-Control':'no-cache',
            'Content-Type':'application/x-www-form-urlencoded',
            'apikey':settings.TOKEN,
        }

    @constant
    def PAYLOAD(self):
        return {
            'channel':'whatsapp',
            'source':settings.SOURCE,
            'src.name':settings.SRC_NAME,
        }
    
    @constant
    def MSG_TXT(self):
        return {
            'type':'text',
        }

    @constant
    def MSG_LST(self):
        return {
            "type":"list",
            "title":"",
            "body":"",
            "msgid":"",
            "globalButtons":[
                {
                    "type":"text",
                    "title":"",
                }
            ],
            "items":[
                {
                    "title":"",
                    "subtitle":"",
                    "options":[]
                },

            ]
        }

    @constant
    def MSG_QCK(self):
        return {
            "type": "quick_reply",
            "content":{},
            "options":[]
        }

    @constant
    def MSG_IMG( self):
        return {
            "type":"image",
            "originalUrl":"",
            "previewUrl":"",
            "caption":"",
            "filename":"",
        }


class _shopify(object):

    @constant
    def PRODUCTS_URL(self):
        return f'https://{settings.SHOPIFY_SHOP}.myshopify.com/admin/api/2021-07/products.json'

    @property
    def AUTH(self):
        return b64encode(f'{settings.SHOPIFY_API}:{settings.SHOPIFY_PWD}'.encode()).decode()

    @constant
    def HEADERS(self):
        return {
            'Content-Type':'application/json',
            'Authorization':f'Basic {self.AUTH}'
        }

    @constant
    def EXAMPLE_IMG_URLS(self):
        return namedtuple('images', ['jpg', 'png'])(
            [
                'https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg',
                'https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample02.jpg',
            ],
            [
                'https://www.buildquickbots.com/whatsapp/media/sample/png/sample01.png',
                'https://www.buildquickbots.com/whatsapp/media/sample/png/sample02.png',
            ]
        )


gupshup = _gupshup()
shopify = _shopify()