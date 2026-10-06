


def find_longest_word(file_path):

    # Открываем файл с помощью контекстного менеджера with для чтения как file
    with open(file_path, 'r') as file:

        # Считываем содержимое файла в переменную content
        content = file.read()

        # Разбиваем строку content по пробелам, получаем список из слов
        words = content.split()

        # Находим самое длинное слово с помощью функции max и ключа len
        longest_word = max(words, key=len)

        longest = len(longest_word)
        longest_words = []

        for el in words:
            if len(el) == longest:
                longest_words.append(el)
    # TODO Возвращаем сразу ДВА! значения - это кортеж из числа и списка
    return longest, longest_words

file_path = '../Test/test3.txt'

print(find_longest_word(file_path))
# TODO Распаковываем кортеж
longest, longest_words = find_longest_word(file_path)

print('Максимальная длина символов в одном слове: ', longest)
print('Слова максимальной длины: ', longest_words)