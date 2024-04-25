# _*_ coding : utf_8 _*_
# @Time : 21:20 
# @Author : 田霄汉
# @File : plugin
# @Project : APIAutoTest
# @User : Administrator


from datetime import datetime

def pytest_configure():
    # 配置加载完毕之后执行，测试用例执行之前
    print(f"{datetime.now()}pytest开始执行了")

def pytest_unconfigure():
    # 配置卸载完毕之后执行，测试用例执行之后
    print(f"{datetime.now()}pytest结束执行了")
