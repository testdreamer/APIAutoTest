# _*_ coding : utf_8 _*_
# @Time : 2024/3/4 19:28
# @Author : 田霄汉
# @File : 三个数排序
# @Project : reliangApiTest

def sorted_num():
    while 1:
        try:
            x = int(input("plz input x:"))
            y = int(input("plz input y:"))
            z = int(input("plz input z:"))
            initial_list = [x, y, z]
            print(sorted(initial_list))
            break
        except:
            print("请输入整数！")

sorted_num()