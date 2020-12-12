# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:01:32 2020

@author: serap
"""

#二重の内容表記
lst1 = [[i,j] for i in [1,2,3] for j in [3,1,4]]
print(lst1)

#改行
print()

#ifを使った二重表記
lst2 = [[i,j] for i in [1,2,3] for j in[3,1,4] if i != j]
print(lst2)

#改行
print()

#文字列と数値のリスト
lst3 = [[i,j]for i in ["a","b"] for j in [1,2]]
print(lst3)

#改行
print()

#rangeを使った二重表記
lst4 = [[i,j]for i in range(2) for j in range(3)]
print(lst4)