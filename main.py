# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-04-'

import re

from window import ApplicationTop, ApplicationExpand
from window import ApplicationBottom, ApplicationBottomDown
from window import Window

if __name__ == '__main__':
	root = Window()		# TK()

	app_top = ApplicationTop(master=root)	# Frame Top
	app_expand = ApplicationExpand(master=root)	# Frame Expand
	app_bottom = ApplicationBottom(master=root)	# Frame Bottom
	app_bottom_down = ApplicationBottomDown(master=root)	# Frame Bottom Down

	root.mainloop()
