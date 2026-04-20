# Python program to create a database of names and phone numbers using a dictionary

def phonebook():
   contacts = {}

   while True:
      print("\nPhonebook Menu:",
            "\n1.Add Contact",
            "\n2.Retrieve Contacts",
            "\nDisplay all contacts",
            "\n4.Exit")
      choice = input("Enter your choice from 1 to 4:")

      if choice == "1":
       name = input("Enter name:")
       phone = input("Enter phone number:")
       contacts[name] = phone
       print(f"Contact added: {name} _ {phone}")

      elif choice == "2":
       name = input("Enter name to retrieve:")
       if name in contacts:
         print(f"{name}'s phone number is {contacts[name]}")
       else:
         print("Contact is not found")

      elif choice == "3":
       if contacts:
        print("\nAll Contacts:")
        for name, phone in contacts.items():
         print(f"{name}: {phone}")

       else:
        print("phonebook is empty")

      elif choice == "4":
       print("Exiting phonebook")
       break
      else:
       print("Invalid choice. Place select a valid option")

# Main Routine
phonebook()
