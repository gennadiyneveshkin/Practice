# Здесь будем хранить названия файлов, введенные пользователем
files = []
while True:
    file = input('Введите имя файла: ')
    if file == '':
        break
    files.append(file)

# Открываем файл, в который будем добавлять данные из всех других файлов
file_result = open(f'../Test/test.txt', 'a', encoding='utf8')

# Поочерередно пытаемся открыть каждый из файлов
for el in files:
    try:
        # Если удалось, записываем данные из него в file_result
        with open(f'../Test/{el}', 'r', encoding='utf8') as file:
            file = file.read()
            file_result.write(file + '\n')

    # Если не удалось, выдаем сообщение об ошибке
    except FileNotFoundError:
        print(f'Не удалось открыть файл {el}')

file_result.close()

