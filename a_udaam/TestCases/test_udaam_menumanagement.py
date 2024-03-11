#-- coding: utf-8 --

#@Time : 2022/6/11 13:19

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : test_udaam_menumanagement.py

#@Software: PyCharm
from Utils.page import *
from Utils.dicttogetparameter import *
from Basepage.unittestChushihua import TestApi
from Utils.operationyaml import *
from Utils.operationini import Conf
from Utils.operationini import *
from Utils.log import *
from Utils.currenttime import *
import json
from Utils.send_email import *
from Utils.operation_zentao_mysql import *
from Utils.encrypt import *
from Utils.currenttime import *
from Utils.all_style_template import *
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
class MenuManagement(TestApi,Helper):
    # 获取服务器地址,,,
    url = read_yaml(sys.path[-1] + '/data/server_address.yaml', 'url')
    case_paramt_ini = sys.path[-1] + '/data/case_parameters.ini'
    cf = Conf
    '''
                  查询所有系统资源,正确
       '''
    def test_query_all_system_resources(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '查询所有系统资源,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/menuManage/page/loadPermissionTree?'+get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)

        sources = []
        for i in range(len(r.json()['data'])):
            sources.append(r.json()['data'][i]['systemId'])
        if self.url == '192.168.13.159:10041':
            self.assertTrue(
                        'ff8bf7d9989c00ec4e0bb4b0baba9b4f' in sources)
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[新增组件目录,正确]的pid,systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[新增组件菜单,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[新增组件按钮,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[查询系统的资源,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[修改组件,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[删除组件按钮,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[删除组件菜单,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[删除组件目录,正确]的systemId
            if 'ff8bf7d9989c00ec4e0bb4b0baba9b4f' in sources:
                self.cf.put_ini(self.case_paramt_ini, '新增组件目录,正确', 'systemId', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
                self.cf.put_ini(self.case_paramt_ini, '新增组件目录,正确', 'pid', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
                self.cf.put_ini(self.case_paramt_ini, '新增组件菜单,正确', 'systemId', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
                self.cf.put_ini(self.case_paramt_ini, '新增组件按钮,正确', 'systemId', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
                self.cf.put_ini(self.case_paramt_ini, '查询系统的资源,正确', 'systemId', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
                self.cf.put_ini(self.case_paramt_ini, '修改组件,正确', 'systemId', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
                self.cf.put_ini(self.case_paramt_ini, '禁用菜单,正确', 'systemId', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
                self.cf.put_ini(self.case_paramt_ini, '禁用按钮,正确', 'systemId', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
                self.cf.put_ini(self.case_paramt_ini, '删除组件按钮,正确', 'systemId', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
                self.cf.put_ini(self.case_paramt_ini, '删除组件菜单,正确', 'systemId', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
                self.cf.put_ini(self.case_paramt_ini, '删除组件目录,正确', 'systemId', 'ff8bf7d9989c00ec4e0bb4b0baba9b4f')
            else:
                self.cf.put_ini(self.case_paramt_ini, '新增组件目录,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '新增组件目录,正确', 'pid', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '新增组件菜单,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '新增组件按钮,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '查询系统的资源,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '修改组件,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '禁用菜单,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '禁用按钮,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '删除组件按钮,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '删除组件菜单,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '删除组件目录,正确', 'systemId', r.json()['data'][0]['systemId'])

        else:
            res = r.json()['code'] == 200 and '55bc97dd2238499b521775578e798b73' in sources
            case_section = '查询所有系统资源,正确'
            url_path = '/sys/menuManage/page/loadPermissionTree'
            mail_title_url = 'http://' + self.url + url_path
            request_method = 'get'
            print(result_buginfo_template(case_section, url, request_method, data, r))
            title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
            content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
            bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
            bug_id = from_zentaotitle_get_zentaoid(title)
            title_mail = 'BUG #' + str(bug_id) + ' ' + title
            mail_temp = bug_mail_template(str(bug_id), title, content,
                                          ['code=' + str(r.json()['code']),sources],
                                          ['code=200',['55bc97dd2238499b521775578e798b73']],
                                          new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
            if res == False:
                send_email('liny@casking.com.cn', title_mail, mail_temp)
            self.assertTrue(
                '55bc97dd2238499b521775578e798b73' in sources)
            self.assertEqual(r.json()['code'], 200)
            self.assertEqual(r.json()['message'], '成功')

            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[新增组件目录,正确]的pid,systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[新增组件菜单,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[新增组件按钮,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[查询系统的资源,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[修改组件,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[删除组件按钮,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[删除组件菜单,正确]的systemId
            # 将查询所有系统资源的systemId值添加到case_parameters.ini文件的[删除组件目录,正确]的systemId
            if '55bc97dd2238499b521775578e798b73' in sources:
                self.cf.put_ini(self.case_paramt_ini, '新增组件目录,正确', 'systemId', '55bc97dd2238499b521775578e798b73')
                self.cf.put_ini(self.case_paramt_ini, '新增组件目录,正确', 'pid', '55bc97dd2238499b521775578e798b73')
                self.cf.put_ini(self.case_paramt_ini, '新增组件菜单,正确', 'systemId', '55bc97dd2238499b521775578e798b73')
                self.cf.put_ini(self.case_paramt_ini, '新增组件按钮,正确', 'systemId', '55bc97dd2238499b521775578e798b73')
                self.cf.put_ini(self.case_paramt_ini, '查询系统的资源,正确', 'systemId', '55bc97dd2238499b521775578e798b73')
                self.cf.put_ini(self.case_paramt_ini, '禁用菜单,正确', 'systemId', '55bc97dd2238499b521775578e798b73')
                self.cf.put_ini(self.case_paramt_ini, '禁用按钮,正确', 'systemId', '55bc97dd2238499b521775578e798b73')
                self.cf.put_ini(self.case_paramt_ini, '修改组件,正确', 'systemId', '55bc97dd2238499b521775578e798b73')
                self.cf.put_ini(self.case_paramt_ini, '删除组件按钮,正确', 'systemId', '55bc97dd2238499b521775578e798b73')
                self.cf.put_ini(self.case_paramt_ini, '删除组件菜单,正确', 'systemId', '55bc97dd2238499b521775578e798b73')
                self.cf.put_ini(self.case_paramt_ini, '删除组件目录,正确', 'systemId', '55bc97dd2238499b521775578e798b73')
            else:
                self.cf.put_ini(self.case_paramt_ini, '新增组件目录,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '新增组件目录,正确', 'pid', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '新增组件菜单,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '新增组件按钮,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '查询系统的资源,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '禁用菜单,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '禁用按钮,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '修改组件,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '删除组件按钮,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '删除组件菜单,正确', 'systemId', r.json()['data'][0]['systemId'])
                self.cf.put_ini(self.case_paramt_ini, '删除组件目录,正确', 'systemId', r.json()['data'][0]['systemId'])

        log.info('查询所有系统资源,正确')
        time.sleep(1)

    '''
               新增组件目录,正确
    '''
    def test_insert_module_dir(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        self.cf.put_ini(self.case_paramt_ini, '新增组件目录,正确','name',str(get_time()))
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '新增组件目录,正确')
        data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"', 'false')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/permission/page/list/add'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url, data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '新增组件目录,正确'
        url_path = '/sys/permission/page/list/add'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
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
        # 将新增组件目录的id值添加到case_parameters.ini文件的[新增组件菜单,正确]的pid
        self.cf.put_ini(self.case_paramt_ini, '新增组件菜单,正确', 'pid', r.json()['data'])
        # 将新增组件目录的id值添加到case_parameters.ini文件的[删除组件目录,正确]的id
        self.cf.put_ini(self.case_paramt_ini, '删除组件目录,正确', 'id', r.json()['data'])

        log.info('新增组件目录,正确')
        time.sleep(1)

    '''
            新增组件菜单,正确
    '''
    def test_insert_module_menu(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        self.cf.put_ini(self.case_paramt_ini, '新增组件菜单,正确', 'name', str(get_time()))
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '新增组件菜单,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/permission/page/list/add'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url, data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '新增组件菜单,正确'
        url_path = '/sys/permission/page/list/add'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
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
        # 将新增组件菜单的id值添加到case_parameters.ini文件的[新增组件按钮,正确]的pid
        self.cf.put_ini(self.case_paramt_ini, '新增组件按钮,正确', 'pid', r.json()['data'])
        # 将新增组件菜单的id值添加到case_parameters.ini文件的[查询系统的资源,正确]的pid
        self.cf.put_ini(self.case_paramt_ini, '查询系统的资源,正确', 'pid', r.json()['data'])
        # 将新增组件菜单的id值添加到case_parameters.ini文件的[禁用菜单,正确]的permissionId
        self.cf.put_ini(self.case_paramt_ini, '禁用菜单,正确', 'permissionId', r.json()['data'])
        # 将新增组件菜单的id值添加到case_parameters.ini文件的[修改组件,正确]的pid
        self.cf.put_ini(self.case_paramt_ini, '修改组件,正确', 'pid', r.json()['data'])
        # 将新增组件按钮的id值添加到case_parameters.ini文件的[删除组件按钮,正确]的id
        self.cf.put_ini(self.case_paramt_ini, '删除组件菜单,正确', 'id', r.json()['data'])
        log.info('新增组件菜单,正确')
        time.sleep(1)

    '''
                新增组件按钮,正确
        '''
    def test_insert_module_btn(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        self.cf.put_ini(self.case_paramt_ini, '新增组件按钮,正确', 'name', str(get_time()))
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '新增组件按钮,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/permission/page/list/add'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url, data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '新增组件按钮,正确'
        url_path = '/sys/permission/page/list/add'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
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
        # 将新增组件按钮的id值添加到case_parameters.ini文件的[禁用按钮,正确]的permissionId
        self.cf.put_ini(self.case_paramt_ini, '禁用按钮,正确', 'permissionId', r.json()['data'])
        # 将新增组件按钮的id值添加到case_parameters.ini文件的[修改组件,正确]的pid
        self.cf.put_ini(self.case_paramt_ini, '修改组件,正确', 'id', r.json()['data'])
        # 将新增组件按钮的id值添加到case_parameters.ini文件的[删除组件按钮,正确]的id
        self.cf.put_ini(self.case_paramt_ini, '删除组件按钮,正确', 'id', r.json()['data'])
        log.info('新增组件按钮,正确')
        time.sleep(1)

    '''
                    查询系统的资源,正确
            '''
    def test_query_system_resources(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '查询系统的资源,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/menuManage/page/getPermissionList?'+get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        # 获取[新增组件按钮,正确]的pid进行校验
        insertmodulemenu_pid = self.cf.getini_by_option(self.case_paramt_ini, '新增组件按钮,正确', 'pid')
        # 获取[新增组件按钮,正确]的name进行校验
        insertmodulemenu_name = self.cf.getini_by_option(self.case_paramt_ini, '新增组件按钮,正确', 'name')
        # 获取[查询系统的资源,正确]的systemId进行校验
        querysystemresources_sysid = self.cf.getini_by_option(self.case_paramt_ini, '查询系统的资源,正确', 'systemId')
        # 获取[查询系统的资源,正确]的pid进行校验
        querysystemresources_pid = self.cf.getini_by_option(self.case_paramt_ini, '查询系统的资源,正确', 'pid')
        res = r.json()['data']['content'][0]['pid']==insertmodulemenu_pid and r.json()['data']['content'][0]['name']==insertmodulemenu_name and r.json()['data']['content'][0]['systemId']==querysystemresources_sysid and r.json()['data']['content'][0]['pid']==querysystemresources_pid and r.json()['code'] == 200
        case_section = '查询系统的资源,正确'
        url_path = '/sys/menuManage/page/getPermissionList'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data']['content'][0]['pid'],r.json()['data']['content'][0]['name'],r.json()['data']['content'][0]['systemId'],r.json()['data']['content'][0]['pid']],
                                      ['code=200',insertmodulemenu_pid,insertmodulemenu_name,querysystemresources_sysid,querysystemresources_pid],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data']['content'][0]['pid'],insertmodulemenu_pid)
        self.assertEqual(r.json()['data']['content'][0]['name'], insertmodulemenu_name)
        self.assertEqual(r.json()['data']['content'][0]['systemId'], querysystemresources_sysid)
        self.assertEqual(r.json()['data']['content'][0]['pid'], querysystemresources_pid)
        #校验type
        self.assertEqual(r.json()['data']['content'][0]['type'],'3')
        # 将查询系统的资源的id值添加到case_parameters.ini文件的[新增组件按钮,正确]的pid
        self.cf.put_ini(self.case_paramt_ini, '修改组件,正确', 'code', r.json()['data']['content'][0]['code'])

        log.info('查询系统的资源,正确')
        time.sleep(1)

    """
                    修改组件,正确
    """
    def test_update_module(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        #获取新增组件按钮的name
        insertmodelbtn_name = self.cf.getini_by_option(self.case_paramt_ini,'新增组件按钮,正确','name')
        #修改后的name
        insertmodelbtnupdate_name = insertmodelbtn_name+'upd'
        #将修改后的name写到case_parameters.ini文件的[修改组件,正确]的name
        self.cf.put_ini(self.case_paramt_ini,'修改组件,正确','name',insertmodelbtnupdate_name)
        # 获取当前时间
        get_times = get_time()
        dangqian_time = get_times
        timeArray1 = time.localtime(dangqian_time / 1000)
        checkpoint1 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray1)

        #将当前时间写到case_parameters.ini文件的[修改组件,正确]的createTime
        self.cf.put_ini(self.case_paramt_ini, '修改组件,正确', 'createTime', checkpoint1)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '修改组件,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/permission/page/list/update'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url, data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '修改组件,正确'
        url_path = '/sys/permission/page/list/update'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
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

        log.info('修改组件,正确')
        time.sleep(1)

    '''
        2022-8-12新增
        禁用菜单,正确
    '''

    def test_disable_menu(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
         # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '禁用菜单,正确')
        get_parameter = dict_to_get_parameter(data)
        data1 = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        url = 'http://' + self.url + '/sys/menuManage/page/list/updateEnabled?'+get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '禁用菜单,正确'
        url_path = '/sys/menuManage/page/list/updateEnabled'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
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

        log.info('禁用菜单,正确')
        time.sleep(1)

    '''
           2022-8-12新增
           禁用按钮,正确
       '''

    def test_disable_btn(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '禁用按钮,正确')
        get_parameter = dict_to_get_parameter(data)
        data1 = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        url = 'http://' + self.url + '/sys/menuManage/page/list/updateEnabled?'+get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '禁用按钮,正确'
        url_path = '/sys/menuManage/page/list/updateEnabled'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
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

        log.info('禁用按钮,正确')
        time.sleep(1)

    """
             删除组件按钮,正确
    """
    def test_delete_module_btn(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        deletemodelbtn_id = self.cf.getini_by_option(self.case_paramt_ini,'删除组件按钮,正确','id')
        deletemodelbtn_systemId = self.cf.getini_by_option(self.case_paramt_ini, '删除组件按钮,正确', 'systemId')
        data = self.cf.getini_by_section(self.case_paramt_ini, '删除组件按钮,正确')
        data = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"','false')))
        ll = {}
        ll['systemId'] = json.loads(data)['systemId']
        data = str(ll)
        url = 'http://' + self.url + '/sys/permission/page/list/delete/'+deletemodelbtn_id+'?systemId='+deletemodelbtn_systemId
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url, data,headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '删除组件按钮,正确'
        url_path = '/sys/permission/page/list/delete/'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
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
        log.info('删除组件按钮,正确')
        time.sleep(1)

    """
                 删除组件菜单,正确
    """
    def test_delete_module_menu(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        deletemodelmenu_id = self.cf.getini_by_option(self.case_paramt_ini, '删除组件菜单,正确', 'id')
        deletemodelmenu_systemId = self.cf.getini_by_option(self.case_paramt_ini, '删除组件菜单,正确', 'systemId')
        data = self.cf.getini_by_section(self.case_paramt_ini, '删除组件菜单,正确')
        data = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        ll = {}
        ll['systemId'] = json.loads(data)['systemId']
        data = str(ll)
        url = 'http://' + self.url + '/sys/permission/page/list/delete/' + deletemodelmenu_id + '?systemId=' + deletemodelmenu_systemId
        # url = 'http://' + self.url + '/sys/permission/page/list/delete/'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '删除组件菜单,正确'
        url_path = '/sys/permission/page/list/delete/'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
        # print(result_buginfo_template(case_section, url, request_method, deletemodelmenu_id + '?systemId=' + deletemodelmenu_systemId, r))
        # title = mail_buginfo_template(case_section, mail_title_url, request_method, deletemodelmenu_id + '?systemId=' + deletemodelmenu_systemId, r)[0]
        # content = mail_buginfo_template(case_section, mail_title_url, request_method, deletemodelmenu_id + '?systemId=' + deletemodelmenu_systemId, r)[1]
        print(result_buginfo_template(case_section, url, request_method,data,r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method,data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method,data, r)[1]
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
        log.info('删除组件菜单,正确')
        time.sleep(1)

    """
                     删除组件目录,正确
    """
    def test_delete_module_dir(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        deletemodeldir_id = self.cf.getini_by_option(self.case_paramt_ini, '删除组件目录,正确', 'id')
        deletemodeldir_systemId = self.cf.getini_by_option(self.case_paramt_ini, '删除组件目录,正确', 'systemId')
        data = self.cf.getini_by_section(self.case_paramt_ini, '删除组件目录,正确')
        data = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        ll = {}
        ll['systemId'] = json.loads(data)['systemId']
        data = str(ll)
        url = 'http://' + self.url + '/sys/permission/page/list/delete/' + deletemodeldir_id + '?systemId=' + deletemodeldir_systemId
        # url = 'http://' + self.url + '/sys/permission/page/list/delete/'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url, data,headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '删除组件目录,正确'
        url_path = '/sys/permission/page/list/delete/'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
        # print(result_buginfo_template(case_section, url, request_method,
        #                               deletemodeldir_id + '?systemId=' + deletemodeldir_systemId, r))
        # title = mail_buginfo_template(case_section, mail_title_url, request_method,
        #                               deletemodeldir_id + '?systemId=' + deletemodeldir_systemId, r)[0]
        # content = mail_buginfo_template(case_section, mail_title_url, request_method,
        #                                 deletemodeldir_id + '?systemId=' + deletemodeldir_systemId, r)[1]
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
        log.info('删除组件目录,正确')
        time.sleep(1)