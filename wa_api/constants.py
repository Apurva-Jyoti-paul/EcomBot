from ecom.settings import SOURCE, SRC_NAME, TOKEN

SEND_MSG_URL = 'https://api.gupshup.io/sm/api/v1/msg'
HEADERS = {
    'Cache-Control':'no-cache',
    'Content-Type':'application/x-www-form-urlencoded',
    'apikey':TOKEN,
}
PAYLOAD = {
    'channel':'whatsapp',
    'source':SOURCE,
    'src.name':SRC_NAME,
}