# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:32:36 2020

@author: serap
"""

#Handling multiple exceptions
#(複数の例外の処理)

#IndexError
try:
    a = 10
    b = [1,2,3]
    #割り算をする
    i = 0
    while i < 4:
        print("{}/{}=".format(a,b[i]),end="")
        print(a / b[i])
        i = i + 1
except IndexError:
    print("配列の範囲をこえました")
except ZeroDivisionError:
    print("ゼロでの割り算はできません")
    
#ZeroDivisionError
try:
    a = 10
    b = [1,2,0]
    #割り算をする
    i = 0
    while i < 4:
        print("{}/{}=".format(a,b[i]),end="")
        print(a / b[i])
        i = i + 1
except IndexError:
    print("配列の範囲をこえました")
except ZeroDivisionError:
    print("ゼロでの割り算はできません")
    
#exceptをひとまとめにしたもの
try:
    a = 10
    b = [1,2,0]
    #割り算をする
    i = 0
    while i < 4:
        print("{}/{}=".format(a,b[i]),end="")
        print(a / b[i])
        i = i + 1
except (IndexError,ZeroDivisionError) as e:
    print(e)
    
#一番楽なもの
#どの例外でエラーが起きてるかわからないときに全部をひっかけられるようにする
try:
    a = 10
    b = [1,2,3]
    i = 0
    while i < 4:
        print("{} / {} = ".format(a,b[i]),end= "")
        print(a / b[i])
        i = i + 1
except BaseException as e:
    print(e)
    print(type(e))