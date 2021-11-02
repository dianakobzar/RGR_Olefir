print("\n\n\n","\t\t\t\t\t    ", "РОЗРАХУНКОВО-ГРАФІЧНА РОБОТА", sep = "")
print("\n","\t\t\t\t\t  ", "З дисципліни:\t   'Програмування-1.' ", sep = "")
print("\n","\t\t\t\t       ", "Тема:'Програма обробки таблично заданих функцій'", sep = "")
print("\n","\t\t\t\t\t", "Виконала","\t\t\t", "Ковальчук Д.Ю", sep = "")
print("\n","\t\t\t\t\t\t\t", "2020","\n\n\n" , sep = "")

print("ІНФОРМАЦІЙНЕ ПОВІДОМЛЕННЯ ТА ВИМОГИ ДО ДАНИХ:",
    "",
    "Ця програма обробляє таблично\nЗадані функції.Введені користувачем координати програма подає у вигляді таблиці,а коли користувач хоче завершити програму,то будуються графіки функцій,\n"
    "",
    "ВИМОГИ ДО ДАНИХ:",
    "",
    "За приклад візьмемо функції двох експонентів.")

print("Перший приклад функція - y = e**x.Для якої вам потрібно ввести координати точок,щоб програма могла задати їх таблично.")

from prettytable import PrettyTable
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy import interpolate





while True:
    while True:
            try:
                x1 =float(input("Введіть значення x1:"))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")
    while True:
            try:
                y1 = float(input("Введіть значення y1: "))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")
    while True:
            try:
                x2 = float(input("Введіть значення x2:"))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")
    while True:
            try:
                y2 = float(input("Введіть значення y2:"))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")
    while True:
            try:
                x3 = float(input("Введіть значення x3: "))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")
    while True:
            try:
                y3 = float(input("Введіть значення y3: "))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")

    while True: 
        p = PrettyTable(["X","Y"])
        p.add_row([x1,y1])
        p.add_row([x2,y2])
        p.add_row([x3,y3])
        print (p.get_string())
        break

    print("Введіть координати ще одного графіка.Наприклад, y = e**(-x)")
    while True:
            try:
                a1 = float(input("Введіть значення x1:"))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")
    while True:
            try:
                b1 = float(input("Введіть значення y1: "))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")
    while True:
            try:
                a2 = float(input("Введіть значення x2:"))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")
    while True:
            try:
                b2 = float(input("Введіть значення y2:"))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")
    while True:
            try:
                a3 = float(input("Введіть значення x3: "))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")
    while True:
            try:
                b3 = float(input("Введіть значення y3: "))
                break
            except ValueError:
                print("Введено невірно. Введіть значення числом!!!")

    while True: 
        j = PrettyTable(["X","Y"])
        j.add_row([a1,b1])
        j.add_row([a2,b2])
        j.add_row([a3,b3])
        print (j.get_string())
        break

    answ = input("Хочете перезапустити програму? Напишіть yes або no:")
    while True:
        if (answ != "yes") and (answ != "no"):
            answ = input("Неправильний формат введення. Напишіть yes або no:")
        elif answ == "no":
            y = lambda x: np.exp(x)
            y1 = lambda x: np.exp(-x)


            fig = plt.subplots()

            x = np.linspace(-3, 3,100)

            plt.plot(x, y(x))
            plt.plot(x,y1(x))

            plt.show()
            break
