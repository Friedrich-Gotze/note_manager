
username = input("Имя пользователя: ")
title1 = input("Введите первый заголовок: ")
title2 = input("Введите второй заголовок: ")
title3 = input("Введите третий заголовок: ")
titles = [title1, title2, title3]
content = input("Описание: ")
status = input("Статус: ")
created_date = input("Дата создания в формате дд-мм-гггг, например 10-11-2024: ")
issue_date = input("Дата истечения в формате дд-мм-гггг, например 10-11-2024: ")

print("Вы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок:", titles)
print("Описание:", content)
print("Статус:", status)
print("Дата создания:", created_date [:5])
print("Дата истечения:", issue_date [:5])

