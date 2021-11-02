from math import exp, sin, cos, pi
from sympy import symbols, diff, lambdify

print("Ви можете ввести свою функцію, або обрати із поданих прикладів")
def operation():
    print("Приклади функцій: \n1) x**3 + x - 5 \n2) x**2 - exp(-x) \n3) x**4 - 3*(x**2) + 75*x - 10000 \n4) (x - 5)**2 + sin(x - 5) \n5) sin(x) - x*cos(x)")
    f = input("\nВведіть функцію:") 
    x = symbols('x')
    while type:
        a = input("Введіть число, з якого почнеться пошук кореня:")
        n = input("Введіть наближення (eпсілон): 10^-")
        k = input("Кількість знаків після коми у відповіді:")
        try:
            a = float(a)
            n = int(n)
            k = int(k)
        except ValueError:
            print("Ви повинні ввести цілi числa")
        else:
            break
        
    e = 1/(10**n)
        
    def dif(f):
        f1 = f
        f2 = diff(f, x)
        return f1, f2

    def fun(dif):
        f1, f2 = dif
        func1 = lambdify(x, f1)
        func2 = lambdify(x, f2)
        return func1, func2

    def method(fun, x, e):
        while True:
            func1, func2 = fun
            f1 = func1(x)
            f2 = func2(x)
            y = x - (f1/f2)
            if abs(y - x) > e:
                x = y
            else:
                break
        return round(y, k)

    print("\nВідповідь:", method(fun(dif(f)), a, e))
    
def replay():
    while True:
        e = input("\nБажаєте продовжити? [y/n]:")
        if e == "y":
            operation()
        elif e == "n":
            print("Програма завершена")
            break
        else:
            print("Потрібно ввести 'y' або 'n'!")

operation()
replay()