tasks = []

def add_task():
    description = input("Task description: ")
    priority = input("Priority (High/Medium/Low): ")
    task = {
        "description": description,
        "priority": priority,
        "status": "Pending"
    }
    tasks.append(task)
    print("Task added.")

def show_tasks(task_list=None):
    if task_list is None:
        task_list = tasks
    if not task_list:
        print("No tasks to show.")
        return
    for i, t in enumerate(task_list):
        print(f"{i}. {t['description']} | Priority: {t['priority']} | Status: {t['status']}")

def mark_completed():
    show_tasks()
    try:
        index = int(input("Enter the number of the task to mark as completed: "))
        if 0 <= index < len(tasks):
            tasks[index]["status"] = "Completed"
            print("Task marked as completed.")
        else:
            print("Index out of range.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def filter_by_priority():
    priority = input("Enter priority to filter by (High/Medium/Low): ")
    filtered = [t for t in tasks if t["priority"].lower() == priority.lower()]
    print(f"Tasks with priority '{priority}':")
    show_tasks(filtered)

def filter_by_status():
    status = input("Enter status to filter by (Pending/Completed): ")
    filtered = [t for t in tasks if t["status"].lower() == status.lower()]
    print(f"Tasks with status '{status}':")
    show_tasks(filtered)

def menu():
    while True:
        print("\n--- TASK MENU ---")
        print("1. Add task")
        print("2. Show all tasks")
        print("3. Mark task as completed")
        print("4. Filter tasks by priority")
        print("5. Filter tasks by status")
        print("6. Exit")

        option = input("Select an option: ")

        if option == "1":
            add_task()
        elif option == "2":
            show_tasks()
        elif option == "3":
            mark_completed()
        elif option == "4":
            filter_by_priority()
        elif option == "5":
            filter_by_status()
        elif option == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")


    menu()