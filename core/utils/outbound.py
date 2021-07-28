import json

import requests

from .constants import (HEADERS, MSG_LST, MSG_QCK, MSG_TXT, PAYLOAD,
                        SEND_MSG_URL)


def _set_params_and_post(dest:str, msg:dict, dispre:bool=False, url:str=SEND_MSG_URL, hdr:dict=HEADERS) -> requests.Response:
    """
    To set parameters appropriately and POST to url.

    :param dest: A  non-empty string representing the 12-digit destination phone number.
    :param msg: A dictionary representing the message parameter.
    :param dispre:(Optional, default: False) A bool for disablePreview parameter.
    :param url:(default: .constants.SEND_MSG_URL) A non-empty string representing the URL to POST. Useful when URL changes.
    :param hdr:(default: .constants.HEADERS) A dictionary representing the request headers. Useful when spec changes.
    :return: `Response <Response>` object.
    """

    _payload = PAYLOAD
    _payload['destination'] = dest
    _payload['message'] = json.dumps(msg)

    if dispre: _payload['disablePreview'] = dispre

    return requests.post(url = url, data = _payload, headers = hdr)


def send_txt_msg(dest:str, msgstr:str, dispre:bool=False) -> int:
    """
    To send a simple message.

    :param dest: A  non-empty string representing the 12-digit destination phone number.
    :param msgstr: A non-empty string representing the message to be sent (max 4096 char).
    :param dispre:(Optional, default: False) A bool for disablePreview parameter.
    :return: An integer, the status code of the response.
    """

    _msg = MSG_TXT
    _msg['text'] = msgstr

    _r = _set_params_and_post(dest, _msg, dispre)

    return _r.status_code


def send_lst_msg(dest:str, titlebody:tuple, opts:list, btntitle:str='View Products') -> int:
    """
    To send a message with List.

    :param dest: A  non-empty string representing the 12-digit destination phone number.
    :param titlebody: A tuple containing non-empty string representing title and body respectively.
    :param opts: A list of dictionaries representing options.
    Each item in the list should contain only non-empty string values for `title`,`postbackText` keys and optionally for `description` key.
    :param btntitle: A non-empty string representing the text of the button (max 20 char).
    :return: An integer, the status code of the response.
    """

    _msg = MSG_LST
    _msg['title'], _msg['body'] = titlebody
    _msg['msgid'] = 'somade_thing_asdfqwert' # will be recieved back through a hook I guess # NOTE - I think this should be unique
    _msg['globalButtons'][0]['title'] = btntitle

    _options:list = _msg['items'][0]['options']

    for i,opt in enumerate(opts):
        _options.append({
            'type':'text',
            'title':opt['title'],
            'description':opt.get('description', ''),
            'postbackText':opt['postbackText']
        })

    _r = _set_params_and_post(dest, _msg)

    return _r.status_code



def send_qck_msg(dest:str, ctn:dict, opts:list) -> int:
    """
    To send a message with Quick reply buttons.

    :param dest: A  non-empty string representing the 12-digit destination phone number.
    :param ctn: A dict representing the message content to be sent (text|image|video|document).
    :param opts: A list of dictionaries representing options.
    Each item in the list should contain only non-empty string values for `title` and `postbackText` keys.
    Can only send up to 3 options.
    :return: An integer, the status code of the response.
    """

    _msg = MSG_QCK
    _msg['msgid'] = 'some_thing' # NOTE - Will be recieved back through a hook I guess
    _msg['content'] = ctn

    for i,opt in enumerate(opts): # NOTE - Can only send three options
        _msg['options'][i] = {
            'type':'text',
            'title':opt['title'],
            'postbackText':opt['postbackText']
        }

    _r = _set_params_and_post(dest, _msg)

    return _r.status_code
