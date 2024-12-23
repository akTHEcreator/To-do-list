class function:

    tasks={}
    task_indexed=[]                                                                                          # This is to ensure tasks can be referred with an index

    def __init__(self):
        self.updatelist()
    
    def addtask(self):
        newtask=input("Please enter your new task: ")
        function.tasks[newtask]="Incomplete"
        print("New task '"+newtask+ "' added")
        self.updatelist()
    
    def deltask(self):
        count=1
        for task in function.task_indexed:
            print(str(count)+". "+task)
            count+=1
        choice=int(input("Choose the task (1-"+str(len(function.tasks))+") you want to delete? "))
        del function.tasks[function.task_indexed[choice-1]]
        print("Task has been deleted.")
        self.updatelist()
    
    def viewtask(self):
        count=1
        for task in function.task_indexed:
            print(str(count)+". "+task)
            count+=1


    def updatelist(self):
        function.task_indexed=list(function.tasks.keys())

     




def main():

    func=function()

    while True:
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Mark Task Complete")
        print("5. Exit")
        option=input("Choose any option (1-5): ")
        if option=="1":
            func.addtask()
        elif option=="2":
            func.deltask()
        elif option=="3":
            func.viewtask()
        elif option=="4":
            func.marktask()
        elif option=="5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")



main()