from .outbound import send_lst_msg, send_qck_msg, send_txt_msg


def send_template(dest:str, tmp:str, disPre:bool=False) -> int:
    """To send the first template message"""

    return send_txt_msg(dest, tmp, disPre)


def send_categories():
    # TODO - GET the categories and send to the client
    pass


def send_products():
# TODO - GET the products and make logic for recurring product list and/or top 5 product     list
    pass
