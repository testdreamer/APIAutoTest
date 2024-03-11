# _*_ coding : utf_8 _*_
# @Time : 2024/3/4 10:45
# @Author : 田霄汉
# @File : 金字塔
# @Project : reliangApiTest

"""
输入金字塔的层数level，打印一个由“*”组成的金字塔，金字塔的层数就是level
"""

# 之前的方法
def pyramid():

    level = int(input("请输入金字塔的层数："))
    for current_level in range(1, level+1):
        for i in range(1, level-current_level+1):
            print(end=" ")
        for j in range(1, 2*current_level):
            print(end="*")
        print()

# 新方法
def new_pyramid():

    level = int(input("请输入金字塔的层数："))
    for current_level in range(1, level+1):
        print(" "*(level-current_level), "*"*(2*current_level-1), end="")
        print()

new_pyramid()