# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:17:36 2020

@author: serap
"""

#他の内包表記
#tupleの内包表記
tup = tuple(i for i in range(10))
print(tup)

#集合
#重複されたものはなくなる
s = {i for i in [1,1,2,3,4,5,5,6]}
print(s)

#辞書
dic = dict(zip(["one","two","three"],[1,2,3]))
print(dic)
