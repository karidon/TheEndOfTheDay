# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""Основное окно обработки времени"""

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-27'

import re
from datetime import datetime


class Timer(object):
	"""Таймер"""
	_data_now_static = datetime.now()  # статическое время

	def considers_time_difference(self):
		'''
		Разница во времени
		:return: class 'datetime.timedelta' или str
		'''
		FRIDAY = 4  # пятница
		SATURDAY = 5  # суббота
		SUNDAY = 6  # воскресенье

		self.data_now = datetime.now()  # время в даный момент

		if self.data_now.weekday() == FRIDAY:
			time = self.data_now.replace(hour=16, minute=45, second=0)
		elif self.data_now.weekday() == SATURDAY or self.data_now.weekday() == SUNDAY:
			res = 'Weekend!'
			return res
		else:
			time = self.data_now.replace(hour=18, minute=0, second=0)

		res = time - self.data_now	# остаток времени

		if time < self.data_now:
			res = 'The End!'
		return res

	def name_day(self):
		'''
		Return name day
		:return: str
		'''
		_day = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда',
				3: 'Четврег', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}
		for k in _day.keys():
			if Timer._data_now_static.weekday() == k:
				return _day[k]

	def get_data(self):
		'''
		Return data
		:return: class 'datetime.date'
		'''
		year = Timer._data_now_static.year
		month = Timer._data_now_static.month
		day = Timer._data_now_static.day

		zero = 0  # добовляет ноль перед цифрами месяца
		if month > 10:
			zero = ''

		return '{0}-{1}{2}-{3}'.format(day, zero, month, year)


if __name__ == '__main__':
	timer_test = Timer()
	print(timer_test.considers_time_difference())
	print(timer_test.name_day())
	print(timer_test.get_data())
	print('Ok')
