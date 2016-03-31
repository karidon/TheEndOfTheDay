# -*- coding: utf-8 -*-
from __future__ import unicode_literals

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-26'

import sys

from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter", 're']}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(name="TheEndOfTheDay",
	  version="0.1.2",
	  description="War so its like cops",
	  options={"build_exe": build_exe_options},
	  executables=[Executable(script="main.py", base=base)])

