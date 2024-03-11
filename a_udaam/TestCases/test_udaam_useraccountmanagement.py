#-- coding: utf-8 --

#@Time : 2022/6/13 20:11

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : test_udaam_useraccountmanagement.py

#@Software: PyCharm
from Utils.page import *
from Utils.dicttogetparameter import *
from Basepage.unittestChushihua import TestApi
from Utils.operationyaml import *
from Utils.operationini import Conf
from Utils.operationini import *
from Utils.log import *
from Utils.send_email import *
from Utils.operation_zentao_mysql import *
import json
from Utils.encrypt import *
from Utils.currenttime import *
from Utils.all_style_template import *
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
class UserAccountManagement(TestApi,Helper):
    # 获取服务器地址,,,
    url = read_yaml(sys.path[-1] + '/data/server_address.yaml', 'url')
    case_paramt_ini = sys.path[-1] + '/data/case_parameters.ini'
    cf = Conf
    '''
            人员条件查询-按用户名,正确
            '''

    def test_selectusercondition_byname(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员条件查询-按用户名,正确')
        data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/account/page/findUserList?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        # 获取[创建人员信息,正确]的username,idCard进行校验
        insertuser_name = self.cf.getini_by_option(self.case_paramt_ini, '创建人员信息,正确', 'username')
        insertuser_idcard = self.cf.getini_by_option(self.case_paramt_ini, '创建人员信息,正确', 'idCard')
        res = r.json()['code'] == 200 and r.json()['data']['content'][0]['username']==insertuser_name and r.json()['data']['content'][0]['idCard']==insertuser_idcard
        case_section = '人员条件查询-按用户名,正确'
        url_path = '/sys/account/page/findUserList'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data']['content'][0]['username'],r.json()['data']['content'][0]['idCard']],
                                      ['code=200',insertuser_name,insertuser_idcard],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data']['content'][0]['username'], insertuser_name)
        self.assertEqual(r.json()['data']['content'][0]['idCard'], insertuser_idcard)
        #将userId值写到[账号新增,正确]的userId中
        self.cf.put_ini(self.case_paramt_ini,'账号新增,正确','userId',r.json()['data']['content'][0]['userId'])
        log.info('人员条件查询-按用户名,正确')
        time.sleep(1)

    '''
    账号新增,正确
    '''
    def test_insert_username(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        self.cf.put_ini(self.case_paramt_ini, '账号新增,正确', 'accountName', str(get_time()))
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '账号新增,正确')
        data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/account/page/list/addAccount'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+token
        }
        r = self.post(url,data1,headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '账号新增,正确'
        url_path = '/sys/account/page/list/addAccount'
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
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['message'], '成功')
        log.info('账号新增,正确')
        time.sleep(1)

    '''
        账号查询-按用户名,正确
        '''

    def test_select_account(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '账号查询-按用户名,正确')
        data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/account/page/findUserAccount?'+get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        # 获取[创建人员信息,正确]的username,idCard进行校验
        insertuser_name = self.cf.getini_by_option(self.case_paramt_ini, '创建人员信息,正确', 'username')
        insertuser_idcard = self.cf.getini_by_option(self.case_paramt_ini, '创建人员信息,正确', 'idCard')
        res = r.json()['code'] == 200 and r.json()['data']['content'][0]['userName']==insertuser_name and r.json()['data']['content'][0]['idCard']==insertuser_idcard
        case_section = '账号查询-按用户名,正确'
        url_path = '/sys/account/page/findUserAccount'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data']['content'][0]['userName'],r.json()['data']['content'][0]['idCard']],
                                      ['code=200',insertuser_name,insertuser_idcard],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data']['content'][0]['userName'],insertuser_name)
        self.assertEqual(r.json()['data']['content'][0]['idCard'], insertuser_idcard)
        self.cf.put_ini(self.case_paramt_ini,'修改账号,正确','userAccountId',
                        r.json()['data']['content'][0]['userAccountId'])
        self.cf.put_ini(self.case_paramt_ini, '修改账号,正确', 'userId',
                        r.json()['data']['content'][0]['userId'])
        self.cf.put_ini(self.case_paramt_ini, '修改账号,正确', 'accountId',
                        r.json()['data']['content'][0]['accountId'])
        self.cf.put_ini(self.case_paramt_ini, '重置密码,正确', 'id',
                        r.json()['data']['content'][0]['accountId'])
        self.cf.put_ini(self.case_paramt_ini, '账号禁用,正确', 'accountId',
                        r.json()['data']['content'][0]['accountId'])
        self.cf.put_ini(self.case_paramt_ini, '账号启用,正确', 'accountId',
                        r.json()['data']['content'][0]['accountId'])
        self.cf.put_ini(self.case_paramt_ini, '账号锁定,正确', 'accountId',
                        r.json()['data']['content'][0]['accountId'])
        self.cf.put_ini(self.case_paramt_ini, '删除用户账号,正确', 'userId',
                        r.json()['data']['content'][0]['userId'])
        self.cf.put_ini(self.case_paramt_ini, '删除用户账号,正确', 'accountId',
                        r.json()['data']['content'][0]['accountId'])
        self.cf.put_ini(self.case_paramt_ini, '账号详情,正确', 'userId',
                        r.json()['data']['content'][0]['userId'])
        log.info('账号查询-按用户名,正确')
        time.sleep(1)

    '''
           2022-08-12新增
            账号详情,正确
     '''

    def test_account_details(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '账号详情,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/account/page/detail?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        # 获取[创建人员信息,正确]的username进行校验
        insertuser_name = self.cf.getini_by_option(self.case_paramt_ini, '创建人员信息,正确', 'username')
        res = r.json()['code'] == 200 and r.json()['data']['userName'] == insertuser_name
        case_section = '账号详情,正确'
        url_path = '/sys/account/page/detail'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']), r.json()['data']['userName']],
                                      ['code=200', insertuser_name],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data']['userName'], insertuser_name)
        log.info('账号详情,正确')
        time.sleep(1)

    '''
               2022-08-12新增
                账号禁用,正确
         '''

    def test_account_stop(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '账号禁用,正确')
        data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/account/page/list/updateAccountEnable'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '账号禁用,正确'
        url_path = '/sys/account/page/list/updateAccountEnable'
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
        log.info('账号禁用,正确')
        time.sleep(1)

    '''
                   2022-08-12新增
                    账号启用,正确
             '''

    def test_account_start(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '账号启用,正确')
        data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/account/page/list/updateAccountEnable'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url, data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '账号启用,正确'
        url_path = '/sys/account/page/list/updateAccountEnable'
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
        log.info('账号启用,正确')
        time.sleep(1)

    '''
                       2022-08-12新增
                        账号锁定,正确
     '''

    def test_account_lock(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '账号锁定,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/account/page/list/updateLockedUserPwd?'+ get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url, {}, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '账号锁定,正确'
        url_path = '/sys/account/page/list/updateLockedUserPwd'
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
        log.info('账号锁定,正确')
        time.sleep(1)

    '''
            修改账号,正确
            '''

    def test_update_account(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        #获取[ 账号新增,正确]的accountName值进行修改
        insertuser_accountname = self.cf.getini_by_option(self.case_paramt_ini,'账号新增,正确','accountName')
        #将accountName值进行修改后写到[修改账号,正确]的accountName中
        self.cf.put_ini(self.case_paramt_ini,'修改账号,正确','accountName',insertuser_accountname+'up')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '修改账号,正确')
        data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/account/page/list/updateAccount'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url, data1,headers)
        log.info(r.text)

        #校验是否修改成功
        url = 'http://' + self.url + '/sys/account/page/findUserAccount?accountName=&uName=&idCard=&phone=&email=&enabled=&pageNum=1&pageSize=10'
        r_as = self.get(url, headers)
        #获取[修改账号,正确]的accountName值进行校验
        updateaccount_accountname = self.cf.getini_by_option(self.case_paramt_ini,'修改账号,正确','accountName')
        res = r.json()['code'] == 200 and r_as.json()['data']['content'][0]['accountName']==updateaccount_accountname
        case_section = '修改账号,正确'
        url_path = '/sys/account/page/list/updateAccount'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r_as.json()['data']['content'][0]['accountName']],
                                      ['code=200',updateaccount_accountname],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r_as.json()['data']['content'][0]['accountName'],updateaccount_accountname)
        log.info('修改账号,正确')
        time.sleep(1)

    '''
                重置密码,正确
                '''

    def test_reset_password(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        para = self.cf.getini_by_option(self.case_paramt_ini,'重置密码,正确','id')
        url = 'http://' + self.url + '/sys/account/page/'+ para
        data = {}
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data,headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '重置密码,正确'
        url_path = '/sys/account/page/'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, para, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, para, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, para, r)[1]
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
        log.info('重置密码,正确')
        time.sleep(1)

    '''
                    删除用户账号,正确
                    '''

    def test_delete_useraccount(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        para = self.cf.getini_by_option(self.case_paramt_ini, '删除用户账号,正确', 'accountId')
        # data = self.cf.getini_by_section(self.case_paramt_ini, '删除用户账号,正确')
        data = {'userId': 'null'}
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/account/page/list/deleteAccount/' + para
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '删除用户账号,正确'
        url_path = '/sys/account/page/list/deleteAccount/'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, para, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, para, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, para, r)[1]
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
        log.info('删除用户账号,正确')
        time.sleep(1)
