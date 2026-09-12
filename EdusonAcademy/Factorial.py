# Вычислить факториал числа n

# Решение с помощью цикла for
n = 5
result = 1
for i in range (n):
    result *= (i + 1)
print(result)

# Решение с помощью цикла while
n = 5
result = 1
i = 1
while i < n:
    result *= (i + 1)
    i += 1
print (result)