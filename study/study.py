# _*_ coding : utf_8 _*_
# @Time : 2024/3/3 9:26
# @Author : 田霄汉
# @File : study
# @Project : reliangApiTest

import math

# print(678%100%10)
# print(678%100//10)
# print(678//100)

# # 高手写的代码
# def function_02(profit):
#     bonus = 0
#     if profit <= 10:
#         bonus = profit*0.1
#     elif 10 < profit <= 20:
#         bonus = (profit-10)*0.075 + function_02(10)
#     elif 20 < profit <= 40:
#         bonus = (profit-20)*0.05 + function_02(20)
#     elif 40 < profit <= 60:
#         bonus = (profit-40)*0.03 + function_02(40)
#     elif 60 < profit <= 100:
#         bonus = (profit-60)*0.015 + function_02(60)
#     else:
#         bonus = (profit-100)*0.01 + function_02(100)
#     return bonus
#
# bonus = function_02(90)
# print(bonus)

# print(math.sqrt(169))

# t = []
# for m in range(168):
#     for n in range(m):
#         if m**2 - n**2 == 168: # n**2=x+100，x+100+168也就是m**2是一个完全平方数；
#             x = n**2 - 100 # n**2就是x+100，也是一个完全平方数
#             t.append(x)
# print('符合条件的整数有：',t )

# print([i for i in range(0, 2)])

# while 1:
#     try:
#         x = int(input("plz input x: "))
#         y = int(input("plz input y: "))
#         z = int(input("plz input z: "))
#         list1 = [x, y, z]
#         print(sorted(list1))
#         break
#     except:
#         print("请输入整数")

# initial_list = [1, 3, 2]
# def dayu2(num):
#     num = int(num)
#     if num <= 2:
#         pass
#     else:
#         return num
#
# print(initial_list.sort(key=dayu2))

# initial_list = [1, 3, 2, 1, 2]
# print(sorted(initial_list))


def mysort1d(a):  #采用冒泡排序
    an=len(a)
    for i in range(an)[::-1]:
        for j in range(i):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
    return a

a=[int(i) for i in input('please input 3 number: ').split( )]
print(mysort1d(a))
