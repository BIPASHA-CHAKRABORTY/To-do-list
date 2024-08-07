to_do_list = []  # Initialize an empty to-do list
#hi
while True:
    print("\n MENU")
    print("1. Add a task")
    print("2. Mark a task as done")
    print("3. Remove a task")
    print("4. Exit")

    # Get user input for choice
    choice = input("\n Enter the number for your preference: ")

    if choice == '1':
        task = input("Enter your task: ")
        to_do_list.append(task)
        print("\n Task added successfully!")

    elif choice == '2':
        if len(to_do_list) == 0:
            print("\n No tasks in the list.")
        else:
            print("\n Current tasks:")
            for index, task in enumerate(to_do_list):
                print(f"{index + 1}. {task}")
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            if 0 <= task_index < len(to_do_list):
                print(f"\n Marking '{to_do_list[task_index]}' as done.")
                to_do_list.pop(task_index)
            else:
                print("\n Invalid task number.")

    elif choice == '3':
        if len(to_do_list) == 0:
            print("\n No tasks in the list.")
        else:
            print("\n Current tasks:")
            for index, task in enumerate(to_do_list):
                print(f"{index + 1}. {task}")
            task_index = int(input("Enter the task number to remove: ")) - 1
            if 0 <= task_index < len(to_do_list):
                removed_task = to_do_list.pop(task_index)
                print(f"\n '{removed_task}' removed from the list.")
            else:
                print("\n Invalid task number.")

    elif choice == '4':
        print("\n Thank you for using the to-do list. See you next time!")
        break

    else:
        print("\n Invalid choice, please try again.")
