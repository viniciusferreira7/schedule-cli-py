from add_contact import add_contact
from see_contact import see_contact
from see_all_contacts import see_all_contacts
from update_contact import update_contact

contacts = [
    {
        "name": "Alice",
        "phone": "(11) 91234-5678",
        "email": "alice@example.com",
        "is_favorite": False,
        "created_at": "2025-01-18 16:05:42",
        "updated_at": "2025-01-18 16:05:42"
    },
    {
        "name": "Bob",
        "phone": "(21) 98765-4321",
        "email": "bob@example.com",
        "is_favorite": False,
        "created_at": "2025-01-18 16:05:42",
        "updated_at": "2025-01-18 16:05:42"
    },
    {
        "name": "Charlie",
        "phone": "(31) 93456-7890",
        "email": "charlie@example.com",
        "is_favorite": False,
        "created_at": "2025-01-18 16:05:42",
        "updated_at": "2025-01-18 16:05:42"
    },
    {
        "name": "Diana",
        "phone": "(41) 94567-1234",
        "email": "diana@example.com",
        "is_favorite": False,
        "created_at": "2025-01-18 16:05:42",
        "updated_at": "2025-01-18 16:05:42"
    },
    {
        "name": "Eve",
        "phone": "(51) 93210-5432",
        "email": "eve@example.com",
        "is_favorite": False,
        "created_at": "2025-01-18 16:05:42",
        "updated_at": "2025-01-18 16:05:42"
    }
]

name = None
loops = 0

while True:
    loops +=1

    if not name:
        name = input("Enter with your name: ").strip()

    if not name:
        print("Please enter with your name ")
        continue

    if loops <= 1:
        print(f"\n-----------Welcome {name}------------")


    
    print("\nManager menu phone book:")
    print("\n1. Add contact")                   # ✔️
    print("2. See contact")                     # ✔️
    print("3. See all contacts")                # ✔️
    print("4. Update contact")                  # ✔️
    print("5. Favorite contact")               
    print("6. Mark as favorite contact")               
    print("7. Unmark as favorite contact")               
    print("8. See all favorite contacts")         
    print("9. See all non-favorite contacts")        
    print("10. Delete contact")                 
    print("11. Exit")


    choice = 0

    try:
        user_choice = int(input("\nEnter with your choice: "))
        choice = user_choice
    except:
        print("\n-----------Error------------")
        print("\nPlease only provide numbers.")
        print("\n-----------Error------------")
        continue

    if user_choice == 1:
        add_contact(contacts)

    if user_choice == 2:
        see_contact(contacts)

    if user_choice == 3:
        see_all_contacts(contacts)

    if user_choice == 4:
        update_contact(contacts)

    if user_choice == 11:
        see_all_contacts(contacts)
        break

                       