tasks = []
while True:
    print("\n--To Do List---")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        task = input("Enter task name: ")
        tasks.append(task)
        print("Task added!")
    elif choice == "2":
        print("\nYour Tasks:")
        if len(tasks) == 0:
            print("No tasks found!")
        else:
            for i in range(len(tasks)):
                print(i+1, ".", tasks[i])
    elif choice == "3":
        if len(tasks) == 0:
            print("No tasks to delete!")
        else:
            num = int(input("Enter task number: "))
            if 0 < num <= len(tasks):
                removed = tasks.pop(num-1)
                print(f"Deleted: {removed}")
            else:
                print("Invalid task number!")
    elif choice == "4":
        print("Thank you ")
        break
    else:
        print("Invalid input, try again!")
