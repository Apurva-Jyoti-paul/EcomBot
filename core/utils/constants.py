from django.conf import settings

SEND_MSG_URL = 'https://api.gupshup.io/sm/api/v1/msg'

HEADERS = {
    'Cache-Control':'no-cache',
    'Content-Type':'application/x-www-form-urlencoded',
    'apikey':settings.TOKEN,
}

PAYLOAD = {
    'channel':'whatsapp',
    'source':settings.SOURCE,
    'src.name':settings.SRC_NAME,
}

MSG_TXT = {
    'type':'text',
}
MSG_LST = { # Has been modified to send 'products'.
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
MSG_QCK = {
    "type": "quick_reply",
    "msgid":"",
    "content":{},
    "options":[
        {
            "type":"text",
        },
        {
            "type":"text",
        },
        {
            "type":"text",
        },
    ]
}
MSG_IMG = {
    "type":"image",
    "originalUrl":"",
    "previewUrl":"",
    "caption":"",
    "filename":"",
}
