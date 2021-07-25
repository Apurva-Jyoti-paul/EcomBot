import json

import requests

from .constants import HEADERS, PAYLOAD, SEND_MSG_URL

DISABLE_PREVIEW = False


def send_text(msg:str, dest:str, disPre:bool=False) -> int:
    """
    :param msg: A string representing the message to be sent (max 4096 char).
    :param dest: A 12-digit phone number string.
    :param disPre: A bool for disablePreview (default: False).
    :return: An integer, the status code of the response.
    """
    _message = {
        'type':'text',
        'text':msg,
    }
    _payload = PAYLOAD
    _payload['destination'] = dest
    _payload['message'] = json.dumps(_message)
    _payload['disablePreview'] = disPre

    _r = requests.post(
        url=SEND_MSG_URL,
        data=_payload,
        headers=HEADERS,
    )

    return _r.status_code


def send_template(tmp:str, dest:str, disPre:bool=False) -> int:
    """
    :param tmp: A string representing the template to be sent (max 4096 char).
    :param dest: A 12-digit phone number string.
    :param disPre: A bool for disablePreview (default: False).
    :return: An integer, the status code of the response.
    """
    return send_text(
        msg=tmp,
        dest=dest,
        disPre=disPre,
    )

def send_categories():
    # TODO - GET the categories and send to the client
    pass


def send_products():
    # TODO - GET the products and make logic for recurring product list and/or top 5 product list
    pass
