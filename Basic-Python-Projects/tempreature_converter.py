choice = input("C to F or F to C? ").lower()

if choice == "c to f":
    c = float(input("Enter Celsius: "))
    print("In Fahrenheit:", (c * 9/5) + 32)
elif choice == "f to c":
    f = float(input("Enter Fahrenheit: "))
    print("In Celsius:", (f - 32) * 5/9)
else:
    print("Invalid choice!")
