def main():

    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Mark Task Complete")
    print("5. Exit")

    while True:
        option=input("Choose any option (1-5): ")
        if option=="1":
            addtask()
        elif option=="2":
            remtask()
        elif option=="3":
            viewtask()
        elif option=="4":
            marktask()
        elif option=="5":
            print("Exiting the app. Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

