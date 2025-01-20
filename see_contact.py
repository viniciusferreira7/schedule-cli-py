from typing import List, Dict

from validation import validate_text
from find_contact import find_contact

def see_contact(contacts: List[Dict[str, str]]):
    idx_or_name = input("Enter with number or name of the contact: ")
    validate_text(idx_or_name)

    contact = find_contact(idx_or_name, contacts)

    index = contacts.index(contact)

    print(f"{"⭐" if contact["is_favorite"] else " "} \n{index + 1}. name: {contact["name"]}, phone: {contact["phone"]}, email: {contact["email"]}, created at: {contact["created_at"]}, updated at: {contact["updated_at"]}")

    

