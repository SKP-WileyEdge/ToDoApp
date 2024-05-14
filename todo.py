import os
import time

# File path for storing tasks
TASK_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            tasks = [line.strip().split(", ") for line in file.readlines()]
    return tasks

def save_tasks(tasks):
    with open(TASK_FILE, "w") as file:
        for task in tasks:
            file.write(", ".join(task) + "\n")

def add_task(description, priority):
    tasks = load_tasks()
    task_id = str(len(tasks) + 1)
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
    tasks.append([task_id, description, priority, timestamp])
    save_tasks(tasks)
    print("Task added successfully!")

def display_all_tasks():
    tasks = load_tasks()
    if tasks:
        print("ID  | DESCRIPTION          | PRIORITY | TIMESTAMP")
        print("-" * 50)
        for task in tasks:
            print(f"{task[0]:<3} | {task[1]:<20} | {task[2]:<8} | {task[3]}")
    else:
        print("No tasks found.")

def delete_task(task_id):
    tasks = load_tasks()
    updated_tasks = [task for task in tasks if task[0] != task_id]
    save_tasks(updated_tasks)
    print("Task deleted successfully!")

def main():
    while True:
        print("\nTODO App Menu:")
        print("1. Add Task")
        print("2. Edit Task")
        print("3. Delete Task")
        print("4. Display All Tasks")
        print("5. Search Task")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            description = input("Enter task description: ")
            priority = input("Enter priority (High/Medium/Low): ")
            add_task(description, priority)
        elif choice == "2":
            print("Feature not implemented yet.")
        elif choice == "3":
            task_id = input("Enter task ID to delete: ")
            delete_task(task_id)
        elif choice == "4":
            display_all_tasks()
        elif choice == "5":
            print("Feature not implemented yet.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
