# Дан список целых чисел nums, в котором вперемешку встречаются нули и другие числа. Нужно переместить все нули в конец списка,
# сохранив при этом порядок остальных чисел друг относительно друга.
# Напишите функцию move_zeroes(nums), которая возвращает список nums с перемещёнными в конец нулями. Порядок ненулевых чисел менять нельзя.

def move_zeroes(nums):
    zeroes = [0 for x in nums if x == 0] # список из нулей
    nums = [x for x in nums if x != 0] # список из всех элементов, кроме нулей
    nums += zeroes
    return nums

nums = [0, 0, 0]
print(move_zeroes(nums))

# Аналогичный вариант:
def move_zeroes(nums):
    non_zeros = [x for x in nums if x != 0]
    zeros_count = len(nums) - len(non_zeros)
    return non_zeros + [0] * zeros_count

# Более сложный, но Интересный! вариант, где мы идем с конца списка
def move_zeroes(nums):
    index = len(nums) - 1
    zeroes = []
    while index >= 0:
        if nums[index] == 0:
            zeroes.append(nums[index])
            nums.pop(index)
        index -= 1 # TODO Уменьшаем индекс на 1 вне зависимости от того, равен элемент 0 или нет
    nums = nums + zeroes
    return nums


nums = [0, 1, 0, 1, 3, 2, 0]
print(move_zeroes(nums))