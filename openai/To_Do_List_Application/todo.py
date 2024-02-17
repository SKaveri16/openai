import json

def load_tasks():
    try:
        with open('tasks.json', 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open('tasks.json', 'w') as file:
        json.dump(tasks, file)

def print_tasks(tasks):
    if not tasks:
        print("No tasks.")
    else:
        print("Tasks:")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task['description']} - {'(completed)' if task['completed'] else '(incomplete)'}")

def add_task(description, tasks):
    tasks.append({'description': description, 'completed': False})
    print("Task added.")

def delete_task(index, tasks):
    try:
        del tasks[index - 1]
        print("Task deleted.")
    except IndexError:
        print("Invalid task index.")

def mark_completed(index, tasks):
    try:
        tasks[index - 1]['completed'] = True
        print("Task marked as completed.")
    except IndexError:
        print("Invalid task index.")

def main():
    tasks = load_tasks()
    while True:
        print("\nWhat would you like to do?")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Mark a task as completed")
        print("4. View tasks")
        print("5. Quit")
        choice = input("Enter your choice: ")

        if choice == '1':
            description = input("Enter task description: ")
            add_task(description, tasks)
        elif choice == '2':
            index = int(input("Enter the index of the task to delete: "))
            delete_task(index, tasks)
        elif choice == '3':
            index = int(input("Enter the index of the task to mark as completed: "))
            mark_completed(index, tasks)
        elif choice == '4':
            print_tasks(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
