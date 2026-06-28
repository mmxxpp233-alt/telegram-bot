from io import BytesIO

import qrcode
from PIL import Image


def create_qr(text: str) -> BytesIO:
    """
    إنشاء QR من نص
    """

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_M,
        box_size=10,
        border=4,
    )

    qr.add_data(text)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()

    image.save(buffer, format="PNG")

    buffer.seek(0)

    return buffer

from io import BytesIO

import cv2
import numpy as np


def read_qr(image_bytes: bytes) -> str | None:
    """
    قراءة QR من صورة
    """

    image = np.frombuffer(image_bytes, dtype=np.uint8)

    image = cv2.imdecode(image, cv2.IMREAD_COLOR)

    detector = cv2.QRCodeDetector()

    data, points, _ = detector.detectAndDecode(image)

    if points is None:
        return None

    if not data:
        return None

    return data

