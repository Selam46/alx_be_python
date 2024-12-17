
# Prompt the user for a number
try:
    number = int(input("Enter a number to see its multiplication table: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    exit()

# Generate and print the multiplication table from 1 to 10
print(f"Multiplication table for {number}:")
for i in range(1, 11):
    result = number * i
    print(f"{number} * {i} = {result}")
