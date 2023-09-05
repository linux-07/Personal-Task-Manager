from datetime import datetime

# Create an empty tasks list
tasks = []

# Create or open the tasks file
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
            file.write(f"Status: {'completed' if task['completed'] else 'pending'}\n\n")


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
                    task_info["completed"] = (line[len("Status: "):] == "completed")
                elif not line:
                    tasks.append(task_info)
                    task_info = {}
    except FileNotFoundError:
        pass


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
        print("Invalid date format. Use DD-MM-YYYY.")
        return

    task = {
        "title": title,
        "description": description,
        "due_date": due_date.strftime("%d-%m-%Y"),
        "completed": False
    }

    tasks.append(task)
    save_tasks()
    print("Task added successfully!")


def mark_completed():
    list_tasks()
    try:
        task_index = int(input("Enter the index of the task that you want to mark as completed: "))
        if 1 <= task_index <= len(tasks):
            tasks[task_index - 1]["completed"] = True
            save_tasks()
            print("Task Marked as Completed ✅")
        else:
            print("Enter a valid task index.")
    except ValueError:
        print("Invalid Input. Please enter a valid number")


def main():
    load_tasks()

    while True:
        print("\nTask Manager Menu:")
        print("1. List Tasks")
        print("2. Add Task")
        print("3. Mark Task as Completed")
        print("4. Quit")

        try:
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
        except ValueError:
            print("Invalid input. Please enter a valid number.")


if __name__ == "__main__":
    main()
