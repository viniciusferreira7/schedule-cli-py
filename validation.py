import re

def validate_text(text, message=None): 
     if not str(text).strip():
        print("Invalid text" if not message else message)
        return 

def validate_phone(phone: str) -> bool:
    phone_regex = r'^\(?\d{2}\)?[\s.-]?\d{4,5}[\s.-]?\d{4}$'
    return bool(re.match(phone_regex, phone))

def validate_email(email: str) -> bool:
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return bool(re.match(email_regex, email))