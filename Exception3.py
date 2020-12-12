# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:26:46 2020

@author: serap
"""

#例外クラス

#0の割り算
try:
    a = 2
    b = 0
    print(a / b)
except ZeroDivisionError as e:
    #例外メッセージの表示
    print(e)
    #例外クラスの名前を表示
    print(type(e))
    
#違う方の演算
try:
    a = 2
    b = "ABC"
    print(a + b)
except TypeError as e:
    #例外メッセージの表示
    print(e)
    #例外クラスの名前を表示
    print(type(e))
    
#例外がわからない場合の書き方
try:
    a = 2
    b = 0
    print(a / b)
except BaseException as e:
    #例外メッセージの表示
    print(e)
    #例外クラスの名前を表示
    print(type(e))

    
