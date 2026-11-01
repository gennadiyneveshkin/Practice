# Даны два словаря dict1 и dict2. Напишите функцию merge_dicts, которая объединит эти два словаря.
# В начале результирующего словаря должны идти ключи dict1.
# Значения с общими ключами должны стать элементами общего списка в результирующем словаре.
# Функция merge_dicts должна вернуть результирующий словарь.

# Мое решение
def merge_dicts (dict1, dict2):

    # Создаем результирующий словарь путем копирования dict1
    merged_dict = dict1.copy()

    # Идем по элементам dict2
    # С помощью метода items() поочередно получаем пары ключ-значене словаря
    for key, value in dict2.items():

        # Если ключ из dict2 есть в merged_dict (а значит и в dict1)
        if key in merged_dict:

            # Перезаписываем значение по этому ключу в виде списка с двумя значениями
            # merged_dict[key] - лежавшее там до этого значиние из первого словаря (остается)
            # value - значение из второго словая (добавляем)
            merged_dict[key] = [merged_dict[key], value]

        # Просто записываем в merged_dict новую пару ключ-значение из второго словаря
        else:
            merged_dict[key] = value
    return merged_dict


# Решение Эдюссон
# Более универсальное, поскольку есть проверка isinstance - возможно одиночные элементы это уже списки изначально
# Возможно масштабироваться, если словарей будет больше двух

def merge_dicts(dict1, dict2):
    result_dict = dict1.copy()

    for key, value in dict2.items():
        if key in result_dict:
            if isinstance(result_dict[key], list):
                result_dict[key].append(value)
            else:
                result_dict[key] = [result_dict[key], value]
        else:
            result_dict[key] = value

    return result_dict