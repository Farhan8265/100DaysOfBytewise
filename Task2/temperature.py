# Exercise: Temperature Converter
print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")
print("4. Kelvin to Celsius")
print("5. Fahrenheit to Kelvin")
print("6. Kelvin to Fahrenheit")

choice = int (input ("Enter Your Choice (1-6): ") )

if choice == 1:
    celsius = float (input("Enter Temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
elif choice == 2:
    fahrenheit = float (input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print("Temperature in Celsius:", celsius)
elif choice == 3:
    celsius = float (input("Enter temperature in Celsius: "))
    kelvin = celsius + 273.15
    print("Temperature in Kelvin:", kelvin)
elif choice == 4:
    kelvin = float (input("Enter temperature in Kelvin: "))
    celsius = kelvin - 273.15
    print("Temperature in Celsius:", celsius)
elif choice == 5:
    fahrenheit = float (input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    kelvin = celsius + 273.15
    print("Temperature in Kelvin:", kelvin)
elif choice == 6:
    kelvin = float (input("Enter temperature in Kelvin: "))
    celsius = kelvin - 273.15
    fahrenheit = (celsius * 9/5) + 32
    print("Temperature in Fahrenheit:", fahrenheit)
else:
    print("Invalid choice")