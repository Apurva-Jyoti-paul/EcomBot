def from_html(html:str):
    return html


def _img_url_generator():

    from .constants import shopify
    images = [*shopify.EXAMPLE_IMG_URLS.jpg, *shopify.EXAMPLE_IMG_URLS.png]
    i = 0
    while True:
        yield images[i % len(images)]
        i += 1


img_url_generator = _img_url_generator()
