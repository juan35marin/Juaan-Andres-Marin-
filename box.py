box_list = []

def add_box():
    box_type = input("Enter the box type: ").strip()
    if not box_type:
        print("You must enter the box type.")
        return
    try:
        quantity = int(input("Enter the quantity of boxes: "))
        if quantity < 0:
            print("Invalid value, quantities cannot be negative.")
            return

        box = {
            'type': box_type,
            'quantity': quantity
        }
        box_list.append(box)
        print(f"'{box_type}' has been added to the inventory list.")
    except ValueError:
        print("Invalid input, please enter numeric values.")

def search(box_type):
    for box in box_list:
        if box['type'].lower() == box_type.lower():
            return box
    return None

def update_quantity():
    box_type = input("Enter the box type to update the quantity: ").strip()
    box = search(box_type)
    if box:
        try:
            new_quantity = int(input("Enter the new quantity: "))
            if new_quantity < 0:
                print("Invalid option, quantity cannot be negative.")
                return
            box['quantity'] = new_quantity
            print(f"The new quantity for '{box_type}' is {new_quantity}.")
        except ValueError:
            print("Invalid option, quantity must be numeric.")
    else:
        print("The product does not exist in the box list.")

def main():
    print("--- Inventory Management ---")
    print("1. Add box")
    print("2. Update quantity")
    print("3. Exit")

    while True:
        try:
            option = int(input("Choose an option: "))
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 3.")
            continue

        if option == 1:
            add_box()
        elif option == 2:
            update_quantity()
        elif option == 3:
            print("Program terminated.")
            break
        else:
            print("Invalid option. Please try again.")

main()