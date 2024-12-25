
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

note = {"Имя пользователя" : username, "Заголовоки" : titles, "Описание" : content,
        "Статус" : status, "Дата создания" : created_date1, "Дата истечения" : issue_date1}
print(note.items())