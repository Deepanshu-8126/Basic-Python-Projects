import random
print("🎲 Dice Roller Simulator 🎲")
while True:
    roll = input("Roll the dice? (y/n): ").lower()
    if roll == "y":
        print("You got:", random.randint(1, 6))
    elif roll == "n":
        print("Thanks for playing!")
        break
    else:
        print(" Invalid input, please enter y or n.")
