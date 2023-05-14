tasks = []

def add_task():
    task = input("Enter your task: ")
    tasks.append(task)
    print("Task added.")

def remove_task():
    task = input("Enter task to remove: ")
    if task in tasks:
        tasks.remove(task)
        print("Task removed.")
    else:
        print("Task not found.")

def show_tasks():
    print("Tasks:")
    for i, task in enumerate(tasks):
        print(f"{i+1}. {task}")

while True:
    print("Select an option:")
    print("a. Add task")
    print("s. Show tasks")
    print("r. Remove task")
    print("e. Exit")
    choice = input("> ")

    if choice == "a":
        add_task()
    elif choice == "r":
        remove_task()
    elif choice == "s":
        show_tasks()
    elif choice == "e":
        print("Exiting...")
        print("THANK YOU FOR ADDING YOUR TASK")
        break
    else:
        print("Invalid choice. Please try again.")
