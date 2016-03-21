# -*- coding: utf-8 -*-



'''

- Выбираем разницу во временя и делаем обратный отчет
'''



from datetime import date, datetime
import time

def considers_time_difference():
	'''
	Разница во времени
	:return: class 'datetime.timedelta' или str
	'''
	set_time_now = datetime.now()
	# TODO: тестовый вариант для отладки
	if set_time_now.weekday() == 1:
		_time = set_time_now.replace(hour=16, minute=45, second=0)
	else:
		_time = set_time_now.replace(hour=23, minute=0, second=0)

	res = _time - set_time_now
	if _time < set_time_now:
		res = 'The End!!!'
	return res







if __name__ == '__main__':
	print(considers_time_difference())

