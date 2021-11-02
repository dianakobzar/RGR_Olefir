print("\n\n\n","\t\t\t\t\t\t", "Розрахунково-графічна  робота", sep = "")
print("\t\t\t\t\t\t", "Варіант №22", sep = "")
print("\n\n\n","\t\t\t\t", "Тема:'Програма інтерполювання таблично заданої функції'", sep = "")
print("\n\n\n","\t\t\t", "Виконала","\t\t\t\t\t\t\t\t", "Харчук О.О.", sep = "")
import numpy as np
import matplotlib.pyplot as plt
while True:
    try:
        n=int(input('Введіть к-сть значень x або y (їх кількість однакова), що задаються:'))
    except:
        print ('Помилка! К-сть може бути задан лише цілим додатним значенням.')
    array = input('Введіть значення x через пробіл (формулювання першого рядка таблиці зі значеннями змінної x):').split()
    x=np.array(array, dtype=float)
    array = input('Введіть значення y через пробіл (формулювання другого рядка таблиці зі значеннями змінної y):').split()
    y=np.array(array, dtype=float)
    def lagranz(x,y,t):
        z=0
        for j in range(len(y)):
            p1=1; p2=1
            for i in range(len(x)):
                if i==j:
                    p1=p1*1; p2=p2*1   
                else: 
                    p1=p1*(t-x[i])
                    p2=p2*(x[j]-x[i])
            z=z+y[j]*p1/p2
        return z
    xnew=np.linspace(np.min(x),np.max(x),100)
    ynew=[lagranz(x,y,i) for i in xnew]
    plt.plot(x,y,'o',xnew,ynew)
    plt.grid(True)
    plt.show()
    print('Бажаєте ввести інші значення? Введіть "так" або "ні".')
    while True:
        ans = input()
        if ans == "так" or ans == "ні":
            break
        else:
            print('Недопустима відповідь. Введіть так або ні.\n')
    if ans == "ні":
        print('До зустрічі!')
        break
