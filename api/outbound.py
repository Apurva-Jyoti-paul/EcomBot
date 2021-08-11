import json

import requests

from .constants import gupshup as _


def _set_params_and_post(dest:str, msg:dict, dispre:bool=False, url:str=_.SEND_MSG_URL, hdr:dict=_.HEADERS) -> requests.Response:
    """
    To set parameters appropriately and POST to url.

    :param dest: A  non-empty string representing the 12-digit destination phone number.
    :param msg: A dictionary representing the message parameter.
    :param dispre:(Optional, default: False) A bool for disablePreview parameter.
    :param url:(default: .constants.SEND_MSG_URL) A non-empty string representing the URL to POST. Useful when URL changes.
    :param hdr:(default: .constants.HEADERS) A dictionary representing the request headers. Useful when spec changes.
    :return: `Response <Response>` object.
    """

    _payload = _.PAYLOAD
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

    _msg = _.MSG_TXT
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

    _msg = _.MSG_LST
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

    _msg = _.MSG_QCK
    _msg['content'] = ctn

    for i,opt in enumerate(opts): # NOTE - Can only send three options
        _msg['options'].append({
            'type':'text',
            'title':opt['title'],
        })

    _r = _set_params_and_post(dest, _msg)

    return _r.status_code


def send_img_msg(dest:str, ourl:str, purl:str, caption:str='', filename:str='') -> int:
    """
    To send an image message

    :param dest: A  non-empty string representing the 12-digit destination phone number.
    :param ourl: A non empty string representing originalUrl parameter.
    :param purl: A non empty string representing previewUrl parameter.
    :param caption:(Optional) A string representing the caption to image message.
    :param filename:(Optional) A string representing the file name.
    :return: An integer, the status code of the response.

    Only JPG/PNG images are supported and besides only the following ones can be used to test, while being in the sandbox
    
    JPG
    https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample01.jpg
    https://www.buildquickbots.com/whatsapp/media/sample/jpg/sample02.jpg

    PNG
    https://www.buildquickbots.com/whatsapp/media/sample/png/sample01.png
    https://www.buildquickbots.com/whatsapp/media/sample/png/sample02.png
    """

    _msg = _.MSG_IMG
    _msg['originalUrl'] = ourl
    _msg['previewUrl'] = purl
    _msg['caption'] = caption
    _msg['filename'] = filename

    _r = _set_params_and_post(dest, _msg)

    return _r.status_code
