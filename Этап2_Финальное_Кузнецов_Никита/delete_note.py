
print("Добро пожаловать в 'Менеджер заметок'!")

notes = []

while True:
    print("1 - Добавить заметку")
    print("2 - Вывести список заметок")
    print("3 - Удалить заметку")
    print("4 - Выход\n")

    didi = int(input("Выберите действие: "))

    if didi == 1:
        note = {"Имя пользователя": input("Имя пользователя: "),
                "Заголовоки": input("Введите заголовок: "),
                "Описание": input("Описание: "),
                "Статус": input("Статус: "),
                "Дата создания": input("Дата создания в формате дд-мм-гггг, например 10-11-2024: "),
                "Дата истечения": input("Дата истечения в формате дд-мм-гггг, например 10-11-2024: ")}

        notes.append(note)

        miki = input("\nХотите добавить ещё одну заметку? (да/нет): ")

        if miki == "да":
            note = {"Имя пользователя": input("Имя пользователя: "),
                    "Заголовоки": input("Введите заголовок: "),
                    "Описание": input("Описание: "),
                    "Статус": input("Статус: "),
                    "Дата создания": input("Дата создания в формате дд-мм-гггг, например 10-11-2024: "),
                    "Дата истечения": input("Дата истечения в формате дд-мм-гггг, например 10-11-2024: ")}

            notes.append(note)
            miki = input("\nХотите добавить ещё одну заметку? (да/нет): ")

        elif miki == "нет":
            print()

    elif didi == 2:
        print("\nСписок всех заметок:")
        for idx, note in enumerate(notes, start = 1):
                print(f"Заметка {idx}:")
                for key, value in note.items():
                    print(f"  {key}: {value}")
        print()

    elif didi == 3:
        name = input("Введите имя пользователя или заголовок для удаления заметки: ")
        for note in notes:
            for value in note.values():
                if value == name:
                    notes.remove(note)
        print("Ваша заметка успешно удалена!")

    elif didi == 4:
        break