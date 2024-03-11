# _*_ coding : utf_8 _*_
# @Time : 2024/3/4 17:17
# @Author : 田霄汉
# @File : 求日期的天数
# @Project : reliangApiTest

"""
输入某年某月某日，判断这一天是这一年的第几天？
"""

# 自己写的
def get_num():

    year = int(input("请输入年份："))
    mouth = int(input("请输入月份："))
    day = int(input("请输入日份："))

    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    sum = 0

    if (year % 400 == 0 or year % 100 != 0 and year % 4 == 0) and mouth > 2:
        for i in range(mouth-1):
            sum += days_list[i]
        sum = sum + 1

    else:
        for i in range(mouth-1):
            if mouth == 1:
                sum = 0
            else:
                sum += days_list[i]

    result_day = sum + day
    print(result_day)

# 优化后的
def get_days():

    year = int(input("请输入年份："))
    mouth = int(input("请输入月份："))
    day = int(input("请输入日份："))

    days_list = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if year%400==0 or year%4==0 and year%100!=0:
        days_list[1] = 29
    else:
        pass

    sum = 0
    for i in range(mouth-1):
        sum += days_list[i]
        print(i)
    result_day = sum + day
    print(result_day)

get_days()