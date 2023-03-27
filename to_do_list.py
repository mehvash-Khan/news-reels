import pdb;



class Task:
    def __init__(self,name,isCompleted):
        self.isCompleted =False
        self.name = name

    def markComplete(self):
        self.isCompleted = True;
       

def viewTask(taskList,state):
    if(taskList != []):

        tasks = [task.name for task in taskList if task.isCompleted == state]
        for completed in tasks:
            print(completed)
    else:
        print("\nNo tasks to be viewed")

def addTask(taskList):
    name = input("\nEnter task for to do list: ")
    task = Task(name,False)
    taskList.append(task)

def removeTask(taskList):
    viewTask(taskList,False);
    name = input("\nEnter task to be marked as complete from the list: ")
    flag =0;
    for task in taskList:
        if task.name == name:
            task.markComplete()
            flag = 1;
            break;
    if flag==0:
        print("\n No such task exist. Please enter correct task name")


def _main_():
    
    options = """ 
    ---------Choose from the list---------
        1. Add task
        2. Mark task as complete
        3. View to do tasks
        4. View completed tasks
        5. Exit application
    """

    taskList = []
    
    
    
    while(True):
        print(options)
        chosen = int(input("Enter yout choice number: "))
        
        if(chosen == 1):
            addTask(taskList);

        elif(chosen == 2):
            #pdb.set_trace();
            removeTask(taskList)
            
            
        elif(chosen == 3):
            print("-----To Do List------")
            viewTask(taskList,False);
       
        elif(chosen == 4):
            print("-----Completed task list------")
            viewTask(taskList,True);

        elif(chosen == 5):
            break;


_main_();