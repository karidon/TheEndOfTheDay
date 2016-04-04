# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""Главное окно виджетов"""

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-04-04'

import tkinter as tk
import re

from timer import Timer


class Window(tk.Tk):
	"""Отображает Главное окно"""
	def window_close(self):
		'''
		Обрабатывает заыкытие окна
		:return:
		'''
		print('Окно закрыто')
		self.destroy()
		self.quit()

	def __init__(self, master=None):
		super().__init__(master)
		self.title('Таймер')  # название окна

		# TODO 1: Сделать на весь экран
		# TODO 2: Весь экран должен сворачиваться по клику мышки
		# TODO 3: При бездействия разварачиваться
		try:
			self.iconbitmap('images/icon.ico')	# иконка в title баре
		except tk.TclError:
			pass

		self.geometry('500x400+300+200')  # размерм окна
		self.protocol('WM_DELETE_WINDOW', self.window_close)  # обработчик закрытия окна

class ApplicationTop(tk.Frame):
	"""Top Frame and Label Top"""

	def __init__(self, master=None):
		super().__init__(master)
		self.pack(side='top')
		self.createWidgets()

	def createWidgets(self):
		''' Label Top '''
		self.label = tk.Label(self)
		self.label['font'] = 'arial 16'
		self.label['fg'] = 'black'
		self.label['text'] = 'До окончания рабочего дня:'
		self.label.pack(side='bottom')


class ApplicationExpand(tk.Frame):
	"""Farme Expand and Label Expand"""

	def __init__(self, master=None):
		super().__init__(master)
		self.pack(expand=True)
		self.createWidgets()

	def createWidgets(self):
		''' Label Expand '''
		self.label = tk.Label(self)
		self.label['font'] = 'arial 72'
		self.label['fg'] = '#8ffe09'
		self.label.pack()
		# self.tmp = None   # для смайла
		self.label.after_idle(self.tick)

	def tick(self):
		'''
		Returns time functions
		:return: str
		'''
		self.tmp = self.label.after(200, self.tick)
		self.label['text'] = Timer.considers_time_difference(self)

	def smile_view(self):
		'''Return smile'''
		# TODO 4: Нужно вернуть смайл заместо текста
		pass


class ApplicationBottom(tk.Frame):
	"""Frame Bottom and Label Bottom"""

	def __init__(self, master=None):
		super().__init__(master)
		self.pack(side='bottom')
		self.createWidgets()

	def createWidgets(self):
		'''Label Bottom'''
		self.label = tk.Label(self)
		self.label['font'] = 'arial 14'
		self.label['fg'] = 'black'
		self.label.pack()
		self.label.after_idle(self.display_day)

	def display_day(self):
		'''
		Shows the name of the day.
		:return: str
		'''
		self.label['text'] = Timer.name_day(self)


class ApplicationBottomDown(tk.Frame):
	"""Form Bottom Down and Label Bottom Down"""

	def __init__(self, master=None):
		super().__init__(master)
		self.pack(side='bottom')
		self.createWidgets()

	def createWidgets(self):
		'''Label Down'''
		self.label = tk.Label(self)
		self.label['font'] = 'arial 14'
		self.label['fg'] = 'black'
		self.label.pack()
		self.label.after_idle(self.display_data)

	def display_data(self):
		'''
		Shows the data.
		:return: str
		'''
		self.label['text'] = Timer.get_data(self)


if __name__ == '__main__':
	root = Window()
	#	root = tk.Tk()
	#	root.title('Таймер')  # название окна
	#	root.geometry('500x400+300+200')  # размерм окна
	#	root.protocol('WM_DELETE_WINDOW',
	#				  window_close)  # обработчик закрытия окна

	app_top = ApplicationTop(master=root)
	app_expand = ApplicationExpand(master=root)
	app_bottom = ApplicationBottom(master=root)
	app_bottom_down = ApplicationBottomDown(master=root)

	root.mainloop()
