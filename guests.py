import json
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def load_guests():
    """Loads guest-list into memory"""
    if os.path.exists(f"{BASE_DIR}/guests.json"):
        with open(f"{BASE_DIR}/guests.json", "r", encoding="utf-8") as f:
            guests = json.load(f)
    else:
        with open(f"{BASE_DIR}/guests.json", "w", encoding="utf-8") as f:
            guests = {
    "guests": 
    [
        
    ]
}
            json.dump(guests, f, indent=4)
    return guests


def show_list(guest_list: dict):
    """Shows guest-list in readable form"""
    guest_num = 0
    print("Guests:\n")
    for guest in guest_list["guests"]:
        guest_num += 1
        print(f"{guest_num}. {guest}")


def add_guest(guest_list: dict):
    """Adds guest to the end of the guest listt"""
    new_guest = input("\nNew guest's name: ")
    guest_list["guests"].append(new_guest)
    auto_save(guest_list)
    print(f"Added: {new_guest} to guest-list")
    print(f"Updated list:\n")
    show_list(guest_list)


def remove_guest(guest_list: dict):
    """Removes a chosen guest from the guest-list"""
    r_guest = input("\nRemove guest from guest-list: ")
    safety_question = input(f"Are you sure you want to remove: {r_guest}\n")
    if normalize(safety_question) == "yes" or normalize(safety_question) == "y":
        for guest in guest_list["guests"]:
            if normalize(r_guest) == normalize(guest):
                guest_list["guests"].remove(guest)
                print(f"Guest: {r_guest} successfully removed from guest-list")
        if r_guest not in guest_list["guests"] or normalize(r_guest) not in guest_list["guests"]:
            print("Guest not found. Please check for typo-s!")
    auto_save(guest_list)  
    print(f"Updated list:")
    show_list(guest_list)



def auto_save(guest_list: dict):
    """Automatic save feature used in remove and add func"""
    with open(f"{BASE_DIR}/guests.json", "w", encoding="utf-8") as f:
        json.dump(guest_list, f, indent=4)

# Plus, QOL functions made from needs, not from plans
def normalize(string: str):
    """Normalizes strings"""
    return string.lower().strip()

def information():
    """About the program"""
    print("About:" \
    "This program is a guest-list manager. It was made for learning purposes," \
    " to be more specific, learning about handling json files, github and venv," \
    " so it does not use a database")


guest_list = load_guests()



def main():
    print("Welcome!\n HOW TO USE: write the name or first letter of the option you want to choose!")
    in_options_menu = True
    while in_options_menu:
        option = input("\nPlease select an action: \nShow;\t Add;\t Remove;\t Information;\t  Exit\n")
        
        if normalize(option) == "show" or normalize(option) == "s":
            show_list(guest_list)

        if normalize(option) == "add" or normalize(option) == "a":
            add_guest(guest_list)

        if normalize(option) == "remove" or normalize(option) == "r":
            remove_guest(guest_list)

        if normalize(option) == "information" or normalize(option) == "i":
            information()
        
        if normalize(option) == "exit" or normalize(option) == "e":
            exit()
            

if __name__ == "__main__":
    main()