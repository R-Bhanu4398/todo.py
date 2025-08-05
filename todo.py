def get_task():
    b = []
    try:
        file = open("tasks.txt", "r")
        b = file.read().splitlines()
        file.close()
    except FileNotFoundError:
        pass
    return b

def save_tasks(b):
    file = open("tasks.txt", "w")
    for i in b:
        file.write(i + "\n")
    file.close()

def view_task(b):
    if not b:
        print("No task available")
    else:
        print("\nTasks:")
        for j, i in enumerate(b, 1):
            print(f"{j}. {i}")

def add_task(b):
    i = input("Enter new task: ")
    b.append(i)
    save_tasks(b)
    print("Task Added")

def remove_task(b):
    view_task(b)
    if b:
        try:
            n = int(input("Enter task number to remove: "))
            if 1 <= n <= len(b):
                removed = b.pop(n - 1)
                save_tasks(b)
                print(f"Removed: {removed}")
            else:
                print("Invalid number")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        print("\n1. View Tasks")
        print("2. Add Task")
        print("3. Remove Task")
        print("4. Exit")
        a = input("Enter your option: ")
        b = get_task() 

        if a == "1":
            view_task(b)
        elif a == "2":
            add_task(b)
        elif a == "3":
            remove_task(b)
        elif a == "4":
            break
        else:
            print("Invalid option")

main()
