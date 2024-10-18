# Task Manager CLI

A simple, command-line interface (CLI) task manager built with Python. This script allows users to **add**, **list**, and **remove** tasks, storing them in a JSON file for persistence.

## Features

- Add tasks with descriptions
- List all tasks with numbering
- Remove tasks by specifying their number
- Tasks are stored in a `tasks.json` file for easy management

## Prerequisites

- Python 3.x
- No external libraries needed (uses standard Python modules)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/task-manager-cli.git
   cd task-manager-cli
   ```

2. No additional dependencies are required.

## Usage

### 1. Add a Task

To add a new task, use the `add` action with the `--task` argument:

```bash
python task_manager.py add --task "Complete GitHub project"
```

### 2. List All Tasks

To view all the tasks in your task list, use the `list` action:

```bash
python task_manager.py list
```

### 3. Remove a Task

To remove a task by its number (as shown in the task list), use the `remove` action with the `--index` argument:

```bash
python task_manager.py remove --index 1
```

### Example

Here’s an example of adding, listing, and removing tasks:

```bash
# Add tasks
python task_manager.py add --task "Complete GitHub project"
python task_manager.py add --task "Study algorithmic trading"

# List tasks
python task_manager.py list

# Remove the first task
python task_manager.py remove --index 1
```

## File Structure

```
task-manager-cli/
│
├── task_manager.py   # The main script
├── tasks.json        # Stores tasks (generated after running the script)
└── README.md         # This README file
```

## Future Improvements

- Add task priorities
- Set task due dates
- Mark tasks as complete
- Sort tasks by priority or due date

## License

This project is open-source and available under the [MIT License](LICENSE).

---

This README provides clear instructions and a good overview of the project, making it easy for others to understand and use.
