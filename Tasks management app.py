# TASKS MANAGEMENT SYSTEM/APP...

def tasks():
    list = []
    print("......wlecome to Task Management App...")
    user = int(input("enter how many tasks you want= "))
    for i  in range(1,user+1):
        task = input(f"enter the tasks{i}= ")
        list.append(task)
    print(list)

    while True:
        operation = int(input("Enter\n1-add\n2-update\n3-delete\n4-view\n5-exit"))
        if operation == 1:
            add = input("enter the task you want to add= ")
            list.append(add)
            print(f"{add} task has been successfully added")

        elif operation == 2:
            update_val = input("enter the task you want to update= ")
            if update_val in list:
                up = input("enter the new task= ")
                ind = list.index(update_val)
                list[ind] = up
                print(f"updated task {up}")

        elif operation == 3:
            delete_val = input("enter the task you want to delete= ")
            if delete_val in list:
                ind = list.index(delete_val)
                del list[ind]
                print(f"task {delete_val} has been deleted successfully")

        elif operation == 4:
            print(f"total tasks are {list}")

        elif operation == 5:
            print("closing the Task management App......")
            break

        else:
            print("invalid input")

tasks()