from tkinter import *

root = Tk()
root.title("Програма-редактор графічних файлів")
canvasWidth = 700
canvasHeight = 500


def create_g_el(event):
    x1 = event.x - 10
    y1 = event.y
    x2 = event.x + 10
    y2 = event.y

    w.create_line(x1, y1, x2, y2, width=2)
    w.create_line(x2, y1 - 5, x2, y2 + 5, width=2)
    w.create_line(x2 + 5, y1 - 10, x2 + 5, y2 + 10, width=2)
    w.create_line(x2 + 5, y1, x2 + 25, y2, width=2)


def create_c_el(event):
    x1 = event.x - 10
    y1 = event.y
    x2 = event.x + 10
    y2 = event.y

    w.create_line(x1, y1, x2, y2, width=2)
    w.create_line(x2, y1 - 7, x2, y2 + 7, width=2)
    w.create_line(x2 + 5, y1 - 7, x2 + 5, y2 + 7, width=2)
    w.create_line(x2 + 5, y1, x2 + 25, y2, width=2)


def create_z(event):
    x1 = event.x - 10
    y1 = event.y
    x2 = event.x + 10
    y2 = event.y

    w.create_line(x1, y1, x2, y2, width=2)
    w.create_rectangle(x2 + 30, y1 - 5, x2, y1 + 5, width=2)
    w.create_line(x2 + 30, y1, x2 + 50, y2, width=2)
    w.create_line(x2, y1, x2 + 30, y2, width=2)


def create_r(event):
    x1 = event.x - 10
    y1 = event.y
    x2 = event.x + 10
    y2 = event.y

    w.create_line(x1, y1, x2, y2, width=2)
    w.create_rectangle(x2 + 30, y1 - 5, x2, y1 + 5, width=2)
    w.create_line(x2 + 30, y1, x2 + 50, y2, width=2)


def create_n_el(event):
    x1 = event.x - 10
    y1 = event.y
    x2 = event.x + 10
    y2 = event.y

    w.create_line(x1, y1, x2, y2, width=2)
    w.create_rectangle(x2 + 32, y1 - 5, x2, y1 + 5, width=2)
    w.create_line(x2 + 8, y1 - 5, x2 + 8, y1 + 5, width=2)
    w.create_line(x2 + 16, y1 - 5, x2 + 16, y1 + 5, width=2)
    w.create_line(x2 + 24, y1 - 5, x2 + 24, y1 + 5, width=2)
    w.create_line(x2 + 32, y1, x2 + 50, y2, width=2)


w = Canvas(root,
           width=canvasWidth,
           height=canvasHeight,
           bg="white")

w.grid(row=2,
       column=0, columnspan=7,
       padx=5, pady=5,
       sticky=E + W + S + N)

w.columnconfigure(6, weight=1)
w.rowconfigure(2, weight=1)

btn1 = Button(text="Гальванічний елемент", width=20,
              command=lambda: w.bind('<Button-1>', create_g_el))

btn2 = Button(text="Конденсатор", width=10,
              command=lambda: w.bind('<Button-1>', create_c_el))

btn3 = Button(text="Запобіжник", width=10,
              command=lambda: w.bind('<Button-1>', create_z))

btn4 = Button(text="Резистор", width=10,
              command=lambda: w.bind('<Button-1>', create_r))

btn5 = Button(text="Нагрівальний елемент", width=20,
              command=lambda: w.bind('<Button-1>', create_n_el))

btn6 = Button(text="Видалити все", width=10,
              command=lambda: w.delete("all"))

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=0, column=3)
btn5.grid(row=0, column=4)
btn6.grid(row=1, column=0)

root.mainloop()
