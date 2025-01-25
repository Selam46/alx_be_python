# shopping_list_manager.py

def display_menu():
    """Display the menu options."""
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    """Main function to manage the shopping list."""
    shopping_list = []  # Initialize the shopping list as an empty list

    while True:
        # Display the menu
        display_menu()
        
        # Get user input for menu choice
        try:
            choice = int(input("Enter your choice: "))  # Ensure input is a number
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue
        
        if choice == 1:
            # Add an item to the shopping list
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == 2:
            # Remove an item from the shopping list
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == 3:
            # View the shopping list
            if shopping_list:
                print("Shopping List:")
                for idx, item in enumerate(shopping_list, start=1):
                    print(f"{idx}. {item}")
            else:
                print("The shopping list is empty.")
        
        elif choice == 4:
            # Exit the program
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()
