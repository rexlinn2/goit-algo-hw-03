import re

def normalize_phone(phone_number):
    phone_number = phone_number.strip()
    
    phone_number = re.sub(r"[^\d+]", "", phone_number)
    
    if phone_number.startswith("+"):
        return phone_number
    
    if phone_number.startswith("380"):
        return "+" + phone_number
    
    return "+38" + phone_number

print(normalize_phone("    +38(050)123-32-34"))