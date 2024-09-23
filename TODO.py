import datetime

task_list = []

while True:
    print("\nTo-Do List Menu:")
    print("1. Add Task")
    print("2. Remove Task")
    print("3. View Tasks")
    print("4. Clear List")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        task = input("Enter Task to add: ")
        current_time = datetime.datetime.now().strftime("(%I:%M:%S %p)")
        task_with_time = f"{task} {current_time}"
        task_list.append(task_with_time)
        print("Task Added into list..")

    elif choice == '2':
        if len(task_list) == 0:
            print("List Is Empty Already!")
        else:
            del_task = input("Enter the task you want to delete: ")
            if del_task in task_list:
                task_list.remove(del_task)
                print("Task deleted from list")
            else:
                print("Task not found in the list")

    elif choice == '3':
        if len(task_list) == 0:
            print("List Is Empty")
        else:
            print("Tasks:")
            for task_with_time in task_list:
                task, time_added = task_with_time.rsplit(' ', 1)
                print(f"{task} {time_added}")

    elif choice == '4':
        task_list.clear()
        print("Your List is Empty")

    elif choice == '5':
        print("Exited...")
        break

    else:
        print("Invalid Choice... Please Enter a Number from 1 to 5!!")
