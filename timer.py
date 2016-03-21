# -*- coding: utf-8 -*-


__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-21'

from datetime import datetime


class Timer(object):
	"""Таймер"""

	def set_data(self):
		'''
		Создаем дату
		:return: class 'datetime.timedelta'
		'''
		self._data_now = datetime.now()
		return self._data_now

	def considers_time_difference(self):
		'''
		Разница во времени
		:return: class 'datetime.timedelta' или str
		'''
		time_now = self.set_data()
		if time_now.weekday() == 4:
			_time = time_now.replace(hour=16, minute=45, second=0)
		else:
			_time = time_now.replace(hour=18, minute=0, second=0)

		res = _time - time_now
		if _time < time_now:
			res = 'The End!!!'
		return res

	def name_day(self):
		'''
		Return name day
		:return: str
		'''
		data_now = self._data_now
		_day = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда',
		        3: 'Четврег', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}
		for k in _day.keys():
			if data_now.weekday() == k:
				return _day[k]

	def get_data(self):
		'''
		Return data
		:return: class 'datetime.date'
		'''
		return self._data_now.date()


if __name__ == '__main__':
	timer_test = Timer()
	print(timer_test.considers_time_difference())
	print(timer_test.name_day())
	print(timer_test.get_data())
	print('Ok')
