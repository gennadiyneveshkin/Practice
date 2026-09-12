# Анаграмма — это слово, которое можно составить с помощью перестановки букв другого слова. Например,  
# в английском языке анаграммами являются слова «live»
# и «evil», а в русском — «выбор» и «обрыв». Напишите
# программу, которая будет запрашивать у пользователя
# два слова, определять, являются ли они анаграммами,
# и выводить на экран ответ

# Мой вариант со сравнением множеств

first_word = (input('Введите первое слово: '))
second_word = (input('Введите второе слово: '))

if len(first_word) == len(second_word):
    first_word = set(first_word)
    second_word = set(second_word)

    def anagram (first_word, second_word):
        if first_word.issuperset(second_word):
            return True
        else:
            return False

    print (anagram (first_word, second_word))

# если слова разной длины, например "рак" и "кара"
# (без этой проверки выдаст True)
else:
    print(False)

# Мой вариант с циклами
# Для полностью правильной работы нужно добавить проверку на
# одинаковое количество символов в каждом из слов
# иначе например для слов "рак" и "кара" выдаст Да, что неверно

word_1 = list(input('Введите первое слово: '))
word_2 = list(input('Введите второе слово: '))

def anagram1 (word_1, word_2):
    for el in word_1:
        if el not in word_2:
            return 'Нет'
    return 'Да'

print(anagram1 (word_1, word_2))

# Вариант Эдюсон
# Простой и лаконичный

def is_anagram(word1, word2):
    return sorted(word1) == sorted(word2)
word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

# Если функция содержит True, тогда
if is_anagram(word1, word2):
    print("Слова являются анаграммами.")

# Иначе функция содержит False
else:
    print("Слова не являются анаграммами.")