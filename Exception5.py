# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:49:14 2020

@author: serap
"""

#pass Ignore exceptions
#(例外の無視とパス)

#例外がおきれも無視する
try:
    a = 2
    b = 0
    print(a / b)
except ZeroDivisionError:
    pass

#whileで使うpass
i = 0
while i < 3:
    print(i)
    i = i + 1
else:
    pass