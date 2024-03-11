# _*_ coding : utf_8 _*_
# @Time : 2024/3/4 16:10
# @Author : 田霄汉
# @File : 完全平方数
# @Project : reliangApiTest

import math

def perfect_square():
    t = []
    for m in range(168):
        for n in range(m):
            if m ** 2 - n ** 2 == 168:  # n**2=x+100，x+100+168也就是m**2是一个完全平方数；
                x = n ** 2 - 100  # n**2就是x+100，也是一个完全平方数
                t.append(x)
    print('符合条件的整数有：', t)

perfect_square()