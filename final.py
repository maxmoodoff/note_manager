# создаем словарь для хранения информации о заметке

note = {}

# собираем данные пользователя

note['username'] = input('Введите имя пользователя: ')
note['content'] = input('Введите содержание заметки: ')
note['status'] = input('Введите статус заметки (например, "Активна", "Выполнена"): ')
note['created_date'] = input('Введите дату создания заметки в формате "день-месяц-год": ')
note['issue_date'] = input('Введите дату изменения заметки в формате "день-месяц-год": ')

# добавляем заголовки списком в словарь

note['titles'] = []
for i in range(3):
    title = input(f'Введите заголовок заметки {i + 1}: ')
    note['titles'].append(title)

# выводим данные

print('\nСобранная информация о заметке:')
for key, value in note.items():
    print(f'{key.capitalize()}: {value}')
