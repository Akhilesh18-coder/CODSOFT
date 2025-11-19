tasks = []  # this will store all your tasks

def show_tasks():
    if len(tasks) == 0:
        print("\nNo tasks yet!\n")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks):
            print(f"{i+1}. {task}")
        print()

def add_task():
    task = input("Enter a new task: ")
    tasks.append(task)
    print("Task added!\n")

def delete_task():
    show_tasks()
    if len(tasks) == 0:
        return
    num = int(input("Enter the task number to delete: "))
    if 1 <= num <= len(tasks):
        tasks.pop(num - 1)
        print("Task deleted!\n")
    else:
        print("Invalid number!\n")

def main():
    while True:
        print("===== TO-DO LIST APP =====")
        print("1. Show tasks")
        print("2. Add task")
        print("3. Delete task")
        print("4. Exit")

        choice = input("Choose 1-4: ")

        if choice == "1":
            show_tasks()
        elif choice == "2":
            add_task()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, try again.\n")

main()
