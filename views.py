# -*- coding: utf-8 -*-


# TODO 1: отдельно тесты написать
# TODO 2: подправить окно
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

	label = tk.Label(root, text='До окончания рабочего дня:', font='arial 16')
	label.place(x=100, y=10)

	label2 = tk.Label(root, font='sans 72')  # размер шрифта таймера
	label2.place(x=50, y=50)
	label2.after_idle(tick)

	label3 = tk.Label(root, font='arial 16')
	label3.place(x=200, y=200)
	label3.after_idle(display_day)

	label4 = tk.Label(root, font='arial 14')
	label4.place(x=200, y=300)
	label4.after_idle(display_data)

	root.mainloop()
