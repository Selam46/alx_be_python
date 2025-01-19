def display_menu():
    print("\nShopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # Start with an empty shopping list

    while True:
        display_menu()  # Display the menu
        choice = input("Enter your choice: ")  # Get user input

        if choice == '1':  # Add Item
            item = input("Enter the item to add: ")  # Get item from the user
            shopping_list.append(item)  # Add the item to the list
            print(f"{item} has been added to your shopping list.")

        elif choice == '2':  # Remove Item
            item = input("Enter the item to remove: ")  # Get item from the user
            if item in shopping_list:  # Check if the item is in the list
                shopping_list.remove(item)  # Remove the item
                print(f"{item} has been removed from your shopping list.")
            else:
                print(f"{item} is not in the shopping list.")  # Item not found

        elif choice == '3':  # View List
            if shopping_list:  # If the list is not empty
                print("\nYour shopping list:")
                for i, item in enumerate(shopping_list, 1):  # Display each item
                    print(f"{i}. {item}")
            else:
                print("Your shopping list is empty.")  # Handle empty list case

        elif choice == '4':  # Exit
            print("Goodbye!")
            break  # Exit the loop and end the program

        else:
            print("Invalid choice. Please try again.")  # Handle invalid input

if __name__ == "__main__":
    main()
