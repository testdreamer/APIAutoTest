#-- coding: utf-8 --

#@Time : 2022/10/20 13:05

#@Author : zhaopt

#@Email : zhaopt@casking.com.cn

#@File : runMain_udemr_s.py

#@Software: PyCharm
import os,sys
import yagmail
from Utils.log import *
from Utils.currenttime import *
from Utils.operation_xml import *
from Utils.zip_file import *
from s_udaam.test_cases.login import *
from Utils.performance_result_assertion import *
from Utils.operation_remote_server import *
from Utils.operation_jmeter_alone import *
from Utils.send_email import *
from Utils.operation_zentao_mysql import *
from Utils.operation_minio import *
from Utils.get_html_data import *
from sys import platform
from Utils.copy_and_clear_file import *
import html
from s_udaam.test_cases.operation_rsas_by_xml import *
import pandas as pd
import json
from Utils.operationini import *
from Utils.all_style_template import *
cf = Conf
if __name__ == '__main__':
    # 获取命令执行py的参数,这个文件是在runMain_all中调用
    system_id = str(sys.argv[1])
    # system_id = 'udaam'
    # 获取当前时间
    now_time = time.strftime("%Y%m%d%H%M%S")
    # 获取配置文件内容
    udaam_config_xml = sys.path[0] + '/s_udaam/data/'+system_id+'/config.xml'
    mail_config = sys.path[0] + '/s_udaam/data/'+system_id+'/mail_config.yaml'
    bug_mail_addressee = read_yaml(mail_config, 'bug_mail_addressee')
    bug_mail_cc = read_yaml(mail_config, 'bug_mail_cc')
    result_mail_addressee = read_yaml(mail_config, 'result_mail_addressee')
    result_mail_cc = read_yaml(mail_config, 'result_mail_cc')
    zentao_bug_commit = read_yaml(mail_config, 'zentao_bug_commit')
    zentao_bug_assign = read_yaml(mail_config, 'zentao_bug_assign')
    # 根据当前系统创建文件夹
    path = sys.path[0] + '\s_udaam\\reports\\' + system_id
    if ("linux" == platform) or ("linux2" == platform):
        os.system('mkdir ' + path.replace('\\', '/'))
    elif ("win32" == platform):
        os.system('md ' + path)
    else:
        log.info("----------Others-----------")

    # 调用绿盟创建扫描任务接口
    task_id = rsas_create_task(udaam_config_xml)
    print(task_id)
    time.sleep(600)
    # 调用绿盟生成测试报告接口
    report_id = rsas_create_report(task_id)
    print(report_id)
    time.sleep(20)
    # 调用绿盟下载测试报告接口
    rsas_download_report_zip(report_id,'html',path)
    time.sleep(10)
    rsas_download_report_zip(report_id, 'pdf',path)
    time.sleep(10)
    rsas_download_report_zip(report_id, 'xls', path)
    time.sleep(10)
    # 定义本地测试报告路径
    index_html = path+'\\index.html'
    index_pdf = path + '\\index.pdf'
    index_xls = path + '\\index.xls'
    # 重命名pdf测试报告
    report_name = system_id + '绿盟安全评估报告'+ now_time+'.pdf'
    report_pdf = path + '\\' + report_name
    # 读取html测试报告
    html = open(index_html, 'r', encoding='utf-8').read()  # local html
    querys = pyquery.PyQuery(html.encode('utf-8'))
    # 获取测试报告中的内容
    safety_level = querys("td").eq(0).text()
    task_name = querys("td").eq(2).text()
    scan_target = querys("td").eq(3).text()
    task_type = querys("td").eq(4).text()
    task_status = querys("td").eq(5).text()
    vulnerability_scan_template = querys("td").eq(6).text()
    to_task_user = querys("td").eq(7).text()
    task_data_source = querys("td").eq(8).text()
    task_info = querys("td").eq(9).text()
    info_statistics = querys("td").eq(12).text()
    domain_statistics = querys("td").eq(13).text()
    time_statistics = querys("td").eq(14).text()
    version_statistics = querys("td").eq(15).text()
    task_name_tmp = task_name[2:][1:][:-1]
    safety_level_upd = safety_level[0:4]
    # 根据安全等级分配安全等级模板
    safety_level_tmp = ''
    if safety_level_upd == '比较安全':
        safety_level_tmp = '<span class="level_danger middle" style="color:#396DC3">'+safety_level
    else:
        safety_level_tmp = '<span class="level_danger middle" style="color:#FF0000">' + safety_level

    total_high_risk = querys("td").eq(34).text()
    total_middle_risk = querys("td").eq(35).text()
    # 根据中风险和高风险判断是否有bug
    res = total_high_risk == '0' and total_middle_risk == '0'
    #获取xml文件内容,读漏洞列表页,不读取第一行,只读取123456列
    data = pd.read_excel(index_xls, '漏洞列表',keep_default_na=False,skiprows=1,usecols=[1,2,3,4,5,6])
    pd.set_option('display.width', None)
    #将获取的内容生成html表格
    html_table = data.to_html(path+'\\risk.html')
    html = open(path+'\\risk.html', 'r', encoding='utf-8').read()  # local html
    querys = pyquery.PyQuery(html.encode('utf-8'))

    import html
    import shutil
    # 复制文件并重命名
    shutil.copyfile(index_pdf, report_pdf)
    # 用os的重命名
    # os.rename(index_pdf, report_pdf)
    # 上传文件到MinIO Browser
    minio_file_upload('192.168.13.148:63805', 'AKIAIOSFODNN7EXAMPLE', 'wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY',
                      'udaam', report_name, report_pdf)
    # 转义html文件
    cdata = html.unescape(str(querys))
    # 定义禅道bug的标题,内容,实际结果,预期结果
    title = '[安全自动化bug]' + '[' + system_id + ']' + '存在中高风险'
    content = system_id + ',绿盟扫描'+'[<a href="'+task_name_tmp+'">'+task_name_tmp+'</a>]'
    pra_result = '存在中高风险!'+'<br/><br/>'+'请查看安全评估报告!'
    exp_result = '不存在中高风险'
    # 定义禅道bug模板
    mail_temp = bug_mail_template_insert_accessory('"http://192.168.13.148:63805/'+'udaam'+'/'+report_name+'"', report_name, content, pra_result, exp_result, new_time().split(' ')[0],
                                  new_time().split(' ')[1], '禅道管理').replace('服务器错误!','')
    # rsas_bug_to_zentao(res, title, mail_temp, 'zhaopt', 'zhaopt','202211/eeee',system_id+'安全评估报告.pdf','pdf','222')
    # bug写进禅道
    bug_to_zentao(res, title, mail_temp, zentao_bug_commit, zentao_bug_assign)
    # 获取禅道bugid
    bug_id = from_zentaotitle_get_zentaoid(title)
    #定义bug邮件模板
    pra_result_mail = '存在中高风险,请查看安全评估报告!'
    mail_temp = bug_mail_template(str(bug_id), title, content, pra_result_mail, exp_result, new_time().split(' ')[0],
                                  new_time().split(' ')[1], '禅道管理').replace('服务器错误!','')
    title_mail = 'BUG #' + str(bug_id) + ' ' + title + ' - ' + system_id
    # 重命名测试报告,显示bugid,当前时间
    report_bugid = system_id + '绿盟安全评估报告'+ now_time+'_禅道BugId='+str(bug_id)+'.pdf'
    # 复制测试报告到重命名的测试报告
    shutil.copyfile(index_pdf, report_bugid)
    # 判断如果有中高风险就发邮件
    if res == False:
        rsas_send_email(bug_mail_addressee[0], title_mail, mail_temp, report_bugid, bug_mail_cc)
        # rsas_send_email('zhaopt@casking.com.cn', title_mail, mail_temp, report_bugid, bug_mail_cc)
        # rsas_send_email('wub@casking.com.cn', title_mail, mail_temp, report_bugid, bug_mail_cc)
    # 发送测试报告邮件
    yagindex = yagmail.SMTP(user={"cdzdhcs@casking.com.cn":system_id+'安全自动化'}, password='Chandao123', host='smtp.exmail.qq.com')
    template = """<div><div style="padding: 10px 0; border: none; vertical-align: middle;"><strong style="font-size: 16px"><div style="border-collapse: collapse; background-color: #fff; border: 1px solid #cfcfcf; box-shadow: 0 0px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px; font-size:13px;"><div style="padding: 10px; background-color: #F8FAFE; border: none; font-size: 14px; font-weight: 500; border-bottom: 1px solid #e5e5e5;"><div text-align="center"><p align="center"><strong><font size="5">"""+system_id+"""安全评估报告</font></strong></p></div><table class="report_table"><tbody><tr class="odd"><th width="120"style="vertical-align:middle">网络风险</th><td style="padding:6px;"><span class="level_danger middle"style="color:#396DC3">"""+safety_level_tmp+"""</span></td></tr></tbody></table><table width="100%"><tbody><tr><td width="50%"valign="top"><table class="report_table plumb"><tbody><tr class="odd"><th width="120">任务名称</th><td>扫描[<a href="""+task_name_tmp+""">"""+task_name_tmp+"""</a>]</td></tr><tr class="even"><th width="120">扫描目标</th><td><a href="""+scan_target+""">"""+scan_target+"""</a></td></tr><tr class="odd"><th>任务类型</th><td>"""+task_type+"""</td></tr><tr class="even"><th width="120">任务状态</th><td>"""+task_status+"""</td></tr><tr class="odd"><th>漏洞扫描模板</th><td>"""+vulnerability_scan_template+"""</td></tr><tr class="even"><th>下达任务用户</th><td>"""+to_task_user+"""</td></tr><tr class="odd"><th>任务数据来源</th><td>"""+task_data_source+"""</td></tr><tr class="even"><th>任务说明</th><td>"""+task_info+"""</td></tr></tbody></table></td><td width="20px"></td><td width="50%"valign="top"><table class="report_table plumb"><tbody><tr class="odd"><th width="120px">信息统计</th><td>"""+info_statistics+"""</td></tr><tr class="even"><th width="120px">域名统计</th><td>"""+domain_statistics+"""</td></tr><tr class="odd"><th width="120px">时间统计</th><td>"""+time_statistics+"""</td></tr><tr class="even"><th>版本信息</th><td>"""+version_statistics+"""</td></tr></tbody></table></td></tr></tbody></table><div style="padding: 10px; background-color: #FFF0D5"><span style="font-size: 16px; color: #F1A325">●</span>&nbsp;<span><span style="border-bottom:1px dashed #ccc;"t="5"times=" 13:55">""" + new_time().split(' ')[0] + """</span>"""+ ""+new_time().split(' ')[1] + """,由<strong>""" + system_id+'安全自动化' + """</strong>创建。</span></div></div></div></div>"""
    # contents1 = [template_file, yagmail.inline(sys.path[-1] +'\luokuan.jpg'), inscribe]
    # yagindex.send('zhaopengtian@lefu.cc', 'yagmail带附件主题实例', yag_contents, new_report)
    send_to = ['wub@casking.com.cn', 'zhaopt@casking.com.cn']
    # yagindex.send(send_to, '身份认证系统接口自动化测试报告', contents1, test_report)
    # if get_html_data(filename)[2].strip() == '0':
    # yagindex.send('wub@casking.com.cn', new_time().split(' ')[0]+' '+new_time().split(' ')[1] + '[性能自动化]-身份认证系统性能测试报告', template)
    # yagindex.send('3407135351@qq.com', new_time().split(' ')[0]+' '+new_time().split(' ')[1] + '[性能自动化]-身份认证系统性能测试报告',template,res_zip)
    # yagindex.send('zhaopt@casking.com.cn', new_time().split(' ')[0]+' '+new_time().split(' ')[1] + '[安全自动化]-'+system_id+'安全评估报告', template,report_pdf)
    yagindex.send(result_mail_addressee,new_time().split(' ')[0] + ' ' + new_time().split(' ')[1] + '[安全自动化]-'+system_id+'安全评估报告',template,report_bugid, cc=result_mail_cc)
    # yagindex.send('zhaopt@casking.com.cn', new_time().split(' ')[0]+' '+new_time().split(' ')[1] + '[安全自动化]-'+system_id+'安全评估报告', template,report_bugid)
    # yagindex.send('tianxh@casking.com.cn', new_time().split(' ')[0]+' '+new_time().split(' ')[1] + '[安全自动化]-'+system_id+'安全评估报告', template,report_pdf)
    log.info('发送邮件成功')
    # 删除复制的测试报告
    os.remove(report_pdf)
    os.remove(report_bugid)
