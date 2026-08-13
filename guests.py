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
            guests = {"guests": []}
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
    if r_guest not in guest_list["guests"] and normalize(r_guest) not in guest_list["guests"]:
        best_distance = float('inf')
        best_name = None
        cutoff = 0.1
        for guest in guest_list["guests"]:
            guest_distance = levenshtein(r_guest, guest)
            if guest_distance < best_distance:
                best_distance = guest_distance
                best_name = guest
        ratio = best_distance / ((len(best_name) + len(r_guest))/2)
        if ratio <= cutoff or best_distance == 1:
            not_found = input(f"Guest not found! Did you think of: {best_name}?\n")
            if normalize(not_found) == "yes" or normalize(not_found) == "y":
                guest_list["guests"].remove(best_name)
                print(f"Guest: {best_name} successfully removed from guest-list")
        else:
            print("No similar guests found!")
    else:
        safety_question = input(f"Are you sure you want to remove: {r_guest}\n")
        if normalize(safety_question) == "yes" or normalize(safety_question) == "y":
            for guest in guest_list["guests"]:
                if normalize(r_guest) == normalize(guest):
                    guest_list["guests"].remove(guest)
                    print(f"Guest: {r_guest} successfully removed from guest-list")
        
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

def levenshtein(A, B):
    grid = [[0 for c in range(len(B)+1) ] for r in range(len(A)+1)]
    for row in range(len(grid)):
        grid[row][0] = row 
    for col in range(len(grid[0])):
        grid[0][col] = col
    for row in range(1, len(grid)):
        for column in range(1, len(grid[0])):
            if A[row-1] == B[column-1]:
                grid[row][column] = grid[row-1][column-1]
            else:
                grid[row][column] = 1 + min(grid[row-1][column-1], grid[row-1][column], grid[row][column-1])
    return grid[-1][-1]


guest_list = load_guests()


def main():
    print("Welcome!\n HOW TO USE: write the name or first letter of the option you want to choose!")
    in_options_menu = True
    while in_options_menu:
        option = input("\nPlease select an action: \nShow;\t Add;\t Remove;\t Information;\t  Exit\n")
        
        if normalize(option) == "show" or normalize(option) == "s":
            show_list(guest_list)

        elif normalize(option) == "add" or normalize(option) == "a":
            add_guest(guest_list)

        elif normalize(option) == "remove" or normalize(option) == "r":
            remove_guest(guest_list)

        elif normalize(option) == "information" or normalize(option) == "i":
            information()
        
        elif normalize(option) == "exit" or normalize(option) == "e":
            break
            

if __name__ == "__main__":
    main()