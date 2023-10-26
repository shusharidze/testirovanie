from tkinter import *
from tkinter.messagebox import showerror, showinfo
import sys

wnd = Tk()  # Создание окна
wnd.title('Проверка треугольника')
wnd.geometry('500x250')
wnd.config(bg='#eee')
wnd.resizable(False, False)

def close(event):
    """Функция выхода из программы кнопкой Escape"""
    sys.exit()

def btn_click(event=None):
    """Функция обработки введенных данных"""
    global a, b, c
    a = entry_a.get()
    b = entry_b.get()
    c = entry_c.get()

    if (len(a) == 0 or len(b) == 0 or len(c) == 0):
        showerror(title='Ошибка', message='Задайте все стороны треугольника!\n')
    elif not (a.isdigit() and b.isdigit() and c.isdigit()):
        showerror(title='Ошибка', message='Задайте стороны треугольника целыми числами!')
    elif int(a) == 0 or int(b) == 0 or int(c) == 0:
        showerror(title='Ошибка', message='Сторона треугольника не может быть равной нулю!')
    elif (int(a) + int(b) <= int(c)) or (int(c) + int(b) <= int(a)) or (int(a) + int(c) <= int(b)):
        showerror(title='Ошибка', message='Такой треугольник невозможен!\n'
                  'Сумма любых двух сторон треугольника должна быть больше третьей стороны.')
    elif int(a) == int(b) == int(c):
        showinfo(title='Сообщение', message='Треугольник равносторонний!')
    elif (int(a) == int(b)) or (int(a) == int(c)) or (int(c) == int(b)):
        showinfo(title='Сообщение', message='Треугольник равнобедренный!')
    else:
        showinfo(title='Сообщение', message='Треугольник разносторонний!')


Label(
    wnd,
    text='Введите стороны треугольника.',
    font=('sans-serif', 25),
    bg='#eee'
).grid(row=0, columnspan=4, sticky='EW', padx=10, pady=(0,20))


frame = LabelFrame(
    wnd,
    text=' Стороны треугольника ',
    font=('sans-serif', 12),
    bg='#fff',
    padx=10,
    pady=10,
)
frame.grid(row=1, columnspan=4, padx=18, pady=(0, 10))


entry_a = Entry(
    frame,
    bg='#fff',
    font=('sans-serif', 16),
    width=8,
    justify=CENTER
)
entry_a.grid(row=0, column=0, sticky=W, pady=10, padx=20)

entry_b = Entry(
    frame,
    bg='#fff',
    font=('sans-serif', 16),
    width=8,
    justify=CENTER
)
entry_b.grid(row=0, column=1, sticky=W, pady=10, padx=20)

entry_c = Entry(
    frame,
    bg='#fff',
    font=('sans-serif', 16),
    width=8,
    justify=CENTER
)
entry_c.grid(row=0, column=2, sticky=W, pady=10, padx=20)

btn = Button(
    frame,
    text='Рассчитать',
    command=btn_click,
    font=('sans-serif', 14),
    padx=20,
    pady=2,
    bg='#eef'
)
btn.grid(row=1, columnspan=3, padx=10, pady=10)

wnd.bind('<Return>', btn_click)
wnd.bind('<Escape>', close)

wnd.mainloop()
