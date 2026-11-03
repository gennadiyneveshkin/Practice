# Нельзя писать так: yesterday = orders
# потому что сторока orders.clear() сотреть данные и в orders и в yesterday
# потому что при такой записи и yesterday и orders ссылаются на !!! одну и ту же ячейку памяти
# нужно работать через .copy()
# тогда для yesterday создастся другая ячейка памяти, данные в которой сохранятся после
# выполнения команды orders.clear()

orders = [1250, 830, 2100, 640]

yesterday = orders.copy()
orders.clear()
print("Заказы за вчера:", yesterday)
print("Заказы за сегодня:", orders)