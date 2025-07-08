
# import psycopg2
from datetime import datetime
import os

# def get_connection():
#     return psycopg2.connect(
#         host=os.getenv("DB_HOST"),
#         dbname=os.getenv("DB_NAME"),
#         user=os.getenv("DB_USER"),
#         password=os.getenv("DB_PASS")
#     )

# def verify_cert(cert_id):
#     conn = get_connection()
#     cur = conn.cursor()
#     cur.execute("SELECT name, expiry_date FROM certifications WHERE certification_id=%s", (cert_id,))
#     result = cur.fetchone()
#     conn.close()
#     if result:
#         expiry = result[1]
#         if expiry < datetime.today().date():
#             return False, f"Expired on {expiry}"
#         return True, f"Valid until {expiry}"
#     return False, "Not found"

def verify_cert(cert_id):
    """
    Mock certification verification for Streamlit Cloud.
    Simulates a simple database lookup.
    """
    mock_db = {
        "CERT123": "Valid until 2026-12-31",
        "CERT456": "Valid until 2025-06-30",
        "CERT789": "Expired",
        "CERT101": "Invalid",
        "CERT202": "Valid until 2027-01-20"
    }

    result = mock_db.get(cert_id)

    if result:
        # Simulate expired status
        if "Expired" in result or "Invalid" in result:
            return False, result
        return True, result
    else:
        return False, "Certification not found in mock database"
