# -*- coding: utf-8 -*-


__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-21'

from datetime import datetime


def considers_time_difference():
	'''
	Разница во времени
	:return: class 'datetime.timedelta' или str
	'''
	set_time_now = datetime.now()
	# TODO: тестовый вариант для отладки
	if set_time_now.weekday() == 4:
		_time = set_time_now.replace(hour=16, minute=45, second=0)
	else:
		_time = set_time_now.replace(hour=18, minute=0, second=0)

	res = _time - set_time_now
	if _time < set_time_now:
		res = 'The End!!!'
	return res


def name_day():
	'''
	Return name day
	:return: str
	'''
	set_data = datetime.now()
	_day = {0: 'Понедельник', 1: 'Вторник', 2: 'Среда',
	        3: 'Четврег', 4: 'Пятница', 5: 'Суббота', 6: 'Воскресенье'}
	for k in _day.keys():
		if set_data.weekday() == k:
			return _day[k]


if __name__ == '__main__':
	print(name_day())
