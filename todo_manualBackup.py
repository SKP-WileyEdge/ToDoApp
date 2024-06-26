# 1. Duplicate Task Allowed
# 2. While printing details aren't formatted --- SOLVED
# 3. Spaces aren't taken care
# 4. Validation not Done Properly
# 5.Task Status Update Field/Feature Missing. (Major)
# 6. Broken CODE --- SOLVED

import json
import os
from datetime import datetime

class TaskManager:
    def __init__(self, filename='tasks_backup.json'):
        self.filename = filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as file:
                return json.load(file)
        return {}

    
########################################## CREATE TASK ##############################################
    def create_task(self,title, priority):
        d = {}
        if(len(self.tasks)>0):
            for i in self.tasks:
                i=int(i)
            i+=1
        else:
            i=1
        task_id = str(i)
        d['id']=task_id
        d['title'] = title
        d['priority'] = priority
        d['timestamp'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if(title and priority):    
            self.tasks[task_id]=d
            return 1
        else:
            return 0


########################################### LIST TASK ##################################################
    def list_tasks(self):
        if len(self.tasks)==0:
            print('\nList is empty')
        else:
            for task in self.tasks.values():
                print(f"{task['id']}: {{\n\tID: {task['id']},\n\tTitle: {task['title']},\n\tPriority: {task['priority']},\n\tTimestamp: {task['timestamp']}\n}},")


    
########################################### DELETE TASK ##################################################
    def delete_task(self, task_id):
        if task_id in self.tasks:
            deleted_task_title = self.tasks[task_id]['title']
            del self.tasks[task_id]
            print(f"\nThe ID {task_id} is successfully deleted. Title: '{deleted_task_title}'")
        else:
            print(f"\nTask with ID {task_id} not found.")



############################################### EDIT TASK ######################################################
    def edit_task(self, task_id, title=None, priority=None):
        if task_id in self.tasks:
            if title:
                self.tasks[task_id]['title'] = title
            if priority:
                self.tasks[task_id]['priority'] = priority



############################################### SEARCH TASK ######################################################
    def search_tasks(self, search_term, search_type):
        if search_type == '1':  # Search by ID
            for task_id, task in self.tasks.items():
                if search_term.lower() == task_id.lower():
                    print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, Timestamp: {task['timestamp']}")
                else:
                    print(f"No Task with id: {search_term} is found")
                    
        elif search_type == '2':  # Search by Task
            for task in self.tasks.values():
                if search_term.lower() in task['title'].lower():
                    print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, Timestamp: {task['timestamp']}")
                else:
                    print(f"No Task with title like: {search_term} is found")
                    
        elif search_type == '3':  # Search by Priority
            for task in self.tasks.values():
                if search_term.lower() in task['priority'].lower():
                    print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, Timestamp: {task['timestamp']}")
                else:
                    print(f"No Task with priority: {search_term} is found")
                    
        else:  # Search by Timestamp
            for task in self.tasks.values():
                if search_term.lower() in task['timestamp'].lower():
                    print(f"ID: {task['id']}, Title: {task['title']}, Priority: {task['priority']}, Timestamp: {task['timestamp']}")
                else:
                    print(f"No Task with timestamp like: {search_term} is found")



###################################################### BACKUP TASK ####################################################
    def backup_tasks(self):
        with open(self.filename, 'w') as file:
            json.dump(self.tasks, file, indent=4)

def main():
    task_manager = TaskManager()
    while True:
        print("\n1. Create Task\n2. Edit Task\n3. List Tasks\n4. Delete Task\n5. Search Tasks\n6. Backup Tasks\n7. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            title = input("Enter task title: ")
            priority = input("Enter task priority (high, medium, low): ")
            ctask=task_manager.create_task(title, priority)
            if ctask==1:
                print('\nNew task is created !')
            elif ctask==0:
                print("\nTask was not created because you have not filled title or priority.\nTry it again!")
            else:
                print("\nSomething went wrong")


        elif choice == '2':
            task_manager.list_tasks()
            print('\n')
            task_id = input("Enter task ID to edit: ")
            if task_id in task_manager.tasks:
                title = input("Enter new title (leave blank to keep current): ")
                priority = input("Enter new priority (leave blank to keep current): ")
                task_manager.edit_task(task_id, title, priority)
            else:
                print('\nInvalid ID')
            print(f"\nThe ID {task_id} is successfully edited.")
            print("\nHere is the Updated todo list: ")
            task_manager.list_tasks()


        elif choice == '3':
            task_manager.list_tasks()


        elif choice == '4':
            task_manager.list_tasks()
            print('\n')
            task_id = input("Enter task ID to delete: ")
            task_manager.delete_task(task_id)


        elif choice == '5':
            if (len(task_manager.tasks)==0):
                print('\nList is empty')
            else:    
                print("\n1. Search by ID\n2. Search by Task\n3. Search by Priority\n4. Search by Timestamp\n")
                search_type = input("Choose type: ")
                valid_search_types = ['1', '2', '3', '4'] 
                if search_type not in valid_search_types:
                    print('\nInvalid search type')
                else:
                    search_term = input("Enter search term: ")
                    flag = 0
                    for i in task_manager.tasks:
                        for v in task_manager.tasks[i].values()
                            if search_term not in v:
                                continue
                            else:
                                task_manager.search_tasks(search_term, search_type)
                                flag = 1
                                break
                    if flag==0:
                        print('\nInvalid search term ')
        
        
        elif choice == '6':
            task_manager.backup_tasks()
            print('\nBackup is created')
        
        
        elif choice == '7':
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
