# Шаг 1. Заказ из чат-бота
order = "  Латте:2, круассан:1, КАПУЧИНО:1 "

clean = order.strip()
clean = clean.lower()
items = clean.split(", ")

# Шаг 2. Позиции заказа
pos1 = items[0].split(':')
pos1 = (pos1[0], int(pos1[1]))
pos2 = items[1].split(':')
pos2 = (pos2[0], int(pos2[1]))
pos3 = items[2].split(':')
pos3 = (pos3[0], int(pos3[1]))
print(pos1, pos2, pos3)










