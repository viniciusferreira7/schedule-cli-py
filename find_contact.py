from typing import List, Dict

def find_contact(idx_or_name, contacts: List[Dict[str, str]]):
    try:
        contact_idx = int(idx_or_name) - 1  

        if contact_idx >= len(contacts) or contact_idx < 0:
            print("Contact not found by number.")

            return None

        return contacts[contact_idx]
    
    except ValueError:
        name = idx_or_name.lower()  
        
        my_contact = next((item for item in contacts if "name" in item and item["name"].lower() == name), None)

        if not my_contact:
            print("Contact not found by nome.")
            return None
        else:
            return my_contact
