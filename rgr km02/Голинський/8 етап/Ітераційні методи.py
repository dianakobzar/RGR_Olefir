import math


def fun(x):
    return (2 - 0.4 * x ** 2) ** 0.5 + math.cos(x)


x1 = float(input("Введіть приближене значення Х="))
e = float(input("Введіть точність e="))
a = float(input("a="))
b = float(input("b="))
a = abs((fun(a + 0.0001) - fun(a)) / 0.0001)
b = abs((fun(b + 0.0001) - fun(b)) / 0.0001)
q = max(a, b)
q = (1 - q) / q
iters = 0
x0 = x1
x1 = fun(x0)
while abs(x1 - x0) <= abs(q * e):
    iters += 1
    x0 = x1
    x1 = fun(x0)
print('Точне значення кореня:', 2.0926)
print('Обчислення значення кореня:', x1)
print('число ітерацій:', iters)