def display_menu():
    """
    Function to display the menu for the shopping list manager.
    This function prints the options that the user can choose from.
    """
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Initialize an empty list for the shopping list

    while True:
        display_menu()  # Call the display_menu function to show the menu
        try:
            choice = int(input("Enter your choice: "))  # Ensure choice is entered as a number
        except ValueError:
            print("Invalid input! Please enter a number.")
            continue

        if choice == 1:  # Add Item
            item = input("Enter the item to add: ")  # Get item from the user
            shopping_list.append(item)  # Add the item to the shopping list
            print(f"{item} has been added to your shopping list.")

        elif choice == 2:  # Remove Item
            item = input("Enter the item to remove: ")  # Get item from the user
            if item in shopping_list:
                shopping_list.remove(item)  # Remove the item from the list
                print(f"{item} has been removed from your shopping list.")
            else:
                print(f"{item} is not in the shopping list.")  # Handle item not found

        elif choice == 3:  # View List
            if shopping_list:  # Check if the list is not empty
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list, 1):  # List all items with index
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")  # Handle empty list case

        elif choice == 4:  # Exit
            print("Goodbye!")  # Exit the program
            break  # Exit the loop and end the program

        else:
            print("Invalid choice! Please enter a valid number between 1 and 4.")  # Handle invalid choice

if __name__ == "__main__":
    main()

