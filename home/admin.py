import secrets
import string
def generate_coupon_code(length=10, existing_codes=None):
    if existing_codes is None:
        existing_codes = set()
    while True:
        code = ''.join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(length))
        if code not in existing _codes:
            return code            