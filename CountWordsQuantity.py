# Посчитать количество слов "тайна" в предложении

text = 'Это секретное сообщение: тайна, тайна и ещё раз тайна.'
text_length = len (text)
quantity = 0
index = 0
while index <= text_length:
    position_secret = text.find('секретное', index)
    index += position_secret + 1
    quantity += 1
else:
    print ('вхождений не найдено')
print(quantity)