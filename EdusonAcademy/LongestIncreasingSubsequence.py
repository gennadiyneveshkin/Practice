# Создайте функцию longest_increasing_subsequence, которая находит длину наибольшей возрастающей подпоследовательности
# в массиве чисел.Возрастающая подпоследовательность — это последовательность чисел, где каждое следующее число
# больше предыдущего, не обязательно подряд. Например, в массиве [10, 9, 2, 5, 3, 7, 101, 18] наибольшими возрастающими
# подпоследовательностями будут [2, 3, 7, 101] или [2, 5, 7, 18], их длина равна 4.
# Функция longest_increasing_subsequence принимает на вход список целых чисел.
# В качестве ответа функция должна вернуть длину наибольшей возрастающей подпоследовательности.
# Используйте динамическое программирование для решения задачи.

def longest_increasing_subsequence(nums):
    if not nums:
        return 0

    n = len(nums)
    # memo[i] — длина наибольшей возрастающей подпоследовательности,
    # которая начинается с элемента nums[i]
    memo = {}

    def lis_from(idx):
        if idx in memo:
            return memo[idx]

        best = 1
        for i in range(idx + 1, n):
            if nums[i] > nums[idx]:
                best = max(best, 1 + lis_from(i))

        memo[idx] = best
        return best

    counter = 0
    for i in range(n):
        counter = max(counter, lis_from(i))

    return counter