from PIL import Image, ImageEnhance
import re

# ✅ Uncomment only if running locally or with Docker that has Tesseract installed:
import pytesseract
pytesseract.pytesseract.tesseract_cmd = '/usr/bin/tesseract'

# ✅ Toggle: True = use real OCR | False = use mock
USE_REAL_OCR = False

def extract_logbook_data(image):
    """
    Use real Tesseract OCR or a mock, based on toggle.
    """
    if USE_REAL_OCR:
        # -------------------------
        # ✅ Real OCR version
        # -------------------------
        # Convert to grayscale
        image = image.convert("L")
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(2.0)
        
        text = pytesseract.image_to_string(image)

        date = re.search(r"\d{2}/\d{2}/\d{4}", text)
        mileage = re.search(r"\d+\s*km", text)
        vehicle_id = re.search(r"[A-Z0-9]{6,}", text)

        return {
            "date": date.group(0) if date else None,
            "mileage": mileage.group(0) if mileage else None,
            "vehicle_id": vehicle_id.group(0) if vehicle_id else None,
            "raw_text": text
        }
    else:
        # -------------------------
        # ✅ Mock version for Streamlit Cloud
        # -------------------------
        return {
            "date": "01/07/2025",
            "mileage": "12345 km",
            "vehicle_id": "ABC1234",
            "raw_text": "Mock OCR result for Streamlit Cloud"
        }

def cross_check_logbook(vehicle_id):
    """
    Simple registry check.
    """
    fake_db = ["ABC1234", "XYZ5678"]
    return vehicle_id in fake_db
