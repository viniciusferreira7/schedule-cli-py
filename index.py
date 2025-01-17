from add_contact import add_contact

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
    print("2. See contact")                    
    print("3. See all contacts")               
    print("4. Update contact")                 
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

    if user_choice == 11:
        print("\n-----------My contacts------------")
        for idx, contact in enumerate(contacts):
            print(f"{"⭐" if contact["is_favorite"] else " "} \n{idx + 1}. name: {contact["name"]}, phone: {contact["phone"]}, email: {contact["email"]}, created at: {contact["created_at"]}, updated at: {contact["updated_at"]}")
        print("\n-------------------------------")
        break

                       