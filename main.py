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
