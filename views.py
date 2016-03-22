# -*- coding: utf-8 -*-


# TODO 1: отдельно тесты написать
# TODO 3: подумать как можно запускать при вкл компа
# TODO 4: упоковать в установщик

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-21'

import tkinter as tk

from timer import Timer


def tick():
	'''
	Returns time functions
	:return: str
	'''
	label2.after(200, tick)
	label2['text'] = timer.considers_time_difference()


def display_day():
	'''
	Shows the name of the day.
	:return: str
	'''
	label3['text'] = timer.name_day()


def display_data():
	'''
	Shows the data.
	:return: str
	'''
	label4['text'] = timer.get_data()


def window_deleted():
	'''
	Close window.
	:return:
	'''
	print('Окно закрыто')
	root.quit()


if __name__ == '__main__':
	timer = Timer()

	root = tk.Tk()

	root.title('Таймер')  # название окна
	root.geometry('500x400+300+200')  # размерм окна
	root.protocol('WM_DELETE_WINDOW',
	              window_deleted)  # обработчик закрытия окна

	fra1 = tk.Frame(root, width=500, height=500)
	fra1.pack(side='top')

	fra2 = tk.Frame(root, width=500, height=500)
	fra2.pack(expand=True)

	fra3 = tk.Frame(root, width=500, height=500)
	fra3.pack(side='bottom')

	fra4 = tk.Frame(root, width=500, height=500)
	fra4.pack(side='bottom')

	label = tk.Label(fra1, text='До окончания рабочего дня:', font='arial 16')
	label.pack()

	label2 = tk.Label(fra2, font='sans 72',
	                  fg='#8ffe09')  # размер шрифта таймера
	label2.pack()
	label2.after_idle(tick)

	label3 = tk.Label(fra3, font='arial 14')
	label3.pack()
	label3.after_idle(display_day)

	label4 = tk.Label(fra4, font='arial 14')
	label4.pack()
	label4.after_idle(display_data)

	root.mainloop()
