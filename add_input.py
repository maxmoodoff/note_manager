# запрашиваем информацию

username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# запрашиваем несколько заголовок и добавляем их в список

title1 = input("Введите первый заголовок заметки: ")
title2 = input("Введите второй заголовок заметки: ")
title3 = input("Введите третий заголовок заметки: ")
titles = [title1, title2, title3]

# выводим данные

print("Вы ввели следующие данные:")
print("Имя пользователя:", username)
print("Заголовок заметки:", titles)
print("Описание заметки:", content)
print("Статус заметки:",status)
print("Дата создания заметки:", created_date)
print("Дата истечения заметки:", issue_date)
