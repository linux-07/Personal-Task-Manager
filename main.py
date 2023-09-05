from datetime import datetime

# Create Empty Tasks list
tasks = []

# Create tasks file
try:
    x = open("tasks.txt", 'x')
    x.close()

except FileExistsError:
    pass

def save_tasks():
    with open("tasks.txt", 'w') as file:
        for task in tasks:
            file.write(f"Title: {task['title']}\n")
            file.write(f"Description: {task['description']}\n")
            file.write(f"Due Date: {task['due_date']}\n")
            file.write(f"Status: {'completed' if task['completed'] else 'pending'}\n\n") # --> Short hand if-else used in the line

def load_tasks():
    try:
        with open("tasks.txt", 'r') as file:
            lines = file.readlines()
            task_info = {}
            for line in lines:
                line = line.strip()
                if line.startswith("Title: "):
                    task_info["title"] = line[len("Title: "):]
                elif line.startswith("Description: "):
                    task_info["description"] = line[len("Description: "):]
                elif line.startswith("Due Date: "):
                    task_info["due_date"] = line[len("Due Date: "):]
                elif line.startswith("Status: "):
                    task_info["completed"] = (line[len("Status: "):] == "Completed")
                elif not line:
                    tasks.append(task_info)
                    task_info = {}
    except:
        raise FileNotFoundError

def list_tasks():
    if not tasks:
        print("No tasks found.")
    else:
        for index, task in enumerate(tasks, 1):
            print(f"{index}. Title: {task['title']}")
            print(f"   Description: {task['description']}")
            print(f"   Due Date: {task['due_date']}")
            print(f"   Status: {'Completed' if task['completed'] else 'Pending'}")

def add_task():
    title = input("Enter task title: ")
    description = input("Enter task description: ")
    due_date = input("Enter due date (YYYY-MM-DD): ")

    try:
        due_date = datetime.strptime(due_date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date.strftime("%Y-%m-%d"),
        "completed": False
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")

def mark_completed():
    list_tasks()
    task_index = int(input("Enter the index of the task that you want to mark as completed: "))
    try:
        task_index = task_index - 1
        if 0<= task_index < len(tasks):
            task_index[task_index]["completed"] = True
            save_tasks()
            print("Task Marked as Completed ✅")
        else:
            print("Enter a valid task index.")
    except ValueError:
        print("Invalid Input. Please enter a valid number")

def main():
    tasks.extend(load_tasks())

    while True:
        print("\nTask Manager Menu:")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            list_tasks()
        elif choice == 2:
            add_task()
        elif choice == 3:
            mark_completed()
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()