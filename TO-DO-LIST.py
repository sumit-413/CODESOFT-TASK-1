import json
import os
from datetime import datetime

TASKS_FILE = "tasks.json"
tasks = []

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def load_tasks():
    global tasks
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as f:
            tasks = json.load(f)
            
    else:
        tasks = []

def save_tasks():
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=10)

def display_menu():
    print("\n ====== TO-DO LIST MENU ======")
    print("1. Show Tasks")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Task as Done")
    print("6. Clear All Tasks")
    print("7. Save & Exit")

def show_tasks():
    if not tasks:
        print("\n No tasks available... please add some tasks!")
    else:
        print("\n Your Tasks:\n")
        print(f"{'No.':<5}{'Task':<30}{'Due Date':<15}{'Status':<10}")
        print("-" * 60)
        for i, task in enumerate(tasks, start=1):
            print(f"{i:<5}{task['title']:<30}{task['due_date']:<15}{task['status']:<10}")
        print("-" * 60)

def add_task():
    title = input("Enter task: ").strip()
    due_date = input("Enter due date (YYYY-MM-DD) [optional]: ").strip()
    due_date = due_date if due_date else "None"
    task = {
        "title": title,
        "due_date": due_date,
        "status": "Pending"
    }
    tasks.append(task)
    print("Task added!")

def update_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to update: "))
        if 1 <= task_num <= len(tasks):
            new_title = input("New task description: ").strip()
            new_due = input("New due date (YYYY-MM-DD) [leave blank to keep]: ").strip()
            tasks[task_num - 1]['title'] = new_title or tasks[task_num - 1]['title']
            if new_due:
                tasks[task_num - 1]['due_date'] = new_due
            print(" Task updated.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    show_tasks()
    try:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            deleted = tasks.pop(task_num - 1)
            print(f"Deleted task: {deleted['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def mark_done():
    show_tasks()
    try:
        task_num = int(input("Enter task number to mark as done: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['status'] = "Done"
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def clear_all_tasks():
    confirm = input("Are you sure you want to delete ALL tasks? (yes/no): ").strip().lower()
    if confirm == "yes":
        tasks.clear()
        print("All tasks cleared.")
    else:
        print(" Operation cancelled.")

def main():
    load_tasks()
    while True:
        clear_screen()
        display_menu()
        choice = input("\nChoose an option (1-7): ").strip()
        if choice == "1":
            clear_screen()
            show_tasks()
            input("\nPress Enter to return to menu...")
        elif choice == "2":
            add_task()
            save_tasks()
        elif choice == "3":
            update_task()
            save_tasks()
        elif choice == "4":
            delete_task()
            save_tasks()
        elif choice == "5":
            mark_done()
            save_tasks()
        elif choice == "6":
            clear_all_tasks()
            save_tasks()
        elif choice == "7":
            save_tasks()
            print(" Tasks saved. Goodbye!")
            break
        else:
            print("Invalid option.")
            input("Press Enter to continue...")

if __name__ == "__main__":
    main()