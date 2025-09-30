import json
from datetime import datetime

# ===============================
# 📝 TO-DO APP with Extra Features
# ===============================
# Features:
# 1. Add Task (with priority + optional deadline)
# 2. Show Tasks (sorted by priority + deadline)
# 3. Remove Task
# 4. Mark Task as Completed
# 5. Edit Task
# 6. Search Task
# 7. Save & Load Tasks (persistent storage)
# 8. Clear All Tasks
# 9. Exit
# 10. View Statistics
# ===============================

tasks = []


# ---------- Save & Load ----------
def savetasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)


def loadtasks():
    global tasks
    try:
        with open("tasks.json", "r") as f:
            tasks = json.load(f)
    except FileNotFoundError:
        tasks = []


# ---------- Core Functions ----------
def addtask(task, priority="Medium", deadline=None):
    tasks.append({
        "task": task,
        "done": False,
        "priority": priority,
        "deadline": deadline
    })
    print(f"✅ Task added: {task} [Priority: {priority}] {f'(Due: {deadline})' if deadline else ''}\n")
    savetasks()


def showTasks():
    if not tasks:
        print("📋 No tasks yet.\n")
        return

    priority_order = {"High": 1, "Medium": 2, "Low": 3}
    sorted_tasks = sorted(tasks, key=lambda t: (
        priority_order.get(t["priority"], 4),
        t["deadline"] if t["deadline"] else "9999-99-99"
    ))

    print("\n📌 Your Tasks:")
    for i, task in enumerate(sorted_tasks, 1):
        status = "✔️" if task["done"] else "❌"
        deadline = f"(Due: {task['deadline']})" if task["deadline"] else ""
        print(f"   {i}. {task['task']} [{status}] [Priority: {task['priority']}] {deadline}")
    print()


def searchTasks(keyword):
    found = [task for task in tasks if keyword.lower() in task["task"].lower()]
    if not found:
        print(f"🔍 No tasks found containing '{keyword}'.\n")
    else:
        print(f"\n🔍 Tasks containing '{keyword}':")
        for i, task in enumerate(found, 1):
            status = "✔️" if task["done"] else "❌"
            print(f"   {i}. {task['task']} [{status}]")
        print()


def removetask(tasknumber):
    if 0 < tasknumber <= len(tasks):
        removed = tasks.pop(tasknumber - 1)
        print(f"🗑️ Task removed: {removed['task']}\n")
        savetasks()
    else:
        print("⚠️ Invalid task number!\n")


def markdone(tasknumber):
    if 0 < tasknumber <= len(tasks):
        tasks[tasknumber - 1]["done"] = True
        print(f"✅ Task marked as completed: {tasks[tasknumber - 1]['task']}\n")
        savetasks()
    else:
        print("⚠️ Invalid task number!\n")


def edittask(tasknumber, newtask):
    if 0 < tasknumber <= len(tasks):
        old = tasks[tasknumber - 1]["task"]
        tasks[tasknumber - 1]["task"] = newtask
        print(f"✏️ Edited: '{old}' → '{newtask}'\n")
        savetasks()
    else:
        print("⚠️ Invalid task number!\n")


def clearAll():
    confirm = input("⚠️ Are you sure you want to clear ALL tasks? (y/n): ")
    if confirm.lower() == "y":
        tasks.clear()
        savetasks()
        print("🧹 All tasks cleared!\n")
    else:
        print("❌ Clear all cancelled.\n")


# ---------- New Feature: Statistics ----------
def viewStatistics():
    if not tasks:
        print("📊 No tasks to analyze yet.\n")
        return

    total = len(tasks)
    completed = sum(1 for t in tasks if t["done"])
    pending = sum(1 for t in tasks if not t["done"])
    not_finished = total - completed  # basically same as pending

    print("\n📊 --- Task Statistics ---")
    print(f"📌 Total tasks: {total}")
    print(f"✅ Completed: {completed}")
    print(f"🕒 Pending: {pending}")
    print(f"❌ Not Finished: {not_finished}\n")


# ---------- Main Menu ----------
def main():
    loadtasks()

    while True:
        print("=" * 40)
        print("📝 TO-DO APP")
        print("=" * 40)
        print("1. ➕ Add Task")
        print("2. 📋 Show Tasks")
        print("3. 🗑️ Remove Task")
        print("4. ✅ Mark Task as Completed")
        print("5. ✏️ Edit Task")
        print("6. 🔍 Search Task")
        print("7. 💾 Save Tasks")
        print("8. 🧹 Clear All Tasks")
        print("9. 🚪 Exit")
        print("10. 📊 View Statistics")
        print("=" * 40)

        ch = input("👉 Enter choice: ")

        if ch == "1":
            t = input("✏️ Enter task: ")
            p = input("🔺 Enter priority (High/Medium/Low): ") or "Medium"
            d = input("⏰ Enter deadline (YYYY-MM-DD) or leave blank: ") or None
            if d:
                try:
                    datetime.strptime(d, "%Y-%m-%d")
                except ValueError:
                    print("⚠️ Invalid date format! Deadline ignored.\n")
                    d = None
            addtask(t, p, d)

        elif ch == "2":
            showTasks()

        elif ch == "3":
            showTasks()
            if tasks:
                try:
                    n = int(input("Enter task no. to remove: "))
                    removetask(n)
                except ValueError:
                    print("⚠️ Please enter a valid number!\n")

        elif ch == "4":
            showTasks()
            if tasks:
                try:
                    n = int(input("Enter task no. to mark done: "))
                    markdone(n)
                except ValueError:
                    print("⚠️ Please enter a valid number!\n")

        elif ch == "5":
            showTasks()
            if tasks:
                try:
                    n = int(input("Enter task no. to edit: "))
                    newt = input("Enter new task text: ")
                    edittask(n, newt)
                except ValueError:
                    print("⚠️ Please enter a valid number!\n")

        elif ch == "6":
            keyword = input("Enter keyword to search: ")
            searchTasks(keyword)

        elif ch == "7":
            savetasks()
            print("💾 Tasks saved!\n")

        elif ch == "8":
            clearAll()

        elif ch == "9":
            print("👋 Goodbye! Stay productive.")
            break

        elif ch == "10":
            viewStatistics()

        else:
            print("⚠️ Wrong choice!! Please choose from 1 - 10 :> \n")


main()
