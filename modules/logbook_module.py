
from PIL import Image, ImageEnhance
import pytesseract
import re

pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

def preprocess_image(image):
    image = image.convert("L")
    enhancer = ImageEnhance.Contrast(image)
    return enhancer.enhance(2.0)

def extract_logbook_data(image):
    image = preprocess_image(image)
    text = pytesseract.image_to_string(image)

    date = re.search(r"\d{2}/\d{2}/\d{4}", text)
    mileage = re.search(r"\d+\s*km", text)
    vehicle_id = re.search(r"[A-Z0-9]{6,}", text)

    return {
        "date": date.group(0) if date else None,
        "mileage": mileage.group(0) if mileage else None,
        "vehicle_id": vehicle_id.group(0) if vehicle_id else None
    }

def cross_check_logbook(vehicle_id):
    fake_db = ["ABC1234", "XYZ5678"]
    return vehicle_id in fake_db
