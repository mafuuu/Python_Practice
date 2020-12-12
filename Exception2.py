# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 15:15:54 2020

@author: serap
"""

#else と　finally

#例外が起きずにelseで抜ける処理の例
#exceptの処理を通っていない
try:
    a = 2
    b = 2
    print(a / b)
except ZeroDivisionError:
    print("例外が発生")
else:
    print("例外発生せずに終了")
    
#例外発生の関係なしに絶対に通る処理
#例外を発生させながら、finallyに抜ける処理
try:
    a = 2
    b = 0
    print(a / b)
except ZeroDivisionError:
    print("例外発生")
finally:
    print("最後に実行")    
    

#例外を発生させず、finallyに抜ける処理
try:
    a = 2
    b = 2
    print(a / b)
except ZeroDivisionError:
    print("例外発生")
finally:
    print("最後に実行")    

#elseとfinallyを一緒に入れることも可能
try:
    a = 2
    b = 2
    print(a / b)
except ZeroDivisionError:
    print("例外発生")
else:
    print("例外の発生がなく終了")
finally:
    print("最後に実行")
