print("\n\n\n","\t\t\t\t\t    ", "РОЗРАХУНКОВО-ГРАФІЧНА РОБОТА", sep = "")
print("\t\t\t\t\t\t  ", "З дисципліни:\n\t\t\t\t\t    'Програмування' 1-ий семестр.", sep = "")
print("\n\n\n","\t\t\t\t       ", "Тема:'Програма чисельного диференціювання'", sep = "")
print("\n\n\n","\t\t\t", "Виконав","\t\t\t\t\t\t\t\t", "Чорний Д.С.", sep = "")
print("\n\n\n","\t\t\t\t\t\t\t", "2020","\n\n\n" , sep = "")

print("ІНФОРМАЦІЙНЕ ПОВІДОМЛЕННЯ ТА ВИМОГИ ДО ДАНИХ:",
    "",
    "Ця програма дозволяє обчислити приблизне значення\nпохідної по таблично заданим даним або аналітичній формулі.\nДля обчислення програма інтерполює табличні значення за\nдопомогою поліному Ньотона.",
    "",
    "ВИМОГИ ДО ДАНИХ:",
    "",
    "Програма обчислює поліном на основі рівновіддалених точок.\nТому, для табличного введення функції потрібно буде обрати крок,\nта місце розташування першого значення в стопвчику х-ів.\nУсі інші значення х програма обрахує з зазначеним вами кроком.\nПереконайтеся, що задана вами функція може бути диференційована\nу точці диференціювання. У разі вводу аналітичної формули вам буде\nзапропоновано ввести функцію за допомогою синтаксису мови Python.\nДалі, буде обрахована таблиця значень з кроком 0.1. Якщо ви бажаєте\nобрати інший крок, або функція не визначена в місцях з кроком 0.1\nвід точки диференціювання рекомендованим є ввести функцію\nвже в табличному вигляді. Точка має знаходитися в проміжку від\nнайпершого табличного х і до останнього.",
    sep="\n")


import math
import itertools

def ask_yes_or_no(firstmsg="", inputmsg=""):
    print(firstmsg)
    yes_or_not = True
    while yes_or_not:
        y_o_n = input(inputmsg)
        if (y_o_n == "Так") or (y_o_n == "так"):
            yes_or_not = False
            return True
        elif (y_o_n == "Ні") or (y_o_n == "ні"):
            yes_or_not = False
            return False
        else:
            print("Ви ввели некоректне значення. Введіть 'так' або 'ні'.")

def ask_num(msg, type_="float"):
    num_stay = True
    while num_stay:
        try:
            if type_ == "int":
                num = int(input(msg+"\n"))
                num_stay = False
                return num
            else:
                num = float(input(msg+"\n"))
                num_stay = False
                return num
        except ValueError:
            print("Ви ввели непідходяще значення. Введіть значення числом.")
def calculate(num, list_, h):
    is_in_table = False
    for i in list_:
        if num == i[0]:
            place = list_.index(i)
            is_in_table = True
        elif i == list_[0] and num < i[0]:
            return ("Х не входить у проміжок заданих таблично даних." , "Х не входить у проміжок заданих таблично даних.")
        elif i == list_[-1] and num > i[0]:
            return ("Х не входить у проміжок заданих таблично даних." , "Х не входить у проміжок заданих таблично даних.")
        elif (list_[list_.index(i)-1][0] < num) and (num < i[0]):
            if (num-list_[list_.index(i)-1][0] > i[0]-num) and (i != list_[-1]):
                place = list_.index(i)
            else:
                place = list_.index(i)-1
    dif_table = [[]]
    for i in range(len(list_)-1):
        dif_table[0].append(list_[i+1][1]-list_[i][1])

    while len(dif_table[-1])!=1:
        dif_table.append([])
        for i in range(len(dif_table[-2])-1):
            dif_table[-1].append(dif_table[-2][i+1]-dif_table[-2][i])

    if is_in_table:
        res = 0
        for i in range(math.ceil((len(list_)-place)/2)):
            res += ((-1)**i)*((dif_table[i][place])/(i+1)) 
        res = res/h
        error = (((-1)**(len(list_)-place-3))*dif_table[len(list_)-place-2][place])/(h*(len(list_)-place-1))

    else:
        res = 0
        q = (num-list_[place][1])/h
        for i in range(math.ceil((len(list_)-place)/2)):
            if i == 0:
                res += dif_table[i][place]
            elif i == 1:
                res += ((2*q-1)/2)*dif_table[i][place]
            else:
                jopa = 1
                for j in range(1, i+1):
                    jopa =jopa*(q-j)

                jui = 0
                coefs = list(itertools.combinations(range(1, i+1), i-1))
                for j in range(i):
                    jack = q
                    for c in coefs[j]:
                        jack=jack*(q-c)
                    jui = jui+jack
                res += ((jopa + jui)/(math.factorial(i+1)))*dif_table[i][place]
        res = res/h

        jopa = 1
        for j in range(1, (len(list_)-place-1)):
            jopa =jopa*(q-j)

        jui = 0
        coefs = list(itertools.combinations(range(1, (len(list_)-place+1)), (len(list_)-place-1)))
        for j in range((len(list_)-place-1)):
            jack = q
            for c in coefs[j-1]:
                jack=jack*(q-c)
            jui = jui+jack
        error = (((-1)**(len(list_)-place-3))*dif_table[len(list_)-place-2][place])/(h*(len(list_)-place-1))

    return (round(res, 6), round(error, 6))

stay = True
while stay:   
    # питання введення функції таблично, чи аналітично
    if ask_yes_or_no("Бажаєте ввести функцію таблично?", "Напишіть 'так' для табличного введення, або 'ні' для аналітичного.\n"):
        point_func_stay = True
        der_stay = False
        point_stay = True
    else:
        point_func_stay = False
        der_func_stay = True
        der_stay = True




    while point_func_stay:
        #Введення функції таблично
        if point_stay:
            print("\nВведіть крок табличних значень, перший 'х' з таблиці та кожен 'у' відповідно. \nДля зупинки запису введіть пустий рядок.")
            numbers = []
            h = ask_num("Введіть крок табличних значень.")
            counter = 0
            x = ask_num("Введіть перший 'х'. (Усі інші будуть обраховані у відповідності з кроком.)")
        while point_stay:
            inp = input("Введіть 'у'. Для зупинки запису введіть пустий рядок.\n")
            if inp == "":
                if len(numbers)==0:
                    print("Ви не ввели ні одного y. Спробуйте ще.")
                else:
                    point_stay = False
            else:    
                try:
                    numbers.append(tuple([x+(h*counter), float(inp)]))
                    counter +=1
                except ValueError:
                    counter +=1
                    print("Значення в некоректному форматі. Введіть число.")
        
        #Введення точки диференціювання
        num = ask_num("\nВведіть точку для диференціювання.")
        
        #Обрахунок значення
        result = calculate(num, numbers, h)
        print("\nЗначення похідної у точці:", result[0])
        print("Обрахована помилка:", result[1])
        
        ##Спробувати ще раз з цією функцією?
        if not ask_yes_or_no("\nБажаєте спробувати ще раз з цією функцією?", "Напишіть 'так', або 'ні'.\n"):
            point_func_stay = False
        else:
            point_stay = False
    

    while der_func_stay:
        #Ввід точки для диференціювання
        num = ask_num("\nВведіть точку для диференціювання.")

        #Введення аналітично
        while der_stay:
            func_ = input("Введіть функцію від x за допомогою синтаксису мови Python.\nЗвертайтеся до модулю math через 'math.'\n")
            try:
                x = num
                eval(func_)
                def func(x):
                    return eval(func_)
                der_stay = False
            except:
                print("\nНеправильно введена функція або функція не визначена у точці диференціювання. Спробуйте ще.")


        #Переведення фунціїї в табличну форму
        iterations = 14
        numbers = []
        for i in range(math.floor(iterations/2)):
            try:                
                numbers.append(tuple([num-math.floor(iterations/2)+(i/10), func(num-math.floor(iterations/2)+(i/10))]))
            except:
                pass
        for i in range(math.ceil(iterations/2)):
            try:
                numbers.append(tuple([num+(i/10), func(num+(i/10))]))
            except:
                pass
        #Обрахунок значення похідної від поліному
        result = calculate(num, numbers, 0.1)
        print("\nЗначення похідної у точці:", result[0])
        print("Обрахована помилка:", result[1])

        #Спробувати ще раз з цією функцією?
        if not ask_yes_or_no("\nБажаєте спробувати ще раз з цією функцією?", "Напишіть 'так', або 'ні'.\n"):
            der_func_stay = False
        else:
            der_stay = False



    #Запустити програму ще раз?
    if not ask_yes_or_no("\nБажаєте спробувати ще раз з іншою функцією?", "Напишіть 'так', або 'ні'.\n"):
            stay = False