# _*_ coding : utf_8 _*_
# @Time : 2024/3/4 11:46
# @Author : 田霄汉
# @File : 企业将近发放
# @Project : reliangApiTest

"""
      企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；利润高

　　　于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提

　　　成7.5%；20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于

　　　40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于

　　　100万元时，超过100万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？
"""

# 笨拙的方法
def function_01(profit):

    # profit = int(input("请输入公司利润（单位：万元）："))
    if profit <= 10:
        bonus = profit*0.1
    elif 10 < profit <= 20:
        bonus = (profit-10)*0.075+1
    elif 20 < profit <= 40:
        bonus = (profit-20)*0.05+1.75
    elif 40 < profit <= 60:
        bonus = (profit-40)*0.03+2.75
    elif 60 < profit <= 100:
        bonus = (profit-60)*0.015+3.35
    else:
        bonus = (profit-100)*0.01+3.95
    print(bonus)

# 高手写的代码
def function_02(profit):
    if profit <= 10:
        bonus = profit*0.1
    elif 10 < profit <= 20:
        bonus = (profit-10)*0.075 + function_02(10)
    elif 20 < profit <= 40:
        bonus = (profit-20)*0.05 + function_02(20)
    elif 40 < profit <= 60:
        bonus = (profit-40)*0.03 + function_02(40)
    elif 60 < profit <= 100:
        bonus = (profit-60)*0.015 + function_02(60)
    else:
        bonus = (profit-100)*0.01 + function_02(100)
    return bonus

# bonus = function_02(90)
# print(bonus)
function_01(120)