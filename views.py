# -*- coding: utf-8 -*-


import tkinter as tk

from models import considers_time_difference


def tick():
	label2.after(200, tick)
	label2['text'] = considers_time_difference()

def window_deleted():
	print('Окно закрыто')
	root.quit()


root = tk.Tk()

root.title('Таймер')  # название окна
root.geometry('500x400+300+200')  # размерм окна
root.protocol('WM_DELETE_WINDOW', window_deleted)  # обработчик закрытия окна

label = tk.Label(root, text='До окончания рабочего дня:', font='arial 16')
label.place(x=100, y=10)
label2 = tk.Label(font='sans 72')  # размер шрифта таймера
label2.place(x=50, y=50)

label2.after_idle(tick)
root.mainloop()
