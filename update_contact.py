from datetime import datetime
from typing import List, Dict
from validation import validate_text, validate_phone, validate_email
from find_contact import find_contact

def make_a_question(message: str) -> str:
    answer = input(f"{message} (y/n): ")
    validate_text(answer)
    
    if not (answer.lower() == 'y' or answer.lower() == 'n'):
        print("Only yes (y) or no (n)")
        return make_a_question(message)  
    
    return answer.lower()


def update_field(contact: Dict[str, str], field_name: str, field_value: str, index: int, contacts: List[Dict[str, str]]):
    contact[field_name] = field_value
    contact["updated_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    contacts[index] = contact  


def update_contact(contacts: List[Dict[str, str]],  update_fields_list: List[str]):
    idx_or_name = input("\nEnter with number or name of the contact: ")
    validate_text(idx_or_name)

    contact = find_contact(idx_or_name, contacts)
    index = contacts.index(contact)

    print(f"{"⭐" if contact['is_favorite'] else ' '} {index + 1}. name: {contact['name']}, phone: {contact['phone']}, email: {contact['email']}, created at: {contact['created_at']}, updated at: {contact['updated_at']}")

    
    if "name" in update_fields_list and make_a_question("\nYou want to update name") == 'y':
        updated_name = input("Enter with new name: ")
        validate_text(updated_name)
        update_field(contact, "name", updated_name, index, contacts)

    
    if  "phone" in update_fields_list and make_a_question("\nYou want to update phone") == 'y':
        updated_phone = input("Enter with new phone: ")
        validate_text(updated_phone)

        if not validate_phone(updated_phone):
            print("\n-----------Error:------------")
            print(f"\nExample of valid format: (99) 99999-9999")
            print("----------------------------------")
            return

        update_field(contact, "phone", updated_phone, index, contacts)

    
    if  "email" in update_fields_list and make_a_question("\nYou want to update email") == 'y':
        updated_email = input("Enter with new email: ")
        validate_email(updated_email)  
        update_field(contact, "email", updated_email, index, contacts)

    if "is_favorite" in update_fields_list and contact["is_favorite"] == False and make_a_question("\nYou want to mark favorite contact") == 'y':
        update_field(contact, "is_favorite", True, index, contacts)

        print("\nUpdated contact details:")
        updated_contact = contacts[index]
        print(f"{'⭐' if updated_contact['is_favorite'] else ' '} {index}. name: {updated_contact['name']}, phone: {updated_contact['phone']}, email: {updated_contact['email']}, created at: {updated_contact['created_at']}, updated at: {updated_contact['updated_at']}")

        return 

    if "is_favorite" in update_fields_list and contact["is_favorite"] == True and make_a_question("\nYou want to unmark favorite contact") == 'y':
        update_field(contact, "is_favorite", False, index, contacts)

        print("\nUpdated contact details:")
        updated_contact = contacts[index]
        print(f"{'⭐' if updated_contact['is_favorite'] else ' '} {index}. name: {updated_contact['name']}, phone: {updated_contact['phone']}, email: {updated_contact['email']}, created at: {updated_contact['created_at']}, updated at: {updated_contact['updated_at']}")

        return 
    
