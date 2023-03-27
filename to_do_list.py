import pdb;

class Task:
    def __init__(self,name,isCompleted):
        self.isCompleted =isCompleted
        self.name = name

    def markComplete(self):
        self.isCompleted = True;
       

class TaskList:
    def __init__(self):
        self.taskList = []
        
    def addTask(self,name):
        task = Task(name,False)
        self.taskList.append(task)

    def removeTask(self,name):
        completed =0;
        for task in self.taskList:
            if task.name == name:
                task.markComplete()
                completed = 1;
                break;
        if completed==0:
            print("\n No such task exist. Please enter correct task name")

    def viewTask(self,state):
        tasks = [task.name for task in self.taskList if task.isCompleted == state]
        if(len(tasks) > 0):
            for completed in tasks:
                print(completed)
        else:
            print("\nNo tasks to be viewed")






def _main_():
    
    options = """ 
    ---------Choose from the list---------
        1. Add task
        2. Mark task as complete
        3. View to do tasks
        4. View completed tasks
        5. Exit application
    """

    taskList = TaskList()
    
    
    
    while(True):
        print(options)
        chosen = int(input("Enter yout choice number: "))
        
        if(chosen == 1):
            task = input("\nEnter task for to do list: ")
            taskList.addTask(task)

        elif(chosen == 2):
            #pdb.set_trace();
            taskList.viewTask(False);
            task = input("\nEnter task to be marked as complete from the list: ")
            taskList.removeTask(task)
            
            
        elif(chosen == 3):
            print("-----To Do List------")
            taskList.viewTask(False);
       
        elif(chosen == 4):
            print("-----Completed task list------")
            taskList.viewTask(True);

        elif(chosen == 5):
            break;


_main_();