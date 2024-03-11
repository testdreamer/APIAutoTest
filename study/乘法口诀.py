# _*_ coding : utf_8 _*_
# @Time : 2024/3/3 9:22
# @Author : 田霄汉
# @File : 乘法口诀
# @Project : reliangApiTest


# 左上乘法表
def left_up_multiplication():

    for i in range(1, 10):
        for j in range(1, i+1):
            print(j, "*", i, "=", i*j, "\t", end="")
        print()

# 右上乘法表
def right_up_multiplication():
    for i in range(1, 10):
        for k in range(1, 10-i):
            print(end="            ")
        for j in range(1, i+1):
            print(j, "*", i, "=", j*i, "\t", end="")
        print("\n")


# 左下乘法口诀
def left_down_multiplication():
    for i in range(1, 10):
        for j in range(1, 11-i):
            print(j, "*", i, "=", i*j, "\t", end="")
        print()


# 右下乘法口诀
def right_down_multiplication():
    for i in range(1, 10):
        for k in range(1, 10-i):
            print(end="            ")
        for j in range(1, i+1):
            print(j, "*", i, "=", i*j, "\t", end="")
        print()