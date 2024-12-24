def project():
    tasks=[]
    print("Hello Welcome!!!!")
    task=int(input("Enter the total number of tasks you want to complete: "))
    for i in range(1,task+1):
        toDo=input(f"enter the task {i}: ")
        tasks.append(toDo)
    print(f"Tasks you want to complete are:{tasks}")
    mod=int(input("1-want to do modifications\n2-to exit\nEnter: "))
    if mod==1:
        while True:
            enter=int(input("1-Addition\n2-Deletion\n3-updation\n4-view all tasks\n5-Exit\nEnter: "))
            if enter==1:
                add_val=input("enter the task you want to add: ")
                if add_val in tasks:
                    print("the task is already present")
                    continue
                else:
                    tasks.append(add_val)
                    print(f"---THE TASK '{add_val}'' HAS BEEN ADDED SUCCESSFULLY---")
            elif enter==2:
                del_val=input("enter the task you want to delete: ")
                if del_val in tasks:
                    k=input("are you sure you want to delete (yes/no): ").strip().lower()
                    if k=="yes":
                        ind=tasks.index(del_val)
                        del tasks[ind]
                        print(f"---THE TASK '{del_val}'' HAS BEEN DELETED SUCCESSFULLY---")
                    else:
                        print("---ok!!! thank you for confirmation")
                        continue
                else:
                    print(f"the task {del_val} is not found")
                    continue
            elif enter==3:
                upd_val1=input("enter the task you want to update: ")
                if upd_val1 in tasks:
                    upd_val2=input("enter the task you want to update with: ")
                    ind=tasks.index(upd_val1)
                    tasks[ind]=upd_val2
                    print(f"---THE TASK '{upd_val1}' HAS BEEN UPDATED SUCCESSFULLY---")
                else:
                    print(f"The task {upd_val1} is not found")
                    continue
            elif enter==4:
                print(f"the tasks are : {tasks}")
            elif enter==5:
                print("---EXITING THE APP---")
                break
            else:
                print("---invalid input---")
                continue
    elif mod==2:
        while True:
            print("---EXITING THE APP---")
            break
    else:
        print("something went wrong\n try again")
    print("Thank you for using the To-Do App. Have a productive day!!!")
    
project()
