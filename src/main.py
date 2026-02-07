# src/main.py

tasks = []
task_id_counter = 1

def add_task():
    """Add a new task"""
    global task_id_counter
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    task = {
        "id": task_id_counter,
        "title": title,
        "description": description,
        "completed": False
    }
    tasks.append(task)
    task_id_counter += 1
    print("✅ Task added successfully!\n")

def view_tasks():
    """View all tasks"""
    if not tasks:
        print("📭 No tasks found.\n")
        return
    for task in tasks:
        status = "✔" if task["completed"] else "✘"
        print(f'ID: {task["id"]} | {task["title"]} | {task["description"]} | Completed: {status}')
    print()

def update_task():
    """Update an existing task"""
    try:
        task_id = int(input("Enter task ID to update: "))
    except ValueError:
        print("⚠️ Invalid ID.\n")
        return
    for task in tasks:
        if task["id"] == task_id:
            task["title"] = input("Enter new title: ")
            task["description"] = input("Enter new description: ")
            print("✅ Task updated!\n")
            return
    print("⚠️ Task not found.\n")

def delete_task():
    """Delete a task by ID"""
    try:
        task_id = int(input("Enter task ID to delete: "))
    except ValueError:
        print("⚠️ Invalid ID.\n")
        return
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            print("🗑️ Task deleted!\n")
            return
    print("⚠️ Task not found.\n")

def toggle_complete():
    """Mark a task complete/incomplete"""
    try:
        task_id = int(input("Enter task ID to toggle complete: "))
    except ValueError:
        print("⚠️ Invalid ID.\n")
        return
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = not task["completed"]
            status = "✔ Completed" if task["completed"] else "✘ Incomplete"
            print(f"✅ Task status toggled: {status}\n")
            return
    print("⚠️ Task not found.\n")

def menu():
    """Main menu"""
    print("📝 Welcome to In-Memory Todo App\n")
    while True:
        print("==== Todo App ====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Delete Task")
        print("5. Toggle Complete")
        print("6. Exit")
        choice = input("Choose an option: ")
        print()
        if choice == "1":
            add_task()
        elif choice == "2":
            view_tasks()
        elif choice == "3":
            update_task()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            toggle_complete()
        elif choice == "6":
            print("👋 Goodbye!")
            break
        else:
            print("⚠️ Invalid choice, try again.\n")

if __name__ == "__main__":
    menu()
