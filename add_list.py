# запрашиваем информацию

username = input("Введите имя пользователя: ")
content = input("Введите описание заметки: ")
status = input("Введите статус заметки (например 'Активна', 'Выполнена'): ")
created_date = input("Введите дату создания заметки в формате 'день-месяц-год': ")
issue_date = input("Введите дату истечения заметки в формате 'день-месяц-год': ")

# создаем список заголовков заметки

titles = []
for i in range(3):
 title = input(f"Введите заголовок заметки {i + 1}: ")
 titles.append(title)

# выводим данные

 print("Вы ввели следующие данные:")
 print("Имя пользователя:", username)
 print("Заголовок заметки:", titles)
 print("Описание заметки:", content)
 print("Статус заметки:", status)
 print("Дата создания заметки:", created_date)
 print("Дата истечения заметки:", issue_date)
