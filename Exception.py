# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:02:01 2020

@author: serap
"""

#例外が起きる例
#0での割り算
a = 2
b = 0
#print(a / b)

#リストの範囲外
a = [1,2,3,4]
print(a[0])
#print(a[100])

#異なる方の演算
a = 2
b = "ABC"
#print(a + b)

#例外処理
#例外が発生した際にプログラムを終了させない処理
#try ~ except

#例外処理の例
#0での割り算
try:
    a = 2
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("0での割り算")
    
#リストの範囲外
try:
    a = [1,2,3,4]
    print(a[100])
except IndexError:
    print("リスト範囲外")
    
#異なる方の演算
try:
    a = 2
    b = "ABC"
    print(a + b)
except TypeError:
    print("異なる方の演算")                  


