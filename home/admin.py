import logging
from django.core.validators.import validate_email
from django.core.exceptions import ValidationError
def validate_email_address(email):
    try:
        validate_email(email)
        return True
    except ValidationError as e:
        logging.error(f"Invalid email address '{email}':{e}")
        return False 
fro utils.validation_utils import validate_email_address
email = "example@example.com"
is_valid = validate_email_address(email)
print(is_valid)                 