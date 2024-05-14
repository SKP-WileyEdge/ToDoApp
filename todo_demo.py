import json
import os

# Define task data structure
class Task:
    def __init__(self, id, title, priority):
        self.id = id
        self.title = title
        self.priority = priority

    def to_dict(self):
        return {"id": self.id, "title": self.title, "priority": self.priority}

class TaskManager:
    def __init__(self, filename='tasks.json', tasks):
        self.filename = filename
        self.tasks = []

    def add_task(self, desc, priority):
        task = {}
        task_id = len(self.tasks)
        task['ID'] = task_id
        task['Description'] = title
        task['Priority'] = input("Enter Priority[high/medium/low]: ")
        task['Datetime'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tasks.append(task)

    def edit_task(self, task_id, desc, priority):
        if task_id <= len(self.tasks):
            self.tasks[task_id-1]['Description'] = desc
            self.tasks[task_id-1]['Priority'] = priority
        else:
            print("Sorry no task with such id !")

    def list_tasks(self):
        for t in self.tasks.keys():
                print(f"ID is {t['ID']}, Task is {t['Description']}, and the Priority of this task is {t['Priority']}" )

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            self.save_tasks()

def search_tasks(self, search_term):
    for task in self.tasks.values():
        if search_term.lower() in task['title'].lower():
            print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}")

def backup_tasks(self, backup_filename):
    with open(backup_filename, 'w') as file:
        json.dump(self.tasks, file, indent=4)

def restore_tasks(self, backup_filename):
    if os.path.exists(backup_filename):
        with open(backup_filename, 'r') as file:
            self.tasks = json.load(file)
        self.save_tasks()

def main():
    task_manager = TaskManager()
    while True:
        print("\n1. Create Task\n2. Edit Task\n3. List Tasks\n4. Delete Task\n5. Search Tasks\n6. Backup Tasks\n7. Restore Tasks\n8. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high, medium, low): ")
            task_manager.create_task(title, priority)
        elif choice == '2':
            task_id = input("Enter task ID to edit: ")
            title = input("Enter new title (leave blank to keep current): ")
            priority = input("Enter new priority (leave blank to keep current): ")
            task_manager.edit_task(task_id, title, priority)
        elif choice == '3':
            task_manager.list_tasks()
        elif choice == '4':
            task_id = input("Enter task ID to delete: ")
            task_manager.delete_task(task_id)
        elif choice == '5':
            search_term = input("Enter search term: ")
            task_manager.search_tasks(search_term)
        elif choice == '6':
            backup_filename = input("Enter backup filename: ")
            task_manager.backup_tasks(backup_filename)
        elif choice == '7':
            backup_filename = input("Enter backup filename to restore: ")
            task_manager.restore_tasks(backup_filename)
        elif choice == '8':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
