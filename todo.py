import time

class TODO:
  
  def _init_(self, todos, ptr):
    self.todos = todos
    self.ptr = ptr

  def add(self):
    todo = {}
    todo['id'] = self.ptr
    self.ptr += 1
    todo['desc'] = input("Enter the description: ")
    todo['priority'] = imput("Enter Priority(high/medium/low): ")
    todo['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S")
    todos.append(todo)

  def edit(self):
    pass
    
  def delete(self):
    pass

  def display(self):
    for i in todos:
      print("ID is %d, Task is %s, Priority of this task is %s and task is given at %s"%(i['id'],i['desc'],i['priority'],i['timestamp']))
    pass

  def searchbyDesc(self):
    pass




