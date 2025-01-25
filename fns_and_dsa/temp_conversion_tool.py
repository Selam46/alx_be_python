# temp_conversion_tool.py

# Global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5
FAHRENHEIT_FREEZE_POINT = 32  # Freezing point of water in Fahrenheit
CELSIUS_FREEZE_POINT = 0  # Freezing point of water in Celsius

def convert_to_celsius(fahrenheit):
    """Convert Fahrenheit to Celsius using the global factor."""
    # Conversion formula: (Fahrenheit - 32) * (5/9)
    return (fahrenheit - FAHRENHEIT_FREEZE_POINT) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    """Convert Celsius to Fahrenheit using the global factor."""
    # Conversion formula: Celsius * (9/5) + 32
    return celsius * CELSIUS_TO_FAHRENHEIT_FACTOR + FAHRENHEIT_FREEZE_POINT

def main():
    try:
        # User input for temperature
        temp = input("Enter the temperature to convert: ")
        temp = float(temp)  # Convert input to float to ensure it's a valid number
        unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

        if unit == 'C':
            # Convert Celsius to Fahrenheit
            fahrenheit = convert_to_fahrenheit(temp)
            print(f"{temp}°C is {fahrenheit}°F")
        
        elif unit == 'F':
            # Convert Fahrenheit to Celsius
            celsius = convert_to_celsius(temp)
            print(f"{temp}°F is {celsius}°C")
        
        else:
            print("Invalid unit. Please enter 'C' for Celsius or 'F' for Fahrenheit.")
    
    except ValueError:
        # Handling invalid input (non-numeric values)
        print("Invalid temperature. Please enter a numeric value.")

if __name__ == "__main__":
    main()
