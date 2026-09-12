# Напишите функцию decipher(), которая заменит все числа в строке на буквы
# русского алфавита. Функция должна принимать один аргумент —
# строку с целыми числами от 0 до 32, между которыми стоит пробел.
# В качестве ответа верните строку с последовательностью букв без пробелов
# и других разделителей. Используйте только строчные буквы.

from shlex import join

alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def decipher(message):

    # Из строки с цифрами делаем список из цифр
    message_list = message.split()

    # Пустой список для сборки расшифрованного сообщения
    decrypted_message = []

    # Идем по каждой цифре из списка из цифр
    for el in message_list:

        # Добавляем в decrypted_message из alphabet букву по индексу el
        decrypted_message.append(alphabet[int(el)])

    # Преобразовываем список букв расшифрованного сообщения в строку
    decrypted_message = ''.join(decrypted_message)

    return decrypted_message

print(decipher('13 0 13 0'))


alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def decipher(message):

    message_list = message.split()
    decrypted_message = ''

    for el in message_list:

        # TODO Сложение букв !!! вместо append
        decrypted_message += alphabet[int(el)]

    return decrypted_message

print(decipher('13 0 13 0'))

a = 'дом'
b = 'свет'
res = ''
res = b[3] + a[1] + a[2]
print(res)

