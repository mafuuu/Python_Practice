# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:21:20 2020

@author: serap
"""
#12/12

#シーケンス応用

#0から10まで二つずつスキップ
for i in range(0,10,2):
    print(i)
#9から0まで-2ずつスキップ
for i in range(9,0,-2):
    print(i)

#listで同じことができる
#文字列でも同じことが可能
lst = [0,1,2,3,4,5,6,7,8,9]
s = "0123456789"

#全部表示
print(lst)
#lst[0:10:2]
print(lst[0:10:2])
#lst[9:0:-2]
print(lst[9:0:-2])

#応用
#rangeからリストを作る
lst = list(range(0,10))
print(lst)

# 文字列からリストを作る
s = "abxdefghij"
print(s)
lst = list(s)
print(lst)



