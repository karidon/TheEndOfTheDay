# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""Главное окно виджетов"""

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-04-04'

import tkinter as tk
from sys import platform
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
		try:
			self.iconbitmap('images/icon.ico')  # иконка в title баре
		except tk.TclError:  # Если нет иконки
			pass

		if platform.startswith('linux'):
			self.geometry('500x400+300+200')  # размерм окна
		else:
			self.state('zoomed')
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
		self.label['font'] = 'arial 18'
		self.label['fg'] = 'black'
		self.label['text'] = 'До окончания рабочего дня:'
		self.label.pack()


class ApplicationExpand(tk.Frame):
	"""Farme Expand and Label Expand"""

	def __init__(self, master=None):
		super().__init__(master)
		self.pack(expand=True)
		self.createWidgets()

	def createWidgets(self, font='arial 72'):
		''' Label Expand '''
		self.label = tk.Label(self)
		self.label['font'] = font
		self.label['fg'] = '#8ffe09'
		self.label.pack()
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


class ApplicationDownClock(tk.Frame):
	"""Top Frame and Label Top"""

	def __init__(self, master=None):
		super().__init__(master)
		self.pack(side='top')
		self.createWidgets()

	def createWidgets(self):
		''' Label Bottom '''
		self.label = tk.Label(self)
		self.label['font'] = 'sans 48'
		self.label['fg'] = 'black'
		self.label.pack()
		self.label.after_idle(self.clock)

	def clock(self):
		'''
		Return clock
		'''
		self.tmp = self.label.after(200, self.clock)
		self.label['text'] = Timer.set_clock(self)


class ApplicationBottom(tk.Frame):
	"""Frame Bottom and Label Bottom"""

	def __init__(self, master=None):
		super().__init__(master)
		self.pack(side='bottom')
		self.createWidgets()

	def createWidgets(self):
		'''Label Bottom'''
		self.label = tk.Label(self)
		self.label['font'] = 'arial 18'
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
		self.label['font'] = 'arial 18'
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
	app_top = ApplicationTop(master=root)
	app_expand = ApplicationExpand(master=root)
	app_top_right = ApplicationDownClock(master=root)
	app_bottom = ApplicationBottom(master=root)
	app_bottom_down = ApplicationBottomDown(master=root)

	root.mainloop()
