import numpy as np
import itertools


def isnumb(x):
    while type(x) != float:
        try:
            x = float(x)
        except ValueError:
            print("Помилка. Введене значення не є числом")
            x = input("Введіть числове значення елемента (дробові числа вводяться з крапкою):")
    return float(x)


def input_check(x, y):
    input_data = input(x)
    if not input_data.isdigit():
        return input_check("Ви ввели не додатнє число. Введіть існуючий номер:", y)
    if 1 <= int(input_data) <= y:
        return int(input_data)
    return input_check("Помилка. Введіть доступне значення:", y)


def permut_list(dim):
    """
    Функція створює список перестановок чисел від 0 до розмірність-1, котрі потім використовуються для обчислення
    визначника матриці довільної розмірності.
    """
    ind_list = []
    for i in range(0, dim):
        ind_list.append(i)
    perm = list(itertools.permutations(ind_list, dim))
    return perm


def determ(matrix, perm_list, dimension):
    """
    Ця функція обчислює елементи для майбутнього додавання, обчислюючи добутки потрібних елементів:
    їх перші індекси рівні 1, 2, ... n, а другі іденксами є перестановками чисел від 1 до n.
    Функція одразу визначає знак потрібного елементу: якщо відповідна йому перестановка є парною,
    елемент береться із знаком +, у протилежному випадку-зі знаком -. На останньому кроці функція додає
    отримані елементи. Результат виконання функції-визначник матриці, число.
    """
    res = []
    a = []
    for i in range(0, len(perm_list)):
        a.append(0)
        for j in range(0, dimension):
            for k in range(0, dimension):
                if j < k and perm_list[i][j] > perm_list[i][k]:
                    a[i] += 1
        if a[i] % 2 == 1:
            a[i] = -1
        else:
            a[i] = 1
        res.append(1)
        for j in range(0, dimension):
            res[i] *= matrix[j][perm_list[i][j]]
        res[i] = res[i] * a[i]
    s = 0
    for i in range(0, len(res)):
        s += res[i]
    return s


def matrix_maker(m, n):
    matrix = np.zeros((m, n))
    # Створення матриці нулів даного розміру для майбутнього заповнення елементами
    for i in range(0, m):
        for j in range(0, n):
            matrix[i][j] = isnumb(input("Введіть елемент а" + str(i + 1) + str(j + 1) + ":"))
    return matrix


def rectang():
    while True:
        m = input("Введіть кількість рядків матриці:")
        while type(m) != int:
            try:
                m = int(m)
                if m <= 0:
                    m = input("Помилка:вказане вам число не більше 0, тому не може бути розмірністю матриці."
                              "Введіть кількість рядків матриці:")
            except ValueError:
                m = input("Помилка: введене вами значення не є цілим числом. Введіть розмірність матриці:")
        n = input("Введіть кількість стовпців матриці:")
        while type(n) != int:
            try:
                n = int(n)
                if n <= 0:
                    n = input("Помилка:вказане вам число не більше 0, тому не може бути розмірністю матриці."
                              "Введіть кількість стовпців матриці:")
            except ValueError:
                n = input("Помилка: введене вами значення не є цілим числом. Введіть розмірність матриці:")
        rect_mat = matrix_maker(m, n)
        print("Ваша матриця:")
        print(rect_mat)
        while True:
            k = input_check("Введіть кількість рядків та стовпців, для яких потрібно знайти мінор:", min(m, n))

            count1 = 0
            rows = []
            while count1 < k:
                numb = input_check("Введіть номер рядка, що входить до мінору:", m)
                while numb in rows:
                    print("Цей рядок уже входить до мінору. Будь ласка, оберіть інший.")
                    numb = input_check("Введіть номер рядка, що входить до мінору:", m)
                rows.append(numb)
                count1 += 1
            rows.sort()

            count2 = 0
            columns = []
            while count2 < k:
                numb = input_check("Введіть номер стовця, що входить до мінору:", n)
                while numb in columns:
                    print("Цей стовпчик уже входить до мінору. Будь ласка, оберіть інший стовпчик.")
                    numb = input_check("Введіть номер стовпця, що входить до мінору:", n)
                columns.append(numb)
                count2 += 1
            columns.sort()

            minor_mat = np.zeros((k, k))
            for i in range(0, k):
                for j in range(0, k):
                    minor_mat[i][j] = rect_mat[rows[i] - 1][columns[j] - 1]
            print("Отримана матриця:")
            print(minor_mat)
            print("Ваш мінор:" + str(determ(minor_mat, permut_list(k), k)))
            if input('Знайти інший мінор цієї матриці(для підтвердження введіть "Так")?:') != "Так":
                break

        if input('Знайти мінор іншої матриці(для підтвердження введіть "Так")?:') != "Так":
            break


def square():
    while True:
        dim = input("Введіть розмірність матриці:")
        while type(dim) != int:
            try:
                dim = int(dim)
                if dim <= 0:
                    dim = input("Помилка:вказане вам число не більше 0, тому не може бути розмірністю матриці."
                                "Введіть розмірність матриці:")
            except ValueError:
                dim = input("Помилка: введене вами значення не є цілим числом. Введіть розмірність матриці:")
        while True:
            matrix = matrix_maker(dim, dim)
            # Цикл заповнює матрицю елементами, котрі вказує користувач
            print("Ваша матриця:")
            print(matrix)
            minor_matrix = np.zeros((dim, dim))
            # Створення матриці нулів даного розміру для заповнення мінорами
            for i in range(0, dim):
                unrowed_matrix = np.delete(matrix, i, 0)
                for j in range(0, dim):
                    new_matrix = np.delete(unrowed_matrix, j, 1)
                    minor_matrix[i][j] = determ(new_matrix, permut_list(dim - 1), dim - 1)
            # Спершу цикли видаляють рядок і стовпець матриці, у якому стояв елемент, для якого обчислюється мінор.
            # Наступним кроком за допомогою функції обчислюється визначник отрмианої матриці.
            ask = input("Отримати матрицю мінорів (введіть 'Матриця') чи мінор елемента(введіть 'Елемент')?:")
            # Цикл дає змогу визначити, в якому виді подати результати
            while True:
                if ask == "Матриця":
                    print("Матриця мінорів:")
                    print(minor_matrix)
                    break
                elif ask == "Елемент":
                    while True:
                        r = input_check("Введіть номер рядка:", dim)
                        c = input_check("Введіть номер стовпця:", dim)
                        print("Мінор елемента а" + str(r) + str(c) + " = " + str(minor_matrix[r - 1][c - 1]))
                        if input("Обрати інший елемент (введіть 'Так')? ") != "Так":
                            break
                    break
                else:
                    print("Помилка: хибне введення.")
                    ask = input("Отримати матрицю мінорів (введіть 'Матриця') чи мінор елемента(введіть 'Елемент')?:")
            if input("Повторити виконання для того ж розміру матриці (для підтвердження введіть 'Так')?:") != 'Так':
                break
        if input("Знайти мінор елемента іншої матриці (для підтвердження введіть 'Так')?:") != 'Так':
            break


def prog():
    decide = input('Оберіть тип мінора ("Матриця" або "Елемент"):')
    while decide not in ['Матриця', 'Елемент']:
        print("Хибне введення. Будь ласка, оберіть один із варіантів")
        decide = input('Оберіть тип мінора ("Матриця" або "Елемент"):')
    if decide == 'Матриця':
        rectang()
    elif decide == 'Елемент':
        square()


print("\n\n\n", "\t\t\t\t\t\t", "Розрахунково-графічна робота", sep="")
print("\n", "\t\t\t\t\t", " З дисципліни: «Програмування» 1-й семестр", sep="")
print("\n\n", "\t\t\t\t", "На тему: «Програма обчислення мінорів заданої матриці»", sep="")
print("\n\n\n\n\n", "\t\t\t", "Виконав", "\t\t\t\t\t\t\t\t", "Студент групи КМ-02", sep="")
print("\n", "\t\t\t", "\t\t\t\t\t\t\t\t\t", "Фірман Д.Б.", sep="")
print("\n\n\n", "\t\t\t\t\t\t\t\t\t\t\t\t\t", "2020", "\n\n\n", sep="")

while True:
    prog()
    if input("Бажаєте повторно скористатись програмою (для підтвердження введіть 'Так')?:") != 'Так':
        break
