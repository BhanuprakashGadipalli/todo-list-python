def show_menu():
    print("\n=== TO-DO LIST ===")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Done")
    print("4. Delete Task")
    print("5. Exit")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = [line.strip() for line in file.readlines()]
    except FileNotFoundError:
        tasks = []
    return tasks

def save_tasks(tasks):
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")

def view_tasks(tasks):
    if not tasks:
        print("No tasks yet!")
    else:
        for idx, task in enumerate(tasks, 1):
            print(f"{idx}. {task}")

def add_task(tasks):
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added.")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: "))
        if 1 <= num <= len(tasks):
            tasks[num-1] += " ✅"
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"Deleted: {removed}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
