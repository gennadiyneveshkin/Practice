# Напишите функцию is_palindrome(text), которая определяет, является ли слово палиндромом, и возвращает True или False.
# Сравнение должно быть регистронезависимым: «Радар» тоже считается палиндромом.

def is_palindrome(text):
    text = text.lower()
    text_reversed = text[::-1]
    if text == text_reversed:
        return True
    return False

print(is_palindrome('Радар'))

