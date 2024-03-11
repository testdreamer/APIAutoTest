# -- coding: utf-8 --
# @Author : tianxh
# @Email : tianxh@casking.com.cn

from Utils.page import *
from Utils.dicttogetparameter import *
from Basepage.unittestChushihua import TestApi
from Utils.operationyaml import *
from Utils.operationini import Conf
from Utils.operationini import *
from Utils.log import *
from Utils.send_email import *
from Utils.operation_zentao_mysql import *
from Utils.currenttime import *
from Utils.all_style_template import *
import json
from Utils.encrypt import *
from Utils.currenttime import *
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
#统计分析模块
class Test_ReportForms(TestApi,Helper):
    """
    统计分析模块：
    /sys/platReportForms/page/userActivity 用户活跃排名查询
    /sys/platReportForms/page/summary  日志消息分类、消息总数、越权数据条数查询
    /sys/orgReportForms/page/getUserCount  应用访问统计-系统用户数
    /sys/orgReportForms/page/trend 应用访问统计-日志访问趋势
    /sys/orgReportForms/page/queryActiveTime   应用访问统计-时间点活跃排名
    """
    # 获取服务器地址,,,
    url = read_yaml(sys.path[-1] + '/data/server_address.yaml', 'url')
    case_paramt_ini = sys.path[-1] + '/data/case_parameters.ini'
    cf = Conf

    #用户活跃排名查询,正确
    def test_userActivity_right(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '用户活跃排名查询,正确')
        data = '"'+str(data)+'"'
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/platReportForms/page/userActivity?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        if self.url == '192.168.13.159:10041':
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['account'])
            print(sources)
            result = ('门户测试' in sources and
                      '协同门户测试' in sources and
                      '田策师' in sources and
                      '区域测试健教' in sources
                      )
            self.assertEqual(r.json()['code'], 200)
            self.assertTrue(result)
        else:
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['account'])
            print(sources)
            exp_account = ['xual','演示账号','chengshilin','宋亦琳']
            result = (set(exp_account) <= set(sources))
            res = r.json()['code'] == 200 and result==True
            case_section = '用户活跃排名查询,正确'
            url_path = '/sys/platReportForms/page/userActivity'
            mail_title_url = 'http://' + self.url + url_path
            request_method = 'get'
            print(result_buginfo_template(case_section, url, request_method, data, r))
            title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
            content = mail_buginfo_template(case_section, mail_title_url, request_method, '', r)[1]
            bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
            bug_id = from_zentaotitle_get_zentaoid(title)
            title_mail = 'BUG #' + str(bug_id) + ' ' + title
            mail_temp = bug_mail_template(str(bug_id), title, content,
                                          ['code=' + str(r.json()['code']),sources],
                                          ['code=200',exp_account],
                                          new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
            if res == False:
                send_email('liny@casking.com.cn', title_mail, mail_temp)
            self.assertEqual(r.json()['code'], 200)
            self.assertEqual(r.json()['message'], '成功')
            self.assertTrue(result)

    #用户活跃排名查询，未传开始时间
    def test_userActivity_wrong_nobegindata(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '用户活跃排名查询,未传开始时间')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/platReportForms/page/userActivity?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        if self.url == '192.168.13.159:10041':
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['account'])
            print(sources)
            result = ('数据质量专用' in sources and
                      '协同门户测试' in sources and
                      '田策师' in sources and
                      '区域测试健教' in sources
                      )
            self.assertEqual(r.json()['code'], 200)
            self.assertTrue(result)
        else:
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['account'])
            print(sources)
            exp_account = ['演示账号','chengshilin','udcms','宋亦琳']
            result = set(exp_account) <= set(sources)
            res = r.json()['code'] == 200 and result == True
            case_section = '用户活跃排名查询,未传开始时间'
            url_path = '/sys/platReportForms/page/userActivity'
            mail_title_url = 'http://' + self.url + url_path
            request_method = 'get'
            print(result_buginfo_template(case_section, url, request_method, data, r))
            title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
            content = mail_buginfo_template(case_section, mail_title_url, request_method, '', r)[1]
            bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
            bug_id = from_zentaotitle_get_zentaoid(title)
            title_mail = 'BUG #' + str(bug_id) + ' ' + title
            mail_temp = bug_mail_template(str(bug_id), title, content,
                                          ['code=' + str(r.json()['code']), sources],
                                          ['code=200', exp_account],
                                          new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
            if res == False:
                send_email('liny@casking.com.cn', title_mail, mail_temp)
            self.assertEqual(r.json()['code'], 200)
            self.assertEqual(r.json()['message'], '成功')
            self.assertTrue(result)

    #用户活跃排名查询，未传结束时间
    def test_userActivity_wrong_noenddata(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '用户活跃排名查询,未传结束时间')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/platReportForms/page/userActivity?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        if self.url == '192.168.13.159:10041':
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['account'])
            print(sources)
            result = ('数据质量专用' in sources and
                      '协同门户测试' in sources and
                      '田策师' in sources and
                      '区域测试健教' in sources
                      )
            self.assertEqual(r.json()['code'], 200)
            self.assertTrue(result)
        else:
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['account'])
            print(sources)
            exp_account = ['演示账号','chengshilin','udcms','宋亦琳']
            result = set(exp_account) <= set(sources)
            res = r.json()['code'] == 200 and result == True
            case_section = '用户活跃排名查询,未传结束时间'
            url_path = '/sys/platReportForms/page/userActivity'
            mail_title_url = 'http://' + self.url + url_path
            request_method = 'get'
            print(result_buginfo_template(case_section, url, request_method, data, r))
            title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
            content = mail_buginfo_template(case_section, mail_title_url, request_method, '', r)[1]
            bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
            bug_id = from_zentaotitle_get_zentaoid(title)
            title_mail = 'BUG #' + str(bug_id) + ' ' + title
            mail_temp = bug_mail_template(str(bug_id), title, content,
                                          ['code=' + str(r.json()['code']), sources],
                                          ['code=200', exp_account],
                                          new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
            if res == False:
                send_email('liny@casking.com.cn', title_mail, mail_temp)
            self.assertEqual(r.json()['code'], 200)
            self.assertEqual(r.json()['message'], '成功')
            self.assertTrue(result)
    #用户活跃排名查询，未传开始结束时间
    def test_userActivity_wrong_nodata(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '用户活跃排名查询,未传开始结束时间')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/platReportForms/page/userActivity?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        if self.url == '192.168.13.159:10041':
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['account'])
            print(sources)
            result = ('数据质量专用' in sources and
                      '协同门户测试' in sources and
                      '田策师' in sources and
                      '区域测试健教' in sources
                      )
            self.assertEqual(r.json()['code'], 200)
            self.assertTrue(result)
        else:
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['account'])
            print(sources)
            result = ('演示账号' in sources and
                      'chengshilin' in sources and
                      'udcms' in sources and
                      '宋亦琳' in sources
                      )
            exp_account = ['演示账号', 'chengshilin', 'udcms', '宋亦琳']
            result = set(exp_account) <= set(sources)
            res = r.json()['code'] == 200 and result == True
            case_section = '用户活跃排名查询,未传开始结束时间'
            url_path = '/sys/platReportForms/page/userActivity'
            mail_title_url = 'http://' + self.url + url_path
            request_method = 'get'
            print(result_buginfo_template(case_section, url, request_method, data, r))
            title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
            content = mail_buginfo_template(case_section, mail_title_url, request_method, '', r)[1]
            bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
            bug_id = from_zentaotitle_get_zentaoid(title)
            title_mail = 'BUG #' + str(bug_id) + ' ' + title
            mail_temp = bug_mail_template(str(bug_id), title, content,
                                          ['code=' + str(r.json()['code']), sources],
                                          ['code=200', exp_account],
                                          new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
            if res == False:
                send_email('liny@casking.com.cn', title_mail, mail_temp)
            self.assertEqual(r.json()['code'], 200)
            self.assertEqual(r.json()['message'], '成功')
            self.assertTrue(result)

    #日志消息分类、消息总数、越权数据条数查询
    #日志消息分类,正确
    def test_summary_right(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '日志消息分类,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/platReportForms/page/summary?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200 and r.json()['data']['totalNum'] == 0
        case_section = '日志消息分类,正确'
        url_path = '/sys/platReportForms/page/summary'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']), r.json()['data']['totalNum']],
                                      ['code=200', 0],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data']['totalNum'], 0)

    #应用访问统计-查询所有机构,正确
    def test_summary_query_all_org(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '应用访问统计-查询所有机构,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/findAllOrg?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        if self.url == '192.168.13.159:10041':
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['name'])
            res = '健教测试龙岗区' in sources and '三国集团' in sources and '龙岗第三人民医院' in sources
            self.assertEqual(r.json()['code'], 200)
            self.assertTrue(res)
        else:
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['name'])
            exp_name = ['深圳联影','技术研发中心','皇家疗人医院']
            rest = set(exp_name) <= set(sources)
            res = r.json()['code'] == 200 and rest == True
            case_section = '应用访问统计-查询所有机构,正确'
            url_path = '/sys/orgReportForms/page/findAllOrg'
            mail_title_url = 'http://' + self.url + url_path
            request_method = 'get'
            print(result_buginfo_template(case_section, url, request_method, data, r))
            title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
            content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
            bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
            bug_id = from_zentaotitle_get_zentaoid(title)
            title_mail = 'BUG #' + str(bug_id) + ' ' + title
            mail_temp = bug_mail_template(str(bug_id), title, content,
                                          ['code=' + str(r.json()['code']), sources],
                                          ['code=200', exp_name],
                                          new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
            if res == False:
                send_email('liny@casking.com.cn', title_mail, mail_temp)
            self.assertEqual(r.json()['message'], '成功')
            self.assertTrue(res)

    #应用访问统计-查询机构下的所有系统,正确
    def test_summary_query_org_all_sys(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '应用访问统计-查询机构下的所有系统,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/getAllSystem?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        if self.url == '192.168.13.159:10041':
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['name'])
            res = '测试0506' in sources and '测试内部应用' in sources and '统一身份认证' in sources
            self.assertEqual(r.json()['code'], 200)
            self.assertTrue(res)
        else:
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['name'])
            exp_name = ['40-testSystem','40Test-Layout','40内应用']
            rest = set(exp_name) <= set(sources)
            res = r.json()['code'] == 200 and rest == True
            case_section = '应用访问统计-查询机构下的所有系统,正确'
            url_path = '/sys/orgReportForms/page/getAllSystem'
            mail_title_url = 'http://' + self.url + url_path
            request_method = 'get'
            print(result_buginfo_template(case_section, url, request_method, data, r))
            title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
            content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
            bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
            bug_id = from_zentaotitle_get_zentaoid(title)
            title_mail = 'BUG #' + str(bug_id) + ' ' + title
            mail_temp = bug_mail_template(str(bug_id), title, content,
                                          ['code=' + str(r.json()['code']), sources],
                                          ['code=200', exp_name],
                                          new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
            if res == False:
                send_email('liny@casking.com.cn', title_mail, mail_temp)
            self.assertEqual(r.json()['code'], 200)
            self.assertEqual(r.json()['message'], '成功')
            self.assertTrue(res)


    #应用访问统计-菜单使用频率,正确
    def test_summary_menu_use_frequency(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '应用访问统计-菜单使用频率,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/useFrequency?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '应用访问统计-菜单使用频率,正确'
        url_path = '/sys/orgReportForms/page/useFrequency'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=200'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')

    # 应用访问统计-系统访问频次,正确
    def test_summary_sys_call_frequency(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '应用访问统计-系统访问频次,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/accessFrequency?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '应用访问统计-系统访问频次,正确'
        url_path = '/sys/orgReportForms/page/accessFrequency'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=200'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')

    # 应用访问统计-系统用户数,正确
    def test_summary_sys_user_count(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '应用访问统计-系统用户数,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/getUserCount?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '应用访问统计-系统用户数,正确'
        url_path = '/sys/orgReportForms/page/getUserCount'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=200'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')

    # 应用访问统计-日志访问趋势,正确
    def test_summary_log_call_trend(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '应用访问统计-日志访问趋势,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/trend?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '应用访问统计-日志访问趋势,正确'
        url_path = '/sys/orgReportForms/page/trend'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=200'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')

    #日志消息分类，未传开始时间
    def test_summary_wrong_nobegindata(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '日志消息分类,未传开始时间')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/platReportForms/page/summary?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 500
        case_section = '日志消息分类,未传开始时间'
        url_path = '/sys/platReportForms/page/summary'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=500'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 500)
        self.assertEqual(r.json()['message'], '服务器内部错误')
        self.assertEqual(r.json()['data'], 'INTERNAL_SERVER_ERROR')

    #日志消息分类，未传结束时间
    def test_summary_wrong_noenddata(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '日志消息分类,未传结束时间')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/platReportForms/page/summary?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '日志消息分类,未传结束时间'
        url_path = '/sys/platReportForms/page/summary'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=200'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')

    #日志消息分类，未传开始结束时间
    def test_summary_wrong_nodata(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '日志消息分类,未传开始结束时间')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/platReportForms/page/summary?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 500
        case_section = '日志消息分类,未传开始结束时间'
        url_path = '/sys/platReportForms/page/summary'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=500'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 500)
        self.assertEqual(r.json()['message'], '服务器内部错误')
        self.assertEqual(r.json()['data'], 'INTERNAL_SERVER_ERROR')


    #应用访问统计-系统用户数
    def test_getUserCount_right(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '系统用户数,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/getUserCount?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        if self.url == '192.168.13.159:10041':
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['systemName'])
            res = '区域卫生综合管理系统' in sources and '多机构-总线服务系统' in sources and '闭环-危急值管理系统' in sources
            self.assertEqual(r.json()['code'], 200)
            self.assertTrue(res)
        else:
            sources = []
            for i in range(len(r.json()['data'])):
                sources.append(r.json()['data'][i]['systemName'])
            print(sources)
            result = ('数据共享发布系统' in sources and
                      '多机构-主数据管理系统' in sources and
                      '患者主索引管理系统' in sources
                      )
            res = r.json()['code'] == 200
            case_section = '系统用户数,正确'
            url_path = '/sys/orgReportForms/page/getUserCount'
            mail_title_url = 'http://' + self.url + url_path
            request_method = 'get'
            print(result_buginfo_template(case_section, url, request_method, data, r))
            title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
            content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
            bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
            bug_id = from_zentaotitle_get_zentaoid(title)
            title_mail = 'BUG #' + str(bug_id) + ' ' + title
            mail_temp = bug_mail_template(str(bug_id), title, content,
                                          ['code=' + str(r.json()['code'])],
                                          ['code=200'],
                                          new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
            if res == False:
                send_email('liny@casking.com.cn', title_mail, mail_temp)
            self.assertEqual(r.json()['code'], 200)
            self.assertEqual(r.json()['message'], '成功')
            # self.assertTrue(result)

    #系统用户数,未传机构机构
    def test_getUserCount_wrong_noorgid(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '系统用户数,未传机构机构')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/getUserCount?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200 and r.json()['data'] == []
        case_section = '系统用户数,未传机构机构'
        url_path = '/sys/orgReportForms/page/getUserCount'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data']],
                                      ['code=200',[]],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data'], [])

    #系统用户数,未传系统编码
    def test_getUserCount_wrong_nosysid(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '系统用户数,未传系统编码')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/getUserCount?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        sources = []
        for i in range(len(r.json()['data'])):
            sources.append(r.json()['data'][i]['systemName'])
        print(sources)
        exp_systemname = ['区域卫生综合管理系统']
        rest = set(exp_systemname) <= set(sources)
        res = r.json()['code'] == 200 and rest == True
        case_section = '系统用户数,未传系统编码'
        url_path = '/sys/orgReportForms/page/getUserCount'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']), sources],
                                      ['code=200', exp_systemname],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertTrue(rest)

    #系统用户数,未传所有编码
    def test_getUserCount_wrong_noallid(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '系统用户数,未传所有编码')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/getUserCount?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200 and r.json()['data'] == []
        case_section = '系统用户数,未传所有编码'
        url_path = '/sys/orgReportForms/page/getUserCount'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']), r.json()['data']],
                                      ['code=200', []],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data'], [])

    #应用访问统计-日志访问趋势
    def test_trend_right(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '日志访问趋势,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/trend?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '日志访问趋势,正确'
        url_path = '/sys/orgReportForms/page/trend'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=200'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')

    # 日志访问趋势,未传机构机构
    def test_trend_wrong_noorgid(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '日志访问趋势,未传机构机构')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/trend?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200 and r.json()['data'] == []
        case_section = '日志访问趋势,未传机构机构'
        url_path = '/sys/orgReportForms/page/trend'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data']],
                                      ['code=200',[]],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data'], [])

    # 日志访问趋势,未传开始时间
    def test_trend_wrong_nobeginDate(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '日志访问趋势,未传开始时间')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/trend?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '日志访问趋势,未传开始时间'
        url_path = '/sys/orgReportForms/page/trend'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=200'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        # self.assertEqual(r.json()['data'][0]['num'], 28)

    # 日志访问趋势,未传结束时间
    def test_trend_wrong_noendDate(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '日志访问趋势,未传结束时间')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/trend?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200 and r.json()['data'] == []
        case_section = '日志访问趋势,未传结束时间'
        url_path = '/sys/orgReportForms/page/trend'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data']],
                                      ['code=200',[]],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data'], [])
    # 日志访问趋势,未传所有值
    def test_trend_wrong_noalldata(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        # print(self.case_paramt_ini)

        data = self.cf.getini_by_section(self.case_paramt_ini, '日志访问趋势,未传所有值')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/orgReportForms/page/trend?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200 and r.json()['data'] == []
        case_section = '日志访问趋势,未传所有值'
        url_path = '/sys/orgReportForms/page/trend'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']), r.json()['data']],
                                      ['code=200', []],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data'], [])