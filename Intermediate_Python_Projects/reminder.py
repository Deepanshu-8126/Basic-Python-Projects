reminders = {}

while True:
    print("\n--- Reminder Menu ---")
    print("1. Add Reminder")
    print("2. View All Reminders")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        date = input("Enter date (DD/MM): ")
        note = input("Enter reminder note: ")
        reminders[date] = note
        print("Reminder saved!")
    elif choice == "2":
        if reminders:
            print("\nAll Reminders:")
            for d, n in reminders.items():
                print(f"{d} → {n}")
        else:
            print("No reminders yet!")
    elif choice == "3":
        print("Exit")
        break
    else:
        print("Invalid input.")
