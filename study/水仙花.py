# _*_ coding : utf_8 _*_
# @Time : 2024/3/3 9:22
# @Author : 田霄汉
# @File : 水仙花
# @Project : reliangApiTest

"""
三位数的百位，十位，个位的立方进行求和，结果还是这个三位数，即水仙花数字
"""

def daffodil():
    result_list = []
    for i in range(100, 1000):
        digit = i%100%10
        tens_digit = i%100//10
        hundreds_digit = i//100
        if digit**3 + tens_digit**3 + hundreds_digit**3 == i:
            result_list.append(i)
    print(result_list)
    
daffodil()