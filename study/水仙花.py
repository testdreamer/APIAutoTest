# _*_ coding : utf_8 _*_
# @Time : 2024/3/3 9:22
# @Author : 田霄汉
# @File : 水仙花
# @Project : reliangApiTest

"""
水仙花数: n位数的各个数位的n次方之和等于这个n位数
举个例子，3位数153，1**3+5**3+3**3 = 1+125+27 = 153
"""

def get_num(num):

    """
    params: 输入num，获取num的各个位数值
    """

    # 获取num的位数
    lenNum = len(str(num))
    return [num//10**(lenNum-n)%10 for n in range(lenNum, 0, -1)]



def narcissistic_num(n):

    """
    params: n为水仙花数的位数，n为大于1的正整数
    """

    # 用来接收水仙花数
    getList = []

    for i in range(10**(n-1), 10**n):
        # 调用get_num()方法获取i的各个数位值，从个位开始，返回的是list格式
        resultList = get_num(i)
        # 对resultList里面的各个数值进行一个n次方处理
        new_resultList = [j**n for j in resultList]
        # 判断如果这个list里面的总和等于i，则把结果写入到getList
        if sum(new_resultList) == i:
            getList.append(i)

    print(getList)


if __name__ == '__main__':
    narcissistic_num(6)