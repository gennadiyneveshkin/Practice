ages = [10, 16, 67, 44, 18, 53]
result = [adult for adult in ages if adult > 18]
print(result)


numbers = [int(input(f'Введите {i+1} число: ')) for i in range(3)]
print(numbers)