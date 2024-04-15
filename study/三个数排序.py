# _*_ coding : utf_8 _*_
# @Time : 2024/3/4 19:28
# @Author : 田霄汉
# @File : 三个数排序
# @Project : reliangApiTest

# 使用sorted()对列表进行排序
try:
    x = int(input("plz input x:"))
    y = int(input("plz input y:"))
    z = int(input("plz input z:"))
    initial_list = [x, y, z]
    print(sorted(initial_list))
except:
    print("请输入整数！")

# 使用冒泡排序方式进行排序
try:
    # x = int(input("plz input x:"))
    # y = int(input("plz input y:"))
    # z = int(input("plz input z:"))
    initial_list = [1, 3, 2]
    for i in range(len(initial_list), 0, -1):
        for j in range(0, i-1):
            if initial_list[j] > initial_list[j+1]:
                initial_list[j], initial_list[j+1] = initial_list[j+1], initial_list[j]
            else:
                pass
    print(initial_list)
except:
    print("请输入整数！")