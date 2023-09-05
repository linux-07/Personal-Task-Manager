from datetime import datetime

# Create Empty Tasks list
tasks = []

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