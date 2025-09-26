tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def show_tasks():
    if not tasks:
        print("No tasks yet")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def remove_task(task_number):
    if 0 <= task_number < len(tasks):
        tasks.pop(task_number)
        print("Task removed!")
    else:
        print("Invalid task number!")

def main():
    while True:
        print("1. Add Task")
        print("2. Show Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            task = input("Enter task: ")
            add_task(task)
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            try:
                num = int(input("Enter task number to remove: ")) - 1
                remove_task(num)
            except ValueError:
                print("Please enter a valid number!")
        elif choice == "4":
            break
        else:
            print("Wrong choice!")

main()
