
# Prompt the user to input the size of the pattern
try:
    size = int(input("Enter the size of the pattern: "))
    if size <= 0:
        print("Please enter a positive integer.")
        exit()
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")
    exit()

# Initialize row counter for while loop
row = 0

# Use a while loop to handle each row
while row < size:
    # Use a for loop to print '*' in each column
    for col in range(size):
        print("*", end="")  # Print '*' without a newline
    print()  # Print a newline after each row
    row += 1
