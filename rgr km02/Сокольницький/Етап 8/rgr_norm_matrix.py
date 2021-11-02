from math import sqrt
import sys
print('\t\t\t\t\tРозрахункова робота на тему: Обчислення норм матриць\n\n')
print('\t\t\t\t\tВиконав студент групи КМ-02 Сокольницький Максим')
print('\n\n\n\n\n\n\n\n\t\t\t\t\t\t\tВаріант 19\n\n\n\n\n')
x = int(input('Введіть кількість стовпців матриці\n'))
y = int(input('Введіть кількість рядків матриці\n'))

matrix = []
row_numb_test = 0
element_index_input = 0
y = range(y)
x = range(x)
for i in y:
    matrix.append([])
    for j in x:
        matrix[i].append(int(input('Введіть %d елемент, %d рядка матриці: '%(j + 1, i + 1))))


norm_1 = 0
norm_2 = 0
norm_3 = []
norm_4 = []
row_numb = 0
element_index = 0
for row in matrix:
    for elem in row:
        norm_1 = norm_1 + abs(elem)
        norm_2 = norm_2 + elem ** 2
        if row_numb == 0:
            norm_3.append(abs(elem))
        else:
            norm_3[row.index(elem)] = norm_3[row.index(elem)] + abs(elem)

    element_index = 0
    row_numb = row_numb + 1

print('l1-норма', norm_1)
print('Евклідова норма:', round(sqrt(norm_2), 3))
print('Стовпцева норма', max(norm_3))

while True:
    ext = input('Вийти? Введіть так:\n').lower()
    if ext == 'так':
        sys.exit(0)
    else:
        print('Введіть так або ні!\n')
        continue
