from sympy import simplify


intro = '''
РОЗРАХУНКОВО-ГРАФІЧНА РОБОТА з дисципліни: «Програмування» 1-й семестр
На тему: "Програма згладжування функції(поліноми)"
Варіант 10
Керівник: Олефір О.С.
Виконала студентка групи КМ-02: Касьяненко Анна'''

desc = '''
Програма створена для обчислення полінома, для цього необхідно ввести дискретний набір довільних точок.
Був використаний метод інтерполяційного полінома Лагранжа.'''

print(intro)

print(desc)



def build_poly(x_array, y_array):
    res = []
    for i in range(0, len(x_array)):
        numerator = "*".join(list(filter(lambda l: l != "", list(map(lambda k: f"(x - {x_array[k]})" if k != i else "", range(0, len(x_array)))))))
        denominator = "*".join(list(filter(lambda l: l != "", list(map(lambda k: f"({x_array[i]} - {x_array[k]})" if k != i else "", range(0, len(x_array)))))))
        res.append(f"{y_array[i]} * ({numerator}) / ({denominator})")
    return simplify("+".join(res))

while True:
    try:
        el_X = list(map(lambda x: float(x), input("Введіть значення аргументів для X через пробіл: ").split()))
        el_Y = list(map(lambda x: float(x), input("Введіть значення аргументів для Y через пробіл: ").split()))
    except ValueError:
        print("Ви ввели не числове значення, спробуйте ще раз: ")
        continue
    if len(el_X) != len(el_Y):
        print("Кількість координат X має співпадати з кількістю координат Y, спробуйте ще раз: ")
        continue

    
    poly = build_poly(el_X, el_Y)
    print("Шуканий поліном: " ,poly)  

    if input("Хочете спробувати ще раз? [y] щоб продовжити, чи будь-який інший символ для завершення програми: ") != 'y':
        break
