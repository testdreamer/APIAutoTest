#-- coding: utf-8 --

#@Time : 2023/1/4 13:39

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : runMain_performanceauto_flask.py

#@Software: PyCharm
import os,sys
import yagmail
from Utils.log import *
from Utils.currenttime import *
from Utils.operation_xml import *
from Utils.zip_file import *
from p_udemr.test_cases.udemr.login import *
from Utils.performance_result_assertion import *
from Utils.operation_remote_server import *
from Utils.operation_jmeter_alone import *
from Utils.send_email import *
from Utils.operation_zentao_mysql import *
from sys import platform
from Utils.operationyaml import *
import json
from Utils.operationini import *
from Utils.all_style_template import *
cf = Conf
if __name__ == '__main__':
    # 获取命令执行py的参数,这个文件是在runMain_all中调用
    system_id = str(sys.argv[1])
    # 获取当前时间
    now = time.strftime("%Y-%m-%d-%H-%M-%S")
    # 读取配置文件
    jmeter_script_config = sys.path[0] + '/p_udemr/data/'+system_id+'/'+system_id+'jmeter_script_config.ini'
    mail_config = sys.path[0] + '/p_udemr/data/'+system_id+'/'+system_id+'mail_config.yaml'
    jmeter_script_name = cf.getini_by_option(jmeter_script_config,'jmeter脚本名称','jmeter_script_name')
    master_hostname = cf.getini_by_option(jmeter_script_config, '压测调度服务器', 'hostname')
    master_username = cf.getini_by_option(jmeter_script_config, '压测调度服务器', 'username')
    master_password = cf.getini_by_option(jmeter_script_config, '压测调度服务器', 'password')
    slave_hostname = cf.getini_by_option(jmeter_script_config, '压测执行服务器', 'hostname')
    total_users = cf.getini_by_option(jmeter_script_config, '性能需求', 'totalUsers')
    script_name = cf.getini_by_option(jmeter_script_config, '性能需求', 'scriptName')
    bug_mail_addressee = read_yaml(mail_config,'bug_mail_addressee')
    bug_mail_cc = read_yaml(mail_config, 'bug_mail_cc')
    result_mail_addressee = read_yaml(mail_config, 'result_mail_addressee')
    result_mail_cc = read_yaml(mail_config, 'result_mail_cc')
    zentao_bug_commit = read_yaml(mail_config, 'zentao_bug_commit')
    zentao_bug_assign = read_yaml(mail_config, 'zentao_bug_assign')
    # 命名测试报告目录
    res = jmeter_script_name + now + 'report'
    jtl = res + '/' + now + 'res.jtl'
    # 远程jmeter脚本地址
    remote_jmx = '/usr/local/jmeter/apache-jmeter-5.1.1/scripts/'+ jmeter_script_name + '.jmx'
    # 根据当前操作系统,按被测项目名创建文件夹
    path = sys.path[0] + '\p_udemr\\test_cases\\' + system_id
    if ("linux" == platform) or ("linux2" == platform):
        os.system('mkdir ' + path.replace('\\', '/'))
    elif ("win32" == platform):
        os.system('md ' + path)
    else:
        log.info("----------Others-----------")
    # 本地jmeter脚本地址
    local_jmx = sys.path[0] + '/' + 'p_udemr' + '/' + 'test_cases' + '/'+system_id+'/' + jmeter_script_name + '.jmx'
    # res_zip = res+'.zip'
    #从服务器拉取jmeter脚本
    # file_download_linux(master_hostname , master_username, master_password,remote_jmx,local_jmx)
    # read_config_file_download_linux()

    #获取token
    token = test_login(jmeter_script_config)
    #将token写到jmx中
    from_xpath_update_content(local_jmx,'.//stringProp[contains(text(),"Bearer ")]','Bearer '+token)
    #将jmeter脚本上传到服务器
    file_upload_linux(master_hostname , master_username, master_password,local_jmx,remote_jmx)
    # 执行jmeter脚本
    comd = 'cd /usr/local/jmeter/apache-jmeter-5.1.1/bin;source /etc/profile;jmeter -n -t '+remote_jmx+' -l /usr/local/jmeter/apache-jmeter-5.1.1/report/'+res+'/'+res+'.jtl -e -o /usr/local/jmeter/apache-jmeter-5.1.1/report/'+res
    execute_linux_commnd(master_hostname , master_username, master_password, comd)
    print(script_name+'----jmeter性能压测中......')
    log.info(script_name+'----jmeter性能压测中......')
    path = sys.path[0] + '\p_udemr\\reports\\' + res
    if ("linux" == platform) or ("linux2" == platform):
        os.system('mkdir ' + path.replace('\\','/'))
    elif ("win32" == platform):
        os.system('md '+path)
    else:
        log.info("----------Others-----------")
    #从服务器中下载测试报告到本地
    file_download_linux(master_hostname , master_username, master_password,'/usr/local/jmeter/apache-jmeter-5.1.1/report/'+res+'/statistics.json',sys.path[0] + '/p_udemr/reports/'+res+'/statistics.json')
    file_download_linux(master_hostname, master_username, master_password,'/usr/local/jmeter/apache-jmeter-5.1.1/report/' + res + '/'+res+'.jtl',sys.path[0] + '/p_udemr/reports/' + res + '/'+res+'.jtl')
    file_download_linux(master_hostname , master_username, master_password,'/usr/local/jmeter/apache-jmeter-5.1.1/report/' + res + '/index.html',sys.path[0] + '/index.html')
    # 定义本地jtl文件路径
    local_jtl = sys.path[0] + '/p_udemr/reports/' + res + '/'+res+'.jtl'
    # os.chdir(sys.path[0] + '/' +'apache-jmeter-5.4.3'+'/'+'bin')
    # os.system('jmeter -n -t '+jmx+' -l '+jtl+' -e -o '+res)
    #测试报告进行压缩
    # make_zip(res,res_zip)
    # 获取配置文件的接口响应时间,返回dict
    api_rt_dict = cf.getini_by_section(jmeter_script_config, '接口响应时间')
    file = sys.path[0] + '/p_udemr/reports/' + res + '/statistics.json'
    # 定义list变量和dict变量
    res_template_list = []
    res_template_exp_text_list = []
    res_template_pra_text_list = []
    res_list = []
    exp_errorpct = {}
    # 循环配置文件的接口响应时间dict
    for key in api_rt_dict:
        # 循环读取statistics.json文件
        with open(file, encoding='utf-8') as a:
            # 读取文件
            result = json.load(a)
            # 获取json文件中的Total所以值
            transaction = str(result.get('Total').get('transaction'))
            sampleCount = str(result.get('Total').get('sampleCount'))
            errorCount = str(result.get('Total').get('errorCount'))
            errorPct = str(result.get('Total').get('errorPct'))
            meanResTime = str(round(result.get('Total').get('meanResTime') / 1000, 2))
            # medianResTime = str(result.get('Total').get('medianResTime')/1000)+'秒'
            minResTime = str(round(result.get('Total').get('minResTime') / 1000, 2)) + '秒'
            maxResTime = str(round(result.get('Total').get('maxResTime') / 1000, 2)) + '秒'
            pct1ResTime = str(round(result.get('Total').get('pct1ResTime') / 1000, 2)) + '秒'
            pct2ResTime = str(round(result.get('Total').get('pct2ResTime') / 1000, 2)) + '秒'
            pct3ResTime = str(round(result.get('Total').get('pct3ResTime') / 1000, 2)) + '秒'
            throughput = str(round(result.get('Total').get('throughput'), 2))
            receivedKBytesPerSec = str(round(result.get('Total').get('receivedKBytesPerSec'), 2))
            sentKBytesPerSec = str(round(result.get('Total').get('sentKBytesPerSec'), 2))
            # 获取json文件中的按配置文件中接口响应时间的所有Key的所以值
            http_request_name = key
            http_request_transaction = str(result.get(http_request_name).get('transaction'))
            http_request_sampleCount = str(result.get(http_request_name).get('sampleCount'))
            http_request_errorCount = str(result.get(http_request_name).get('errorCount'))
            http_request_errorPct = str(result.get(http_request_name).get('errorPct'))
            http_request_meanResTime = str(round(result.get(http_request_name).get('meanResTime') / 1000, 2))
            # http_request_medianResTime = str(result.get(http_request_name).get('medianResTime') / 1000) + '秒'
            http_request_minResTime = str(round(result.get(http_request_name).get('minResTime') / 1000, 2)) + '秒'
            http_request_maxResTime = str(round(result.get(http_request_name).get('maxResTime') / 1000, 2)) + '秒'
            http_request_pct1ResTime = str(round(result.get(http_request_name).get('pct1ResTime') / 1000, 2)) + '秒'
            http_request_pct2ResTime = str(round(result.get(http_request_name).get('pct2ResTime') / 1000, 2)) + '秒'
            http_request_pct3ResTime = str(round(result.get(http_request_name).get('pct3ResTime') / 1000, 2)) + '秒'
            http_request_throughput = str(round(result.get(http_request_name).get('throughput'), 2))
            http_request_receivedKBytesPerSec = str(round(result.get(http_request_name).get('receivedKBytesPerSec'), 2))
            http_request_sentKBytesPerSec = str(round(result.get(http_request_name).get('sentKBytesPerSec'), 2))
            # 定义bug邮件模板的html
            tr_v = '<tr role=row class=odd>'
            td_v = """<td>"""+http_request_name+"""<td>"""+http_request_sampleCount+"""<td>"""+http_request_errorCount+"""<td>"""+http_request_errorPct+"""<td>"""+http_request_meanResTime+"""<td>"""+http_request_minResTime+"""<td>"""+http_request_maxResTime+"""<td>"""+http_request_pct1ResTime+"""<td>"""+http_request_pct2ResTime+"""<td>"""+http_request_pct3ResTime+"""<td>"""+http_request_throughput+"""<td>"""+http_request_receivedKBytesPerSec+"""<td>"""+http_request_sentKBytesPerSec+""""""
            # 循环向list变量中添加html的结果
            res_template_exp_text_list.append('&nbsp;'*20+key+',页面响应时间不大于'+api_rt_dict[key]+'秒'+'<br />')
            res_template_pra_text_list.append('&nbsp;'*20+key+',页面响应时间为'+http_request_meanResTime+'秒'+'<br />')
            res_template_list.append(tr_v)
            res_template_list.append(td_v)
            # 定义需求错误率
            exp_errorpct[key] = 0.3
            # 实际的压测响应时间和配置文件中的需求响应时间进行比较,判断结果
            meanrestime_res = round(result.get(key).get('meanResTime') / 1000, 2) <= int(api_rt_dict[key])
            # 实际压测的错误率和需求错误率进行比较
            errorpct_res = result.get(key).get('errorPct') <= exp_errorpct[key]
            # 进行总体判断,响应时间和错误率判断
            res = round(result.get(key).get('meanResTime') / 1000, 2) <= int(api_rt_dict[key]) and result.get(key).get(
                'errorPct') <= exp_errorpct[key]
            # 判断如果响应时间有False,就返回这些结果
            if meanrestime_res == False:
                title = '[性能自动化bug]'+'['+script_name+']'+key+'实际响应时间大于需求响应时间'
                content = script_name+'需求并发数:'+total_users
                pra_result = key+'平均响应时间为:'+str(round(result.get(key).get('meanResTime') / 1000, 2))+'秒'
                exp_result = key+'平均响应时间为:'+api_rt_dict[key]+'秒'
            # 判断如果错误率有False,就返回这些结果
            if errorpct_res == False:
                title = '[性能自动化bug]' + '[' + script_name + ']' + key + '错误率大于0.3%'
                content = script_name + '需求并发数:' + total_users
                pra_result = key + '错误率为:' + str(result.get(key).get('errorPct')) + '%'
                exp_result = key + '错误率为:不大于3%'
            # 通过邮件模板方法返回禅道模板
            mail_temp = bug_mail_template('', title, content, pra_result, exp_result, new_time().split(' ')[0],
                                          new_time().split(' ')[1], '禅道管理').replace('实际返回值与预期返回值不相等!','')
            # 将bug写到禅道
            bug_to_zentao(res, title, mail_temp, zentao_bug_commit, zentao_bug_assign)
            # 获取bugid
            bug_id = from_zentaotitle_get_zentaoid(title)
            # 通过邮件模板方法返回邮件模板
            mail_temp = bug_mail_template(str(bug_id), title, content, pra_result, exp_result, new_time().split(' ')[0],
                                          new_time().split(' ')[1], '禅道管理').replace('实际返回值与预期返回值不相等!','')
            title_mail = 'BUG #' + str(bug_id) + ' ' + title+' - '+script_name
            # 判断如果有False,就发邮件
            if res == False:
                rsas_send_email(bug_mail_addressee[0], title_mail, mail_temp, local_jtl, bug_mail_cc)
                # rsas_send_email('tianxh@casking.com.cn', title_mail, mail_temp, local_jtl, bug_mail_cc)
            # 收集每次判断的结果添加到list变量
            res_list.append(res)
    # 判断list变量中是否有False,如果有就返回不通过的html模板,如果没有就返回通过的html模板
    if False in res_list:
        res_text = '不通过'
        res_template = """<table border="4"cellspacing=0 style="margin: auto;"width='60%'><tr><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"></td><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong>通过</strong></td></tr><tr><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong><font color="red">√</font></strong></td><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong>不通过</strong></td></table>"""
    else:
        res_text = '通过'
        res_template = """<table border="4"cellspacing=0 style="margin: auto;"width='60%'><tr><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong><font color="green">√</font></strong></td><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong>通过</strong></td></tr><tr><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"></td><td class="td"style="font-size: 25px;width:200px;height:100px;text-align: center;"><strong>不通过</strong></td></table>"""
    # 将所有的list进行str连接
    res_template_pra_text_str = ''.join(res_template_pra_text_list)
    res_template_exp_text_str = ''.join(res_template_exp_text_list)
    res_template_str = ''.join(res_template_list)
    # 通过配置文件中的需求参数进行结果对比,如果实际压测的平均响应时间小于需求的平均响应时间则通过,否则不通过,同时返回需求参数
    # performance_assert = performance_demand_and_assertion(jmeter_script_config, meanResTime)
    # 发邮件
    yagindex = yagmail.SMTP(user={"cdzdhcs@casking.com.cn":script_name+'性能自动化'}, password='Chandao123', host='smtp.exmail.qq.com')
    template = """<div><div style="padding: 10px 0; border: none; vertical-align: middle;"><strong style="font-size: 16px">各位领导、同事:<br/>大家好，""" + script_name + """性能测试完成,结果为:""" + res_text+ res_template+ """<br/>并发需求规则:""" + script_name + """通过标准""" + total_users + """个并发数<br/>""" + res_template_exp_text_str + """<br/>实际测试结果:<br/>""" +res_template_pra_text_str+"""<br/><br/></div><div style="border-collapse: collapse; background-color: #fff; border: 1px solid #cfcfcf; box-shadow: 0 0px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px; font-size:13px;"><div style="padding: 10px; background-color: #F8FAFE; border: none; font-size: 14px; font-weight: 500; border-bottom: 1px solid #e5e5e5;"><div text-align="center"><p align="center"><strong><font size="5">数据统计</font></strong></p></div><table style="margin: auto;"width='90%'cellspacing=0 border="2"id="statisticsTable"class="table table-bordered table-condensed tablesorter tablesorter-blue"role="grid"><th data-sorter="false"colspan="1"data-column="0"class="tablesorter-header sorter-false tablesorter-headerUnSorted"scope="col"role="columnheader"aria-disabled="true"unselectable="on"aria-sort="none"style="user-select: none;"><div class="tablesorter-header-inner">请求</div></th><th data-sorter="false"colspan="3"data-column="1"class="tablesorter-header sorter-false tablesorter-headerUnSorted"scope="col"role="columnheader"aria-disabled="true"unselectable="on"aria-sort="none"style="user-select: none;"><div class="tablesorter-header-inner">执行</div></th><th data-sorter="false"colspan="7"data-column="4"class="tablesorter-header sorter-false tablesorter-headerUnSorted"scope="col"role="columnheader"aria-disabled="true"unselectable="on"aria-sort="none"style="user-select: none;"><div class="tablesorter-header-inner">响应时间(s)</div></th><th data-sorter="false"colspan="1"data-column="11"class="tablesorter-header sorter-false tablesorter-headerUnSorted"scope="col"role="columnheader"aria-disabled="true"unselectable="on"aria-sort="none"style="user-select: none;"><div class="tablesorter-header-inner">吞吐量</div></th><th data-sorter="false"colspan="2"data-column="12"class="tablesorter-header sorter-false tablesorter-headerUnSorted"scope="col"role="columnheader"aria-disabled="true"unselectable="on"aria-sort="none"style="user-select: none;"><div class="tablesorter-header-inner">网络(KB/sec)</div></th></div><tr role="row"class="tablesorter-headerRow"><th data-column="0"class="tablesorter-header tablesorter-headerAsc"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="ascending"aria-label="Label: Ascending sort applied, activate to apply a descending sort"style="user-select: none;"><div class="tablesorter-header-inner">标签</div></th><th data-column="1"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="#Samples: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">#采样</div></th><th data-column="2"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="FAIL: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">失败</div></th><th data-column="3"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="Error %: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">错误%</div></th><th data-column="4"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="Average: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">平均值</div></th><th data-column="5"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="Min: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">最小值</div></th><th data-column="6"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="Max: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">最大值</div></th><th data-column="8"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="90th pct: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">90%用户</div></th><th data-column="9"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="95th pct: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">95%用户</div></th><th data-column="10"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="99th pct: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">99%用户</div></th><th data-column="11"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="Transactions/s: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">吞吐率</div></th><th data-column="12"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="Received: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">接收</div></th><th data-column="13"class="tablesorter-header tablesorter-headerUnSorted"tabindex="0"scope="col"role="columnheader"aria-disabled="false"aria-controls="statisticsTable"unselectable="on"aria-sort="none"aria-label="Sent: No sort applied, activate to apply an ascending sort"style="user-select: none;"><div class="tablesorter-header-inner">发送</div></th></tr><div class="tablesorter-no-sort"><div role="row"><td>"""+transaction+"""</td><td>"""+sampleCount+"""</td><td>"""+errorCount+"""</td><td>"""+errorPct+"""</td><td>"""+meanResTime+"""秒</td><td>"""+minResTime+"""</td><td>"""+maxResTime+"""</td><td>"""+pct1ResTime+"""</td><td>"""+pct2ResTime+"""</td><td>"""+pct3ResTime+"""</td><td>"""+throughput+"""</td><td>"""+receivedKBytesPerSec+"""</td><td>"""+sentKBytesPerSec+"""</td></tr></div><div aria-live="polite"aria-relevant="all">"""+res_template_str+"""</table></fieldset></div><div style="padding: 10px; background-color: #FFF0D5"><span style="font-size: 16px; color: #F1A325">●</span>&nbsp;<span><span style="border-bottom:1px dashed #ccc;"t="5"times=" 13:55">""" + new_time().split(' ')[0] + """</span> """+ ""+new_time().split(' ')[1] + """,由<strong>""" + script_name+'性能自动化' + """</strong>创建。</span></div></div>"""
    yagindex.send(result_mail_addressee, new_time().split(' ')[0]+' '+new_time().split(' ')[1] + '[性能自动化]-'+script_name+'性能测试报告', template,local_jtl,cc=result_mail_cc)
    # yagindex.send('tianxh@casking.com.cn',new_time().split(' ')[0] + ' ' + new_time().split(' ')[1] + '[性能自动化]-' + script_name + '性能测试报告',template)
    log.info('发送邮件成功')
