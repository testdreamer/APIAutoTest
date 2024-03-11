#-- coding: utf-8 --

#@Time : 2022/6/9 10:50

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : test_udaam_internalapplication.py

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
from Utils.all_style_template import *
from Utils.encrypt import *
from Utils.currenttime import *
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
class InternalApplication(TestApi,Helper):
    # 获取服务器地址,,,
    url = read_yaml(sys.path[-1] + '/data/server_address.yaml', 'url')
    case_paramt_ini = sys.path[-1] + '/data/case_parameters.ini'
    cf = Conf
    '''
           资源发现,正确
    '''
    def test_resource_discovery(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '资源发现,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/system/getServiceResource?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '资源发现,正确'
        url_path = '/sys/system/getServiceResource'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, get_parameter, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, get_parameter, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, get_parameter, r)[1]
        bug_to_zentao(res, title, content, 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=200'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['message'], '成功')
        self.assertTrue(res)
        log.info('资源发现,正确')
        time.sleep(1)

    '''
               新增内部应用,正确
        '''

    def test_insert_internal_app(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        #随机生成内部应用name和code写到[新增内部应用,正确]name和code中
        self.cf.put_ini(self.case_paramt_ini, '新增内部应用,正确', 'name', str(get_time()))
        self.cf.put_ini(self.case_paramt_ini, '新增内部应用,正确', 'code', str(get_time()))

        #获取系统资源id写到[资源发现,正确]resourceIdList中
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url = 'http://' + self.url + '/sys/poolResource/page/findAll'
        r = self.get(url, headers)
        log.info('dffffff' + r.text)
        sources = []
        for i in range(len(r.json()['data'][4]['children'])):
            sources.append(r.json()['data'][4]['children'][i]['id'])
        sources_up = str(sources).replace("'","\"")
        self.cf.put_ini(self.case_paramt_ini, '新增内部应用,正确','resourceIdList',sources_up)
        #获取应用分类树id写到[新增内部应用,正确]typeId中
        url = 'http://' + self.url + '/sys/appType/loadAppTypeTree'
        r = self.get(url, headers)
        self.cf.put_ini(self.case_paramt_ini, '新增内部应用,正确','typeId',r.json()['data'][0]['id'])
        #获取厂商id写到[新增内部应用,正确]supplierId中
        url = 'http://' + self.url + '/sys/threeAppInfo/findAllSupplier'
        r = self.get(url, headers)

        self.cf.put_ini(self.case_paramt_ini, '新增内部应用,正确','supplierId',r.json()['data'][0]['id'])

        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '新增内部应用,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'[", "[").replace("]'", "]").replace("'", "\"").replace('"null"', 'null').replace(
                '"true"', 'true').replace('userType": "0"', 'userType": 0')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/appInfo/manage/add'
        r_insert = self.post(url, data1,headers)
        log.info(r.text)
        res = r_insert.json()['code'] == 200
        case_section = '新增内部应用,正确'
        url_path = '/sys/appInfo/manage/add'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, get_parameter, r_insert))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, get_parameter, r_insert)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, get_parameter, r_insert)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r_insert.json()['code'])],
                                      ['code=200'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r_insert.json()['message'], '成功')
        self.assertTrue(res)

        self.cf.put_ini(self.case_paramt_ini, '查询内部应用详情,正确','id',r_insert.json()['data'])
        self.cf.put_ini(self.case_paramt_ini, '查询内部应用修改,正确', 'id', r_insert.json()['data'])
        self.cf.put_ini(self.case_paramt_ini, '内部应用删除,正确', 'id', r_insert.json()['data'])

        log.info('资源发现,正确')
        time.sleep(1)

    '''
            查询内部应用详情,正确
    '''
    def test_internalapp_Info(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_option(self.case_paramt_ini, '查询内部应用详情,正确','id')
        url = 'http://' + self.url + '/sys/appInfo/'+data
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        #获取[新增内部应用,正确]的name和code进行校验
        insert_name = self.cf.getini_by_option(self.case_paramt_ini, '新增内部应用,正确','name')
        insert_code = self.cf.getini_by_option(self.case_paramt_ini, '新增内部应用,正确', 'code')

        res = r.json()['data']['code'] == insert_code and r.json()['data']['name'] == insert_name and r.json()['code'] == 200
        case_section = '查询内部应用详情,正确'
        url_path = '/sys/appInfo/'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data']['code'],r.json()['data']['name']],
                                      ['code=200',insert_code,insert_name],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['message'], '成功')
        self.assertTrue(res)


        log.info('查询内部应用详情,正确')
        time.sleep(1)

    '''
                查询内部应用修改,正确
    '''
    def test_internalapp_update(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 随机生成内部应用name和code写到[查询内部应用修改,正确]name和code中
        self.cf.put_ini(self.case_paramt_ini, '查询内部应用修改,正确', 'name', str(get_time()))
        self.cf.put_ini(self.case_paramt_ini, '查询内部应用修改,正确', 'code', str(get_time()))

        # 获取系统资源id写到[查询内部应用修改,正确]resourceIdList中
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        url = 'http://' + self.url + '/sys/poolResource/page/findAll'
        r = self.get(url, headers)
        sources = []
        for i in range(len(r.json()['data'][0]['children'])):
            sources.append(r.json()['data'][0]['children'][i]['id'])
        sources_up = str(sources).replace("'", "\"")
        self.cf.put_ini(self.case_paramt_ini, '查询内部应用修改,正确', 'resourceIdList', sources_up)

        # 获取应用分类树id写到[查询内部应用修改,正确]typeId中
        url = 'http://' + self.url + '/sys/appType/loadAppTypeTree'
        r = self.get(url, headers)
        self.cf.put_ini(self.case_paramt_ini, '查询内部应用修改,正确', 'typeId', r.json()['data'][1]['id'])

        # 获取厂商id写到[查询内部应用修改,正确]supplierId中
        url = 'http://' + self.url + '/sys/threeAppInfo/findAllSupplier'
        r = self.get(url, headers)
        self.cf.put_ini(self.case_paramt_ini, '查询内部应用修改,正确', 'supplierId', r.json()['data'][1]['id'])

        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '查询内部应用修改,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'[", "[").replace("]'", "]").replace("'", "\"").replace('"null"', 'null').replace(
                '"true"', 'true').replace('userType": "0"', 'userType": 0')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/appInfo/manage/update'
        r = self.post(url,data1, headers)
        log.info(r.text)
        res =  r.json()['code'] == 200
        case_section = '查询内部应用修改,正确'
        url_path = '/sys/appInfo/manage/update'
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
        self.assertEqual(r.json()['message'], '成功')
        self.assertTrue(res)

        log.info('查询内部应用修改,正确')
        time.sleep(1)


    '''
                    多机构应用-应用列表,正确
    '''
    def test_many_institutions_app_list(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '多机构应用-应用列表,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/appInfo/manyOrgList?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '多机构应用-应用列表,正确'
        url_path = '/sys/appInfo/manyOrgList'
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
        self.assertEqual(r.json()['message'], '成功')
        self.assertTrue(res)
        # sources = []
        # for i in range(len(r.json()['data'])):
        #     sources.append(r.json()['data'][i]['name'])
        # print(sources)
        # self.assertTrue(
        #                 '危急值管理系统' in sources and
        #                 '危急值管理系统321' in sources and
        #                 '危急值管理系统111' in sources and
        #                 '危急值管理系统555' in sources and
        #                 '危急值管理系统2' in sources and
        #                 '危急值管理系统1' in sources and
        #                 '删除报错' in sources
        #                 )
        log.info('多机构应用-应用列表,正确')
        time.sleep(1)

    '''
                多机构应用-机构列表,正确
    '''
    def test_many_org_list(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '多机构应用-机构列表,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/appInfo/orgList?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '多机构应用-机构列表,正确'
        url_path = '/sys/appInfo/orgList'
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
        self.assertTrue(res)
        self.assertEqual(r.json()['message'], '成功')
        # sources = []
        # for i in range(len(r.json()['data']['content'])):
        #     sources.append(r.json()['data']['content'][i]['name'])
        # print(sources)
        # self.assertTrue(
        #
        #                 '测试机构' in sources and
        #                 '龙岗人民医院' in sources and
        #                 '龙岗人民医院' in sources and
        #                 '龙岗人民医院' in sources
        #                 )
        log.info('多机构应用-机构列表,正确')
        time.sleep(1)

    '''
                 内部应用删除,正确
        '''

    def test_internal_app_delete(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_option(self.case_paramt_ini, '内部应用删除,正确', 'id')
        url = 'http://' + self.url + '/sys/appInfo/manage/delete/' + data
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,{}, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '内部应用删除,正确'
        url_path = '/sys/appInfo/manage/delete/'
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
        self.assertTrue(res)
        self.assertEqual(r.json()['message'], '成功')
        log.info('内部应用删除,正确')
        time.sleep(1)
