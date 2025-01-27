
titles = []

title1 = input("Введите заголовок заметки (или оставьте пустым для завершения): ")
while title1 != "":
    titles.append(title1)
    title1 = input("Введите заголовок заметки (или оставьте пустым для завершения): ")

print("\nЗаголовки заметки:")
for title1 in titles:
    print(title1)






