# Посчитать количество повторяющихся слов в предложении
import re


def count_words (sentence, word):
    words = re.split('[:, ]', sentence)
    print(words)
    counter = 0
    for el in words:
        if el == word:
            counter += 1
    return counter

print(count_words ('Это секретное сообщение: тайна, тайна, тайна и еще раз тайна', 'тайна'))


