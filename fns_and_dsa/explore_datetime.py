from datetime import datetime, timedelta

def display_current_datetime():
    """
    Function to display the current date and time in a readable format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Function to calculate and display a future date based on user input.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

# Main execution
if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
=======
# explore_datetime.py

import datetime  # Import the datetime module
=======
from datetime import datetime, timedelta
>>>>>>> 6a92cb34f3c453a63e1504e2be2c6b1ea35c5812

def display_current_datetime():
    """
    Function to display the current date and time in a readable format.
    """
    current_date = datetime.now()
    formatted_date = current_date.strftime("%Y-%m-%d %H:%M:%S")
    print(f"Current date and time: {formatted_date}")

def calculate_future_date():
    """
    Function to calculate and display a future date based on user input.
    """
    try:
        days_to_add = int(input("Enter the number of days to add to the current date: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days_to_add)
        formatted_future_date = future_date.strftime("%Y-%m-%d")
        print(f"Future date: {formatted_future_date}")
    except ValueError:
        print("Invalid input. Please enter an integer value.")

# Main execution
if __name__ == "__main__":
<<<<<<< HEAD
    # Call the functions and ensure formatted dates are returned
    display_current_datetime()  # Will display and return current date
    calculate_future_date()  # Will prompt user for input and return future date
>>>>>>> 4f0b7d13f668955e9c0fa165016e27b53584811c
=======
    display_current_datetime()
    calculate_future_date()
>>>>>>> 6a92cb34f3c453a63e1504e2be2c6b1ea35c5812
