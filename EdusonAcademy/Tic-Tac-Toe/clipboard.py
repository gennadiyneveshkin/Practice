# board = [[11, 12, 13],
#         [11, 22, 23],
#         [11, 32, 33]]
#
# for i in range(3):
#     a = [x[i] for x in board]
#     print(a)
#     if all(a) == 11:
#         print (True)
#
#
#
# for i in range(3):
#     if all([x[i] == 11 for x in board]):
#         print (True)
#     else:
#         print(False)

list = [1, 1, 1, 1]
if all(x == 1 for x in list):
# если все элементы в списке равны 1
    print(True)