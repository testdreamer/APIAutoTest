# _*_ coding : utf_8 _*_
# @Time : 2024/3/3 10:06
# @Author : 田霄汉
# @File : 不重复数字
# @Project : reliangApiTest

"""
有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
"""

# 自己写的
def function_01():

    result_list = []
    n = 0
    for i in range(1, 5):
        for j in range(1, 5):
            for k in range(1, 5):
                if i != j and j != k and i != k:
                    result_list.append(i*100+j*10+k)
                    n += 1
    print(result_list)
    print(n)

# 高手写的
def function_02():

    result_list = []
    num = 0
    for i in range(1, 5):
        for j in range(1, 5):
            if i == j:
                continue
            for k in range(1, 5):
                if i == k or j == k:
                    continue
                result_list.append(i*100+j*10+k)
                num += 1
    print(num)
    print(result_list)

# 利用列表的remove()方法
def function_03():

    result_list = []
    num = 0
    initial_list = [1, 2, 3, 4]
    for i in initial_list:
        new_list = initial_list.copy()
        new_list.remove(i)
        for j in new_list:
            new_new_list = new_list.copy()
            new_new_list.remove(j)
            for k in new_new_list:
                result_list.append(i*100+j*10+k)
                num += 1
    print(num)
    print(result_list)