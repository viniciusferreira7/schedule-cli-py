from typing import List, Dict

def see_all_contacts(contacts: List[Dict[str, str]], filter_type: List[str]):
    print("\n-----------My contacts------------")
    
    if "favorite" in filter_type:
        for idx, contact in enumerate(contacts):
            if contact["is_favorite"]:
                print(f"{'⭐' if contact['is_favorite'] else ' '} {idx + 1}. name: {contact['name']}, phone: {contact['phone']}, email: {contact['email']}, created at: {contact['created_at']}, updated at: {contact['updated_at']}")
                print("\n-------------------------------")
    
    elif "non_favorite" in filter_type:
        for idx, contact in enumerate(contacts):
            if not contact["is_favorite"]:
                print(f"{'⭐' if contact['is_favorite'] else ' '} {idx + 1}. name: {contact['name']}, phone: {contact['phone']}, email: {contact['email']}, created at: {contact['created_at']}, updated at: {contact['updated_at']}")
                print("\n-------------------------------")

    else:
        for idx, contact in enumerate(contacts):
            print(f"{'⭐' if contact['is_favorite'] else ' '} {idx + 1}. name: {contact['name']}, phone: {contact['phone']}, email: {contact['email']}, created at: {contact['created_at']}, updated at: {contact['updated_at']}")
            print("\n-------------------------------")