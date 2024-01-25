ToDoList = []

def addtask():
    task = input("Enter task: ")
    ToDoList.append({"task": task, "completed": False})
    print("Task added successfully")

def viewtask():
    for index, task in enumerate(ToDoList, start=1):
        status = "Done" if task["completed"] else "Pending"
        print(f"{index}. {task['task']} - {status}")
    print()

def markascompleted():
    viewtask()
    try:
        index = int(input("Enter the number of the task you want to mark as completed: ")) - 1
        ToDoList[index]["completed"] = True
        print("Task marked as completed successfully")
    except (ValueError, IndexError):
        print("Invalid input")

def removetask():
    viewtask()
    try:
        index = int(input("Enter the number of the task you want to remove: ")) - 1
        removed_task = ToDoList.pop(index)
        print(f"Task '{removed_task['task']}' removed successfully")
    except (ValueError, IndexError):
        print("Invalid input")

while True:
    choice = input("Enter your choice:\n1 to add task\n2 to view tasks\n3 to mark task as completed\n4 to remove task\n5 to exit the app\n")

    if choice == "1":
        addtask()
    elif choice == "2":
        viewtask()
    elif choice == "3":
        markascompleted()
    elif choice == "4":
        removetask()
    elif choice == "5":
        print("Exiting the app. Goodbye!")
        break
    else:
        print("Invalid input")
