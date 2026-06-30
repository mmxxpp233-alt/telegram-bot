import io

import qrcode


def generate_qr(text: str):
    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    buffer.seek(0)

    return buffer
