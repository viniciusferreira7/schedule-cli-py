from typing import List, Dict
from validation import validate_text
from find_contact import find_contact

def delete_contact(contacts: List[Dict[str, str]]):
    idx_or_name = input("\nEnter with number or name of the contact: ")
    validate_text(idx_or_name)

    contact = find_contact(idx_or_name, contacts)
    index = contacts.index(contact)

    contacts.pop(index)

    print("Contact is removed successfully!")