#-- coding: utf-8 --

#@Time : 2022/9/22 17:34

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : performance_result_assertion.py

#@Software: PyCharm
import os,sys
from Utils.operationini import *
cf = Conf
def performance_demand_and_assertion(file,practical_average_response_time):
    """
    通过配置文件中的需求参数进行结果对比,如果实际压测的平均响应时间小于需求的平均响应时间则通过,否则不通过,
    同时返回需求参数
    :param file: 配置文件路径
    :param practical_average_response_time: 实际压测的平均响应时间
    :return: 需求参数&结果
    """
    #获取config.ini文件中[性能需求]所有值
    script_name = cf.getini_by_option(file,'性能需求','scriptName')
    total_users = cf.getini_by_option(file, '性能需求', 'totalUsers')
    expect_average_response_time = cf.getini_by_option(file, '性能需求', 'averageResponseTime')

    res = ''
    if float(practical_average_response_time) > float(expect_average_response_time):
        res = """
            <table border="4"cellspacing=0 style="margin: auto;"width='60%'><tr><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"></td><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong>通过</strong></td></tr><tr><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong><font color="red">√</font></strong></td><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong>不通过</strong></td></table>
        """
    else:
        res = """
            <table border="4"cellspacing=0 style="margin: auto;"width='60%'><tr><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong><font color="green">√</font></strong></td><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong>通过</strong></td></tr><tr><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"></td><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong>不通过</strong></td></table>
        """
    return script_name,total_users,expect_average_response_time,res