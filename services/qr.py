from pyzbar.pyzbar import decode
from PIL import Image


def read_qr(path):
    img = Image.open(path)
    data = decode(img)

    if not data:
        return None

    return data[0].data.decode("utf-8")
