tasks = []  # initialize empty list titled tasks

def addtask(task):
    tasks.append(task)
    print(f"✅ Task added: {task}\n")
# addtask function appends the task to the tasks list and confirms addition

def showTasks():
    if len(tasks) == 0:
        print("📋 No tasks yet.\n")
    else:
        print("\n📌 Your Tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"   {i}. {task}")
        print()  # extra newline for spacing
# shows the status of the list whether it has an existing task or not

def searchTasks(keyword):
    found = [task for task in tasks if keyword.lower() in task.lower()]
    if not found:
        print(f"🔍 No tasks found containing '{keyword}'.\n")
    else:
        print(f"\n🔍 Tasks containing '{keyword}':")
        for i, task in enumerate(found, 1):
            print(f"   {i}. {task}")
        print()
######
def removetask(tasknumber):
    if 0 < tasknumber <= len(tasks):
        removed = tasks.pop(tasknumber - 1)
        print(f"🗑️ Task removed: {removed}\n")
    else:
        print("⚠️ Invalid task number!\n")

def main():
    while True:
        print("=" * 30)
        print("📝 TO-DO APP")
        print("=" * 30)
        print("1. ➕ Add Task")
        print("2. 📋 Show Tasks")
        print("3. 🗑️ Remove Task")
        print("4. 🚪 Exit")
        print("5. 🔍 Search Task")   # 👈 NEW OPTION
        print("=" * 30)

        ch = input("👉 Enter choice: ")

        if ch == "1":
            t = input("✏️ Enter task: ")
            addtask(t)
        elif ch == "2":
            showTasks()
        elif ch == "3":
            showTasks()
            if tasks:  # only ask if tasks exist
                try:
                    n = int(input("Enter task no. to remove: "))
                    removetask(n)
                except ValueError:
                    print("⚠️ Please enter a valid number!\n")
        elif ch == "4":
            print("👋 Goodbye!")
            break
        elif ch == "5":   # 👈 NEW OPTION
            keyword = input("Enter keyword to search: ")
            searchTasks(keyword)
        else:
            print("⚠️ Wrong choice!! Please choose from 1 - 5 :> \n")
