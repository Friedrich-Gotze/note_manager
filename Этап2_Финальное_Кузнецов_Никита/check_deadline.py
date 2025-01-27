import datetime

current_datetime = datetime.datetime.now()
print("Текущая дата:", current_datetime.strftime("%d-%m-%Y"))

create_date = input("Введите дату дедлайна (в формате день-месяц-год): ")
create_date1 = datetime.datetime.strptime(create_date, format("%d-%m-%Y"))
date = (create_date1 - current_datetime).days

while True:
    if date < 0:
        print(f"Внимание! Дедлайн истёк {date} дней назад!")
    elif date > 0:
        print(f"До дедлайна осталось {date} дней")
    else:
        print("Дедлайн сегодня!")

    print("Для выхода нажмите Enter")
    input()
    break

