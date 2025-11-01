
books = ["Python", "C Programming", "Data Science", "AI Basics"]

while True:
    print("\n1. View Books\n2. Borrow Book\n3. Return Book\n4. Exit")
    ch = input("Enter your choice: ")

    if ch == "1":
        print(" Available Books:", books)
    elif ch == "2":
        b = input("Enter book name to borrow: ")
        if b in books:
            books.remove(b)
            print("You borrowed:", b)
        else:
            print("Book not available.")
    elif ch == "3":
        b = input("Enter book name to return: ")
        books.append(b)
        print(" Book returned successfully.")
    elif ch == "4":
        print(" Thank you! Visit again.")
        break
    else:
        print(" Invalid option.")
