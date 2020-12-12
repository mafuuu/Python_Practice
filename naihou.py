# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:49:24 2020

@author: serap
"""

#内包表記
#規則的なものを簡単に作りたいとき！
#iの中にrange10が入っている
lst1 = [i for i in range(10)]
print(lst1)
#lst1のrangeに3をかけた
lst2 = [i * 3 for i in lst1]
print(lst2)
#lst1のrangeに1を足した
lst3 = [i + 1 for i in lst1]
print(lst3)

#少し応用
#forの中にifを入れられる
lst2 = [i for i in range(10) if i % 2 == 1]
print(lst2) 
#lst1のrangeに1を足した
lst3 = [i for i in range(10) if i % 2 == 0]
print(lst3)