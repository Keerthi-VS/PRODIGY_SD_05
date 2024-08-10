def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def celsius_to_kelvin(celsius):
    return celsius + 273.15

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15

def kelvin_to_celsius(kelvin):
    return kelvin - 273.15

def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32

def convert_temperature(value, unit):
    if unit == 'C':
        print(f"{value}°C is {celsius_to_fahrenheit(value):.2f}°F and {celsius_to_kelvin(value):.2f}K")
    elif unit == 'F':
        print(f"{value}°F is {fahrenheit_to_celsius(value):.2f}°C and {fahrenheit_to_kelvin(value):.2f}K")
    elif unit == 'K':
        print(f"{value}K is {kelvin_to_celsius(value):.2f}°C and {kelvin_to_fahrenheit(value):.2f}°F")
    else:
        print("Invalid unit. Please enter 'C' for Celsius, 'F' for Fahrenheit, or 'K' for Kelvin.")

def main():
    value = float(input("Enter the temperature value: "))
    unit = input("Enter the unit of the temperature (C for Celsius, F for Fahrenheit, K for Kelvin): ").upper()
    convert_temperature(value, unit)

if __name__ == "__main__":
    main()
