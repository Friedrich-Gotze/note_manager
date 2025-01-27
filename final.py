
username = input("Имя пользователя: ")
title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")
titles = [title1, title2, title3]
content = input("Описание: ")
status = input("Статус: ")
created_date = input("Дата создания в формате дд-мм-гг, например 10-11-2024: ")
created_date1 = created_date[:5]
issue_date = input("Дата истечения в формате дд-мм-гг, например 10-11-2024: ")
issue_date1 = issue_date[:5]

note = {"Имя пользователя" : username,
        "Заголовоки" : titles,
        "Описание" : content,
        "Статус" : status,
        "Дата создания" : created_date1,
        "Дата истечения" : issue_date1}

print("\nВы ввели следующие данные:")
print("Имя пользователя:", note["Имя пользователя"])
print("Заголовоки:", note["Заголовоки"])
print("Описание:", note["Описание"])
print("Статус:", note["Статус"])
print("Дата создания:", note["Дата создания"])
print("Дата истечения:", note["Дата истечения"])