from add_contact import add_contact
from see_contact import see_contact
from see_all_contacts import see_all_contacts
from update_contact import update_contact
from delete_contact import delete_contact

contacts = []

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
    print("5. Mark as favorite contact")        # ✔️        
    print("6. Unmark as favorite contact")      # ✔️         
    print("7. See all favorite contacts")       # ✔️  
    print("8. See all non-favorite contacts")   # ✔️    
    print("9. Delete contact")                  # ✔️  
    print("10. Exit")                           # ✔️


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
        update_contact(contacts, ["name", "phone", "email", "is_favorite"])

    if user_choice == 5:
        update_contact(contacts, ["is_favorite"])

    if user_choice == 6:
        update_contact(contacts, ["is_favorite"])

    if user_choice == 7:
        see_all_contacts(contacts, ["favorite"])

    if user_choice == 8:
        see_all_contacts(contacts, ["non_favorite"])

    if user_choice == 9:
        delete_contact(contacts)

    if user_choice == 10:
        see_all_contacts(contacts)
        break

                       