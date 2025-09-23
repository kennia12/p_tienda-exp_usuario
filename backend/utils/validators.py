# backend/utils/validators.py

import re

def is_valid_email(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email)

def is_valid_password(password):
    return len(password) >= 6

def is_valid_price(price):
    try:
        return float(price) > 0
    except:
        return False
