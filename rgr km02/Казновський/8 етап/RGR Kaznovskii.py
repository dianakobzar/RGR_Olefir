# Виведення початкової інформації
print("ПРОГРАМА ЧИСЕЛЬНОГО ДИФЕРЕНЦІЮВАННЯ (обчислення другої похідної \nРозробник: Казновський Антон\n")

print("Формат даних\n"+"-"*13,
    "\nПрограма обчислює значення другої похідної деякої функції, заданої таблично\n" +
    "(з однаковою різницею між сусідніми аргументами), у заданій користувачем точці.\n" +
    "Для цього програма спочатку запитує різницю аргументів, далі перший з них і значення функції для\n" +
    "кожного наступного аргументу (користувач може ввести необмежену кількість залежних змінних).\n" +
    "Абсциса досліджуваної точки має бути одним із аргументів досліджуваної функції, для якого\n" +
    "користувач задав значення.\n")

print('Значення мають вводитися у форматі цілого, або десяткового дробового числа через символ ".".\n' +
    'В інших випадках програма виведе помилку та запитає повторне введення.\n' +
    'Після кінця введення всіх значень функцій відправте слово "готово".\n' +
    'Кінцевий результат виводиться у вигляді числа, округленого до 4 знаку після коми.\n')

print("ПОРАДА\n" + "-"*16 + "\nДля найбільш точного результату слід задати перший аргумент таким, в якому\n"+
    "шукатиметься друга похідна та ввести як мінімум 5 значення функції.\n")
print("Виконання\n" + "-"*16)


# Імпорт додаткових бібліотек
import numpy as np
from sympy import diff, symbols


# Задання допоміжних функцій
def table(lst):
    '''Функція створення матриці значень дельта у'''
    k = len(lst[0])
    for i in lst:
        if len(i) != k:
            for d in range((k - len(i))):
                i.append(float(0))
    delta_y_table = np.array(lst).transpose()
    return delta_y_table


def lisst(list_of_values, length):
    '''Функція створення списку для таблиці значень y'''
    delta_y_list = []
    for d in range(length-1):
        delta_y_list.append([])
    for k in range(1, length):
        delta_y_list[0].append(list_of_values[k] - list_of_values[k-1])
    for i in range(1, length):
        for k in range(len(delta_y_list[i-1]) - 1):
            delta_y_list[i].append(delta_y_list[i-1][k+1] - delta_y_list[i-1][k])
    delta_y_list.insert(0, list_of_values)
    return delta_y_list


def polinome(delta_y_list, i):
    '''Функція для створення поліному'''
    a, q = symbols('a, q')
    summa = 0
    a=1
    for j in range(len(list_of_arguments)):
        summa += a*(deltas_ys[i, j])
        a *= q - j
        a /= 1 + j
    return summa
    

def pohidna(summa):
    '''Функція, що рахує другу похідну у даній точці для отриманого поліному'''
    q = symbols('q')
    h = (delta)**(-1)
    second_pohidna = (h**2)*diff(summa, q, 2)
    param = h*(find_x-list_of_arguments[0])
    result = second_pohidna.evalf(subs={q:param})
    return result


def count_measuring_error(length, deltas_ys, i):
    '''Функція для розрахунку похибки обчислень'''
    h = (delta)**(-1)
    return (-1)**(length-i-2)*h/(length-i)*deltas_ys[i, length-i-1]


#==========================


# Реалізація програми
while True:
    #Введення різниці між х
    while True:
        try:
            delta = float(input("Введіть різницю між сусідніми х: "))
            break
        except ValueError:
            print("Будь-ласка, введіть ціле або дійсне число у правильному форматі.")
    print()

    #Введення першого значення х
    while True:
        try:
            x = float(input("Введіть перший х: "))
            break
        except ValueError:
            print("Будь-ласка, введіть ціле або дійсне число у правильному форматі.")
    print()

    #Введення та формування списку значень
    list_of_arguments = []
    list_of_values = []
    while True:
        n = input("Введіть у для х="+str(x)+ " : ")
        if n == "готово":
            if len(list_of_values) != 0:
                break
            else:
                print("Введіть хочаб одне значення у")
        else:
            try:
                list_of_values.append(float(n))
                list_of_arguments.append(x)
                x += delta
            except ValueError:
                print("Будь-ласка, введіть ціле або дійсне число у правильному форматі.")
    print()

    #Введення значення х, в якому шукатиметься друга похідна
    while True:
        try:
            find_x = float(input("Введіть х точки, для якої шукатиметься значення другої похідної: "))
            if find_x in list_of_arguments:
                break
            else:
                print("Будь-ласка, введіть значення, для якого ви задали ординату.")
        except ValueError:
            print("Будь-ласка, введіть ціле або дійсне число у правильному форматі.")
    print()

    #Опрацювання даних
    length = len(list_of_values)
    i = list_of_arguments.index(find_x)
    deltas_ys = table(lisst(list_of_values, length))

    znachennya = pohidna(polinome(deltas_ys, i))
    znachennya = round(float(znachennya), 4)
    pohibka = round(count_measuring_error(length, deltas_ys, i), 4)


    #Виведення результату
    print("Значення другої похідної у даній точці становить:", znachennya)
    print("Значення похибки становить:", pohibka)

    #Запит на повторний запуск програми
    cont = input("\nХочете перезапустити програму? Напишіть + або -\n")
    while True:
        if (cont != "-") and (cont != "+"):
            cont = input("Неправильний формат введення. Напишіть + або -\n")
        else: break
    if cont == "-":
        break