# Напишите программу, которая будет считывать содержимое файла, добавлять к считанным
# строкам порядковый номер и сохранять их в таком виде в новом файле
# Каждая строка в созданном файле должна начинаться с ее номера, двоеточия и пробела
# после чего должен идти текст строки из исходного файла.

file_new =  open('../Test/test5.txt', 'a', encoding='utf-8')
with open('../Test/test4.txt', 'r', encoding='utf-8') as file:
    file_splitted = file.readlines()
    print(file_splitted)

    for i, el in enumerate(file_splitted):

        # Добавляем в начале строки порядковый номер, двоеточие и пробел с помощью конкатенации
        el = str(i+1) + ': ' + el
        file_new.write(el)

file_new.close()
