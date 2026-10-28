tasks = []

def add_task():
    title = input("Введите задачу: ")
    tasks.append({"title": title, "done": False})
    print("Задача добавлена!")

def show_tasks():
    if not tasks:
        print("Список задач пуст.")
        return

    for i, task in enumerate(tasks, start=1):
        status = "Выполнено" if task["done"] else "Не выполнено"
        print(f"{i}. {task['title']} — {status}")

def complete_task():
    show_tasks()
    if not tasks:
        return

    try:
        number = int(input("Номер задачи: "))
        if 1 <= number <= len(tasks):
            tasks[number - 1]["done"] = True
            print("Задача выполнена!")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите число.")

def delete_task():
    show_tasks()
    if not tasks:
        return

    try:
        number = int(input("Номер задачи: "))
        if 1 <= number <= len(tasks):
            tasks.pop(number - 1)
            print("Задача удалена!")
        else:
            print("Неверный номер.")
    except ValueError:
        print("Введите число.")

while True:
    print("\n--- TO-DO MANAGER ---")
    print("1. Добавить задачу")
    print("2. Показать задачи")
    print("3. Выполнить задачу")
    print("4. Удалить задачу")
    print("0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        show_tasks()
    elif choice == "3":
        complete_task()
    elif choice == "4":
        delete_task()
    elif choice == "0":
        print("Программа завершена.")
        break
    else:
        print("Неверный выбор.")
