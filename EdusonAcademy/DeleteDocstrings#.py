# Напишите программу, которая будет удалять все комментарии из исходного файла с кодом

# Мой вариант, не учитывает, что докстринг може быть в строке после кода
# Например x = 5 # это комментарий



# В file_new собираем код без докстрингов
with open('../Test/test2.py', 'a', encoding = 'utf8') as file_new:
    try:
        with open ('../Test/test1.py', 'r', encoding='utf8') as file:

            # Читаем файл с докстрингами в список content который состоит из строк
            content = file.readlines()

            # Проверяем начинается ли строка с #
            for el in content:
                if el[0] != '#':

                    # Если нет, записываем ее в file_new
                    file_new.write(el)
    except FileNotFoundError:
        print('Не удалось открыть файл')

# Вариант Эдюсон

def remove_comments(file_name, new_file_name):
    try:
        with open(file_name, "r") as file:
            content = file.readlines()
            stripped_content = []
            for line in content:
                stripped_line = line.split("#")[0].strip()
                stripped_content.append(stripped_line)
        with open(new_file_name, "w") as new_file:
            new_file.write("\n".join(stripped_content))
    except:
        print('Не удалось открыть входной файл')

file_name = input("Введите имя входного файла: ")
new_file_name = input("Введите имя файла для вывода: ")
remove_comments(file_name, new_file_name)
