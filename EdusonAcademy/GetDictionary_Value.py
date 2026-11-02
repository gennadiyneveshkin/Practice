# Напишите функцию get_value, которая принимает на вход словарь data и ключ key.
# Функция должна возвращать значение из словаря data, соответствующее переданному ключу key.
# Если ключ отсутствует в словаре, функция должна возвращать строку "Key not found".

# Мой вариант
def get_value (data, key):
    if key not in data:
        return "Key not found"
    return data[key]

# Вариант Алисы, более лаконичный!
def get_value(data, key):

    # Возьми из словаря data значение по ключу key и верни его,
    # а если его нет верни значение по умолчанию "Key not found"
    return data.get(key, "Key not found")

# Вариант Эдюссон
# Сработает некорректно!, если значение в словаре по ключу это слово None
def get_value(data, key):
    value = data.get(key)
    return value if value is not None else "Key not found"
