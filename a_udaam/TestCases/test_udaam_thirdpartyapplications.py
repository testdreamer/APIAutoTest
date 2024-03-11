#-- coding: utf-8 --

#@Time : 2022/6/9 17:36

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : test_udaam_thirdpartyapplications.py

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
from Utils.operation_zentao_mysql import *
from Utils.all_style_template import *
from Utils.send_email import *
from Utils.encrypt import *
from Utils.currenttime import *
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
class ThirdPartyApplications(TestApi,Helper):
    # 获取服务器地址,,,
    url = read_yaml(sys.path[-1] + '/data/server_address.yaml', 'url')
    case_paramt_ini = sys.path[-1] + '/data/case_parameters.ini'
    cf = Conf
    '''
           新增第三方应用,正确
    '''
    def test_insert_third_part_app(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        #随机生成第三方应用名写到[新增第三方应用,正确]name和code中
        self.cf.put_ini(self.case_paramt_ini, '新增第三方应用,正确','name',str(get_time()))
        self.cf.put_ini(self.case_paramt_ini, '新增第三方应用,正确', 'code', str(get_time()))

        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '新增第三方应用,正确')
        data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true').replace('"false"','false')))
        # get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/threeAppInfo/manage/add'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '新增第三方应用,正确'
        url_path = '/sys/threeAppInfo/manage/add'
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
        #获取id写到[修改第三方应用,正确]的id中
        self.cf.put_ini(self.case_paramt_ini,'修改第三方应用,正确','id',r.json()['data'])
        # 获取id写到[删除第三方应用,正确]的id中
        self.cf.put_ini(self.case_paramt_ini, '删除第三方应用,正确', 'id', r.json()['data'])
        log.info('新增第三方应用,正确')
        time.sleep(1)

    '''
            查询第三方应用分类,正确
    '''
    def test_query_third_party_app_classifi(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '查询第三方应用分类,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/appInfo/loadAppTypeTree?'+get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        #获取[新增第三方应用,正确]的typeId值
        inserttr_typeid = self.cf.getini_by_option(self.case_paramt_ini,'新增第三方应用,正确','typeId')
        #获取[应用分类查询,正确]的pid值
        appcla_pid = self.cf.getini_by_option(self.case_paramt_ini, '应用分类查询,正确', 'pid')
        res = r.json()['code'] == 200 and r.json()['data'][0]['id'] == appcla_pid
        case_section = '查询第三方应用分类,正确'
        url_path = '/sys/appInfo/loadAppTypeTree'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data'][0]['id']],
                                      ['code=200',appcla_pid],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data'][0]['id'],appcla_pid)

        log.info('查询第三方应用分类,正确')
        time.sleep(1)

    '''
               查询第三方应用,正确
    '''
    def test_query_third_party_app(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '查询第三方应用,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/threeAppInfo/list?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)

        # 获取[新增第三方应用,正确]的typeId值
        inserttr_typeid = self.cf.getini_by_option(self.case_paramt_ini, '新增第三方应用,正确', 'typeId')
        # 获取[新增第三方应用,正确]的name值
        inserttr_name = self.cf.getini_by_option(self.case_paramt_ini, '新增第三方应用,正确', 'name')
        res = r.json()['code'] == 200 and r.json()['data']['content'][0]['typeId'] == inserttr_typeid and r.json()['data']['content'][0]['name'] == inserttr_name
        case_section = '查询第三方应用,正确'
        url_path = '/sys/threeAppInfo/list'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']), r.json()['data']['content'][0]['typeId'],r.json()['data']['content'][0]['name']],
                                      ['code=200', inserttr_typeid,inserttr_name],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data']['content'][0]['typeId'], inserttr_typeid)
        self.assertEqual(r.json()['data']['content'][0]['name'], inserttr_name)

        log.info('查询第三方应用,正确')
        time.sleep(1)



    '''
                   修改第三方应用,正确
    '''
    def test_update_third_party_app(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[新增第三方应用,正确]的typeId值
        inserttr_typeid = self.cf.getini_by_option(self.case_paramt_ini, '新增第三方应用,正确', 'typeId')
        # 获取[新增第三方应用,正确]的name值
        inserttr_name = self.cf.getini_by_option(self.case_paramt_ini, '新增第三方应用,正确', 'name')
        # 获取[新增第三方应用,正确]的supplierId值
        inserttr_supplierid = self.cf.getini_by_option(self.case_paramt_ini, '新增第三方应用,正确', 'supplierId')
        # 获取[新增第三方应用,正确]的code值
        inserttr_code = self.cf.getini_by_option(self.case_paramt_ini, '新增第三方应用,正确', 'code')


        # 将修改后的值写到ini文件的[修改第三方应用,正确]中
        self.cf.put_ini(self.case_paramt_ini, '修改第三方应用,正确', 'typeId', inserttr_typeid)
        self.cf.put_ini(self.case_paramt_ini, '修改第三方应用,正确', 'supplierId', inserttr_supplierid)
        self.cf.put_ini(self.case_paramt_ini, '修改第三方应用,正确', 'name', str(get_time()))
        self.cf.put_ini(self.case_paramt_ini, '修改第三方应用,正确', 'code', str(get_time()))
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '修改第三方应用,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('"false"',
                                                                                                     'false')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/threeAppInfo/thirdUpdate'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '修改第三方应用,正确'
        url_path = '/sys/threeAppInfo/thirdUpdate'
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
        log.info('修改第三方应用,正确')
        time.sleep(1)

    '''
            删除第三方应用,正确
    '''
    def test_delete_third_party_app(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_option(self.case_paramt_ini, '删除第三方应用,正确','id')
        # get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/threeAppInfo/manage/delete/'+data
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,{}, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '删除第三方应用,正确'
        url_path = '/sys/threeAppInfo/manage/delete/'
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
        log.info('删除第三方应用,正确')
        time.sleep(1)
