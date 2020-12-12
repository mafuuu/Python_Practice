# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:58:59 2020

@author: serap
"""

#7 Exercises

#1.例外発生をつくる
a = 10
b = 0#1
try:
    print(a / b)
except ZeroDivisionError:
    msg = "例外発生"
    print(msg)
    
#2.msg1に例外2　msg2に例外処理終了
try:
    array = [3,2,0,1]
    a = 10
    i = "ABC"#1
    b = array[i]
except ZeroDivisionError:
    msg1 = "例外１"
    print(msg1)
except TypeError:#2
    msg1 = "例外2"
    print(msg1)
finally:#3
    msg2 = "例外処理終了"
    print(msg2)
    
#3.msg1 例外発生　msg2 例外処理終了
try:
    a = 1
    b = "ABC"
    ans = a + b
except TypeError:#1
    msg1 = "例外発生"
    print(msg1)
else:
    msg1 = "例外発生せず"
    print(msg1)
finally:#2
    msg2 = "例外処理終了"
    print(msg2)