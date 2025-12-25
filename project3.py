import json
import os

def add_person():
    name = input("Name: ")
    age = input("Age: ")
    email = input("Email: ")
    person = {"name": name, "age": age, "email": email}
    return person

def display_people(people):
    if not people:
        print("No contacts found.")
        return
    
    for i, person in enumerate(people):
        print(i + 1, "-", person["name"], "|", person["age"], "|", person["email"])

def delete_contact(people):
    display_people(people)
    if not people:
        return
    
    while True:
        number = input("Enter a number to delete: ")
        try:
            number = int(number)
            if number <= 0 or number > len(people):
                print("Invalid number, out of range.")
            else:
                break
        except ValueError:
            print("Invalid number, must be an integer.")
    
    people.pop(number - 1)
    print("Person deleted.")

def search(people):
    search_name = input("Search for a name: ").lower()
    results = [person for person in people if search_name in person["name"].lower()]
    
    if results:
        display_people(results)
    else:
        print("No contacts found matching that name.")

print("Hi, welcome to the Contact Management System.\n")

# Load contacts safely
if os.path.exists("contacts.json"):
    with open("contacts.json", "r") as f:
        people = json.load(f).get("contacts", [])
else:
    people = []

while True:
    print("\nContact list size:", len(people))
    command = input("You can 'Add', 'Delete', 'Search', or 'Q' to quit: ").lower()
    
    if command == "add":
        person = add_person()
        people.append(person)
        print("Person added!")
    elif command == "delete":
        delete_contact(people)
    elif command == "search":
        search(people)
    elif command == "q":
        break
    else:
        print("Invalid command.")

# Save contacts
with open("contacts.json", "w") as f:
    json.dump({"contacts": people}, f, indent=4)