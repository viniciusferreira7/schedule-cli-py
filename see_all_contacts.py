from typing import List, Dict

def see_all_contacts(contacts: List[Dict[str, str]]):
    print("\n-----------My contacts------------")
    for idx, contact in enumerate(contacts):
        print(f"{"⭐" if contact["is_favorite"] else " "} {idx + 1}. name: {contact["name"]}, phone: {contact["phone"]}, email: {contact["email"]}, created at: {contact["created_at"]}, updated at: {contact["updated_at"]}")
        print("\n-------------------------------")