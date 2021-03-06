# Імпорт модулів math та re
from math import *
import re


# Функція для перевірки дійсних чисел
def check_float(text):
    pattern = "^[+-]?([0-9]*[.])?[0-9]+$"
    input_text = input(text)
    while not re.match(pattern, input_text):
        input_text = input("Ви ввели значення, яке не задвольняє умові задачі, будь ласка введіть дійсне значення:")
    return float(input_text)


# Функція для перевірки цілих додатних чисел, відмінних від нуля
def check_int(text):
    input_text = input(text)
    pattern = "^[0-9]+$"
    while not re.match(pattern, input_text):
        input_text = input("Неправильний формат, введенне значення повинно бути цілим додатним числом, відмінним від нуля: ")
    return int(input_text)


# Функція для обрахування значення введеної у рядок підінтегральної функції, яка інтерпрeтується, як код
def func(x):
    return eval(f)


# Виведення загальної інформації
print("РОЗРАХУНКОВО-ГРАФІЧНА РОБОТА".center(110), "\n")
print("з дисципліни: «Програмування-1»".center(110))
print("на тему: «Програма обчислення визначених інтегралів (формули трапецій)»".center(110))
print("Варіант-VII".center(110), "\n\n\n\n")
print("Виконав: Задорожний Богдан Юрійович".rjust(110))
print("Група КМ-02, факультет ФПМ".rjust(110), "\n")
print("Керівник: Олефір О.С.".rjust(110), "\n")
print("ІНФОРМАЦІЙНЕ ПОВІДОМЛЕННЯ".center(110), "\n")
print("Ця прогрмама дозволяє обчислити визначений інтеграл за допомогою формули трапеції. \n"
      "Програма пропонує користувачеві ввести підінтегральну функцію, межі інтегрування та кількість частин, на які \n"
      "розбиваються межі інтегрування. Далі програма обчислює площу визначеного інтеграла та виводить його на екран.")
print("ВИМОГИ ДО ФОРМАТУ ВВЕДЕННЯ ДАНИХ".center(110), "\n")
print("Для коректної роботи програми підінтегральну функцію потрібно вводити за допоммогою синтаксису мови Python.")
print("Приклади використання деяких математичних операцій:\n"
      "  - fabs(X) - модуль X\n"
      "  - factorial(X) - факторіал числа X\n"
      "  - exp(X) - експонента в степені X\n"
      "  - log(X, Y) - логарифм X за основою Y. Якщо Y не вказан, обраховується натуральний логарифм\n"
      "  - pow(X, Y) - X в степені Y\n"
      "  - sqrt(X) - квадратний корінь з X\n"
      "  - cos(X) - косинус X (X вказується у радіанах)\n"
      "  - sin(X) - синус X (X вказується у радіанах)\n"
      "  - tan(X) - тангенс X (X вказується у радіанах)\n"
      "  - pi - число pi\n"
      "  - e - експонента")
print("-" * 25)
r = ""
# Цикл для повторного запуску програми
while not r == "N":
    # Цикл для введення меж інтегрування, підінтегральної функції, кількості частин розбиття та перевірка їх валідності
    while True:
        try:
            a = check_float("Введіть нижню межу інтегрування: ")
            b = check_float("Введіть верхню межу інтегрування: ")
            f = input("Введіть підінтегральну функцію: ")
            for i in range(int(a), int(b) + 1):
                func(i)
            n = check_int("Введіть кількість частин, на які розбиваються межі інтегрування: ")
            if n == 0:
                raise ValueError
            break
        except ValueError:
            print("Не можливо обрахувати площу підінтегральної функції, будь ласка перевірте правильність введення \n"
                  "меж інтегрування, підінтегральної функції та кількості частин розбиття.\n", "-" * 25)
        except NameError:
            print("Ви ввели значення, яке не задвольняє умові задачі, будь ласка перевірте правильність введення \n"
                  "функції та спробуйте ввести фунцію ще раз.\n", "-" * 25)
        except ZeroDivisionError:
            print("Введена функція містить ділення на нуль. Спробуйте ввести іншу функцію або змінити межі інтегрування.\n",
                  "-" * 25)
        except SyntaxError:
            print("Невірно введено підінтегральну функцію. Спробуйте ввести функцію знову.\n", "-" * 25)
    # Обрахування площі підінтегральної функції
    h = (b - a) / n
    S = 0
    x = a + h
    while x < b:
        F = func(x)
        S = S + F
        x = x + h
    Fa = func(a)
    Fb = func(b)
    S = (h/2) * (Fa + Fb + 2 * S)
    # Виведення результату обчислень
    print("-" * 25, "\nПлоща визначеного інтегралу(результат обчислення):", S)
    print("-" * 25)
    r = ""
    # Запит на повторний запуск програми
    while not (r == "Y") | (r == "N"):
        r = input("Ви маєте бажання спробувати ще раз? (Y/N): ")
        if r == "Y":
            print("-" * 25, "\nЗапускаэмо програму.")
        elif r == "N":
            print("-" * 25, "\nДякую за користування. Гарного дня!")
        else:
            print("Введене вами значення не є коректним, спробуйте ще раз.")
