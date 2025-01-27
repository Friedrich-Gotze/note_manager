status = 0

while True:
    if status == 0:
        print("\nВаша заметка отложена")
    elif status == 1:
        print("\nВаша заметка в процессе")
    elif status == 2:
        print("\nВаша заметка выполнена")

    print("Выберите статус заметки: ")
    print("0 - Отложена")
    print("1 - В процессе")
    print("2 - Выполнена")
    print("3 - Выход")

    status = int(input("Ваш выбор: "))

    if status == 3:
        break

    if status > 3:
        print("Выберете число от 0 до 3")