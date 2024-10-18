import argparse
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

# Load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks to file
def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add a new task
def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task})
    save_tasks(tasks)
    print(f"Task added: {task}")

# List all tasks
def list_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task['task']}")

# Remove a task by index
def remove_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        save_tasks(tasks)
        print(f"Removed task: {removed_task['task']}")
    else:
        print("Invalid task number.")

# Set up the command-line interface
def main():
    parser = argparse.ArgumentParser(description="Simple Task Manager CLI")
    
    parser.add_argument("action", choices=["add", "list", "remove"], help="Action to perform")
    parser.add_argument("--task", type=str, help="Task description for 'add' action")
    parser.add_argument("--index", type=int, help="Task index for 'remove' action")

    args = parser.parse_args()

    if args.action == "add":
        if args.task:
            add_task(args.task)
        else:
            print("Please provide a task description with --task.")
    elif args.action == "list":
        list_tasks()
    elif args.action == "remove":
        if args.index is not None:
            remove_task(args.index - 1)
        else:
            print("Please provide the task number to remove with --index.")

if __name__ == "__main__":
    main()
