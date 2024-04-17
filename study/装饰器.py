# _*_ coding : utf_8 _*_
# @Time : 16:58 
# @Author : 田霄汉
# @File : 装饰器
# @Project : APIAutoTest
# @User : Administrator

# import time
#
# def getTime(func):
#     def demo(*args, **kwargs):
#         starttime = time.time()
#         func(*args, **kwargs)
#         endtime = time.time()
#         exectime = endtime - starttime
#         print("程序执行时间：{}".format(exectime))
#     return demo
#
# @getTime
# def function01():
#     time.sleep(3)
#     print("在测试用例01中")
#
#
# function01()

def pwd_switch(switch):
    if switch == 'on':
        def pwd(func):
            def demo(*args, **kwargs):

                try:
                    password = input("请输入账号的密码：")
                    if password == '123':
                        func(*args, **kwargs)
                    else:
                        print("密码错误，请重新输入")

                except Exception as e:
                    print("Error: " + format(str(e)))

            return demo
        return pwd
    else:
        def pwd(func):
            def demo(*args, **kwargs):
                try:
                    func()
                except Exception as e:
                    print("Error: {}".format(str(e)))
            return demo
        return pwd


@pwd_switch('on')
def buy():
    print("买入成功")

buy()