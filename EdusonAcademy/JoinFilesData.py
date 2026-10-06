file1 = open('../Test/test3.txt', 'r', encoding='utf8')
file1 = file1.readline()
file2 = open('../Test/test4.txt', 'a', encoding='utf8')
file2.write('\n' + file1)