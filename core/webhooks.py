from os import getenv

from rest_framework import status

from api.outbound import send_img_msg, send_lst_msg, send_qck_msg, send_txt_msg

if getenv('API') is not None:
    api = __import__(f"api.{getenv('API')}", fromlist=['api'])
else:
    raise ValueError('API provider name cannot be None')


def _send_product(dest:str, name:str, reply_button:bool=False):

    print(product := api.get_product(name))

    if product.id == -1:
        return status.HTTP_404_NOT_FOUND

    if product.image_url == 'NO_IMAGE_URL':
        if reply_button:
            ctn = {
                'type' : 'text',
                'text' : product.title,
                'caption' : product.description,
            }
            opt = {
                'type' : 'text',
                'title' : 'View More',
            }
            return send_qck_msg(dest, ctn, [opt])
        return send_txt_msg(dest, product.payload)
    else:
        if reply_button:
            ctn = {
                'type' : 'image',
                'url' : product.image_url,
                'caption' : product.payload,
            }
            opt = {
                'type' : 'text',
                'title' : 'View More'
            }
            return send_qck_msg(dest, ctn, [opt])
        return send_img_msg(dest, product.image_url, product.image_url, product.payload)


def send_template(dest:str, tmp:str, disPre:bool=False) -> int:
    """To send the first template message"""

    return send_txt_msg(dest, tmp, disPre)


def send_products(dest:str, keyword:str):

    # TODO - To generate a list of Products based on keyword
    sent = []
    for _ in range(4):
        sent.append(_send_product(dest, ['Leather Wallet', 'Smart Phone', 'Pizza'][_ % 3]))
    sent.append(_send_product(dest, 'Leather Wallet', True))
    if set(sent) == {status.HTTP_200_OK}:
        return status.HTTP_200_OK
    else:
        return status.HTTP_417_EXPECTATION_FAILED
