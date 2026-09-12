# Проверить начинается ли предложение с заглавной буквы
# И стоит ли в конце предложения точка

text = 'my name is Bob'
letter = text[0:1]
result = letter.isupper()
if result == True:
    print ('ОК')
else:
    print ('Первая буква предложения должна быть заглавной')
point = text.find('.')
if point == -1:
    print('В конце предложения должна стоять точка')
else:
    print('ОК')
