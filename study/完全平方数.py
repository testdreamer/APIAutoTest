# _*_ coding : utf_8 _*_
# @Time : 2024/3/4 16:10
# @Author : 田霄汉
# @File : 完全平方数
# @Project : reliangApiTest

import math

def perfect_square01():
    t = []
    for m in range(168):
        for n in range(m):
            if m ** 2 - n ** 2 == 168:  # n**2=x+100是完全平方数，m**2=x+100+168也是完全平方数；
                x = n ** 2 - 100  # n**2就是x+100，也是一个完全平方数
                t.append(x)
    print('符合条件的整数有：', t)



def perfect_square02():
    """
    完全平方数：一个整数的平方就是完全平方数，例如：1*1=1,2*2=4,3*3=9...
    在0~100000的范围内取值，数字加上100是完全平方数，数字加上268也是完全平方数，打印出满足条件的数字
    """

    # 先在0-10万中遍历取值
    for i in range(100000):
        # 将i+100和i+268进行开平方根，再转换成整形
        x = int(math.sqrt(i+100))
        y = int(math.sqrt(i+268))
        # 如果转换成的整形正好是i+100和i+268
        if x**2 == i+100 and y**2 == i+268:
            # 则可以认定i符合要求
            print(i)

if __name__ == '__main__':
    perfect_square01()