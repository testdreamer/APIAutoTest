#-- coding: utf-8 --

#@Time : 2023/1/3 11:08

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : runMain_apiauto_flask.py

#@Software: PyCharm
import xlrd
from HTMLTestRunner import HTMLTestRunner
import unittest
from Utils.currenttime import *
import sys,os
import xlrd
from HTMLTestRunner import HTMLTestRunner
from Utils.get_html_data import *
import yagmail
import requests
import json
from Utils.getImageverification import *
import pytest
import unittest
from Utils.create_random import *
from Utils.page import *
from Utils.currenttime import *
from Utils.operationyaml import *
from Utils.log import *
from Utils.operation_jsonpath import *
import ddt
import configparser
from Utils.encrypt import *
import sys,os

if __name__ == '__main__':
    # 获取命令执行py的参数,这个文件是在runMain_all中调用
    system_id = str(sys.argv[1])
    # system_id = '号源池'
    system_under_test_yaml = sys.path[0] + '/api_auto_excel/data/system_under_test.yaml'
    token_data = {'被测系统': system_id}
    write_yaml(system_under_test_yaml, token_data)
    #  清空yaml文件内容
    variable_storage_yaml = sys.path[-1] + '/api_auto_excel/data/variable_storage.yaml'
    clear_yaml(variable_storage_yaml)
    # excel_filename = 'http://192.168.13.148:63805/udaam/' + system_id + '接口用例脚本.xlsx'
    original_file = sys.path[-1] + '/api_auto_excel/test_cases/' + system_id + '接口用例脚本.xlsx'
    # from_wget_download_file(excel_filename, original_file)
    file_name = original_file
    # file_name = 'C:\\Users\\ud\\Desktop\\号源池接口用例脚本.xlsx'
    book = xlrd.open_workbook(file_name)
    # 通过下标方法读取sheet值
    sheet = book.sheet_by_name('配置')
    report_mail_addressee = sheet.cell_value(1, 3)
    print(report_mail_addressee)
    if sheet.cell_value(1, 4) != '':
        report_mail_cc = sheet.cell_value(1, 4)
    else:
        report_mail_cc = None
    sheet = book.sheet_by_name('接口用例')
    ust_name = str(sheet.cell_value(1, 1)).split('_')[0]

    # 记录用例执行前的时间
    get_times_start = get_time()
    get_times_start_ymd = new_time()
    sdir = sys.path[0] + '/api_auto_excel/business/'

    testlist = unittest.defaultTestLoader.discover(start_dir=sdir, pattern='register_case.py')
    now = time.strftime("%Y-%m-%d_%H:%M:%S")
    # filename = 'result.html'
    # filename = test_report + "\\" + now +'result.html'
    filename = sys.path[-1] + "/api_auto_excel/reports/" +ust_name+ '接口自动化测试报告.html'
    fp = open(filename, 'wb')

    runner = HTMLTestRunner(
        stream=fp,  # 文件
        verbosity=2,
        title=ust_name+"接口自动化测试报告",  # 标题
        description=u"系统环境：Liunx 用例执行情况："  # 描述
    )
    runner.run(testlist)  # 启动测试套件
    fp.close()
    #     发送邮件
    # 记录用例执行完的时间
    get_times_end = get_time()
    print(report_mail_addressee,report_mail_cc)
    print('所有用例 ：' + get_html_data(filename)[5])
    print('成功用例 ：' + get_html_data(filename)[4])
    print('失败用例 ：' + get_html_data(filename)[3])
    print('错误用例 ：' + get_html_data(filename)[2])
    # 计算用例执行时间
    run_time = (get_times_end - get_times_start) / 1000
    print('总运行时间:' + str(run_time) + 's')
    all_time = str(run_time) + 's'
    # 获取html测试报告的内容
    data = get_html_by_id_create_list(filename)
    # gf = Graphs()
    # 生成pdf的测试报告
    # gf.create_pdf(get_times_start_ymd, all_time, get_html_data(filename)[4], int(get_html_data(filename)[5]), int(get_html_data(filename)[4]), int(get_html_data(filename)[3]), data)
    notice = ''
    if '"message": "服务器内部错误"' in str(read_html(filename)):
        notice = '注意!需要开发人员查看,被测系统存在服务器内部错误!'
    elif '没有到主机的路由' in str(read_html(filename)):
        notice = '注意!需要开发人员查看,被测系统存在没有到主机的路由错误!'

    report_pdf = sys.path[-1] + "/" + 'fff.pdf'
    yagindex = yagmail.SMTP(user={"cdzdhcs@casking.com.cn": ust_name+'接口自动化'}, password='Chandao123',
                            host='smtp.exmail.qq.com')
    template = """<div style="line-height: 25px;"><div style="padding: 10px 0; border: none; vertical-align: middle;"><strong style="font-size: 16px">各位领导、同事:<br/>大家好，以下为"""+ust_name+"""接口自动化项目构建信息及运行结果</br></div><div style="border-collapse: collapse; background-color: #fff; border: 1px solid #cfcfcf; box-shadow: 0 0px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px; font-size:13px;"><div style="padding: 10px; background-color: #F8FAFE; border: none; font-size: 14px; font-weight: 500; border-bottom: 1px solid #e5e5e5;">禅道地址:<a href="http://192.168.13.148:63802/bug-browse-1-0-unclosed.html"style="color: #333; text-decoration: underline;"target="_blank">http://192.168.13.148:63802/bug-browse-1-0-unclosed.html</a><br/>在线测试报告:<a href="http://192.168.13.159:63363"style="color: #333; text-decoration: underline;"target="_blank">http://192.168.13.159:63363</a></div><div style="padding: 10px; border: none;"><fieldset style="border: 1px solid #e5e5e5"><legend style="color: #114f8e">状态</legend><div style="padding:5px;"><b><font color="#0B610B">构建信息</font></b><hr size="2"width="100%"align="center"/><ul style="line-height: 20px;"><li>项目名称："""+ust_name+"""接口自动化项目</li><li>触发原因：云帮-研发团队-"""+ust_name+"""</li><li>构建状态：操作成功</li><li>构建URL：<a href="http://192.168.13.159:10000/#/team/xdpvzcyl/region/CLUSTER-56/components/gr5279b8/overview">http://192.168.13.159:10000/#/team/xdpvzcyl/region/CLUSTER-56/components/gr5279b8/overview</a></li></ul><b><font color="#0B610B"style="font-size: 14px;">运行结果</font></b><hr size="2"width="100%"align="center"/><ul style="line-height: 20px;;margin-bottom: 0px;"><li>运行时长：""" + all_time + """</li><li>所有用例：""" + \
               get_html_data(filename)[5] + """</li><li>成功用例：""" + get_html_data(filename)[4] + """</li><li>失败用例：""" + \
               get_html_data(filename)[3] + """</li><li>错误用例：""" + get_html_data(filename)[
                   2] + """</li></ul><div><div style="font-size: 12px;color: #ddb100;border-bottom: 1px dashed #ccc;font-weight: bold;padding-left: 6px;font-weight: normal;">备注</div><ul style="color:#ddb100;line-height:20px; font-weight: normal;"><li>失败表示被测接口问题</li><li>错误表示测试用例问题</li></ul></div></div><div style="padding: 10px; background-color: #FFF0D5"><span style="font-size: 16px; color: #F1A325">●</span>&nbsp;<span><span style="border-bottom:1px dashed #ccc;"t="5"times=" 13:55">""" + \
               new_time().split(' ')[0] + """</span>""" + new_time().split(' ')[
                   1] + """,由<strong>""" + ust_name+'接口自动化' + """</strong>创建。</span></div></div>"""
    read_html(filename)
    if 'configparser.ParsingError' not in str(read_html(filename)) and 'WinError 10048' not in str(
            read_html(filename)) and '"message": "未经授权"' not in str(
            read_html(filename)) and 'UnicodeDecodeError' not in str(
            read_html(filename)) and 'configparser.DuplicateOptionError' not in str(read_html(filename)):
        pass
    yagindex.send(report_mail_addressee,
                  new_time().split(' ')[0] + ' ' + new_time().split(' ')[1] + '[接口自动化]' + '-' + ust_name + '接口自动化测试报告',
                  template, filename, cc=report_mail_cc)

    log.info('发送邮件成功')
