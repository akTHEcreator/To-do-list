class functions:

    tasks={}
    task_indexed=[]                                                                                          # This is to ensure tasks can be referred with an index

    def __init__(self,option):
        self.option=option
        self.updatelist()
    
    def addtask(self):
        newtask=input("Please enter your new task: ")
        tasks[newtask]="Incomplete"
        print("New task '"+newtask+ "' added")
    
    def deltask(self):
        count=1
        for num in len(tasks):
            print(count+". "+tasks[num])
            count=+1
        choice=int(input("Choose the task (1-"+str(len(tasks))+") you want to delete?"))
        del tasks[task_indexed[choice-1]]
        print("Task has been deleted.")
    

    def updatelist(self):
        task_indexed=list(tasks.keys())

        
        


        















def main():

    print("1. Add Task")
    print("2. Delete Task")
    print("3. View Tasks")
    print("4. Mark Task Complete")
    print("5. Exit")

    while True:
        option=input("Choose any option (1-5): ")
        if option=="1":
            addtask()
        elif option=="2":
            deltask()
        elif option=="3":
            viewtask()
        elif option=="4":
            marktask()
        elif option=="5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")



