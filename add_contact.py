from datetime import datetime

from validation import validate_text, validate_phone, validate_email

from typing import List, Dict

def add_contact(contacts: List[Dict[str, str]]):
    name = input("Enter with contact's name: ")
    validate_text(name)

    phone = input("Enter with contact's phone: ")
    validate_text(phone)

    is_validated_phone = validate_phone(phone)

    if not is_validated_phone:
        print("\n-----------Error:------------")
        print(f"\nExample of valid format: (99) 99999-9999")
        print("----------------------------------")


    email = input("Enter with contact's email: ")
    validate_text(email)

    is_validated_email = validate_email(email)
    
    if not is_validated_email:
        print("\n-----------Error:------------")
        print(f"Invalid Email: {email}")
        print(f"\nExample of valid format: john.doe@example.com")
        print("----------------------------------")

    
    contacts.append({
        "name": name,
        "phone": phone,
        "email": email,
        "is_favorite": False,
        "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"), 
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    })

    print("\n-----------Contact added successfully ✔️ ------------")
    print(f"name: {name}, phone: {phone}, email: {email}")

