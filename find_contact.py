from typing import List, Dict

def find_contact(idx_or_name, contacts: List[Dict[str, str]]):
    print(f"idx_or_name: {idx_or_name}")
    try:
        contact_idx = int(idx_or_name) - 1  
        print(f"contact_idx: {contact_idx}")

        if contact_idx >= len(contacts) or contact_idx < 0:
            print("Índice fora do alcance.")
            return None

        return contacts[contact_idx]
    
    except ValueError:
        name = idx_or_name.lower()  
        
        my_contact = next((item for item in contacts if "name" in item and item["name"].lower() == name), None)

        if not my_contact:
            print("Contato não encontrado pelo nome.")
            return None
        else:
            return my_contact
