# -*- coding: utf-8 -*-

__author__ = 'karidon'
__email__ = 'Genek_x@mail.ru'
__date__ = '2016-03-26'

import sys
from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need fine tuning.
build_exe_options = {"packages": ["os"], "excludes": ["tkinter"]}

# GUI applications require a different base on Windows (the default is for a
# console application).
base = None
if sys.platform == "win32":
	base = "Win32GUI"

setup(name="TheEndOfTheDay",
	  version="0.1",
	  description="Return time",
	  options={"build_exe": build_exe_options},
	  executables=[Executable("main.py", base=base)])
