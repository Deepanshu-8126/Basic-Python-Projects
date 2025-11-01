print("Hi! I’m BasicBot Type 'bye' to exit.")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("PyBot: Hello! How are you?")
    elif "name" in user:
        print("PyBot: I'm Basic  Bot, your Python friend!")
    elif "python" in user:
        print("PyBot: Python is my favorite language too! 🐍")
    elif "bye" in user:
        print("PyBot: bye bye have a nice day ")
        break
    else:
        print("PyBot: Hmm... I didn't understand that.")
