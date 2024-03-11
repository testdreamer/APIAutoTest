#-- coding: utf-8 --import sysimport requestsfrom Utils.page import *from Utils.dicttogetparameter import *from Basepage.unittestChushihua import TestApifrom Utils.operationyaml import *from Utils.operationini import Conffrom Utils.operationini import *from Utils.log import *from Utils.operation_zentao_mysql import *from Utils.send_email import *from Utils.currenttime import *from Utils.all_style_template import *import jsonfrom Utils.encrypt import *from Utils.currenttime import *import sys,ossys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))class Test_system_setting(TestApi,Helper):    # 获取服务器地址,,,    url = read_yaml(sys.path[-1] + '/data/server_address.yaml', 'url')    case_paramt_ini = sys.path[-1] + '/data/case_parameters.ini'    cf = Conf    #基础设置查询，正确    def test_system_settting_search_right(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        # print(self.case_paramt_ini)        data = self.cf.getini_by_section(self.case_paramt_ini, '基础设置查询,正确')        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))        get_parameter = dict_to_get_parameter(data)        url = 'http://' + self.url + '/sys/dictData/page/findAllByTypeCode?' + get_parameter        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token        }        r = self.get(url, headers)        log.info(r.text)        exp_createusername = "admin"        res = r.json()['code'] == 200 and r.json()['data'][1]['createUserName'] == exp_createusername        case_section = '基础设置查询,正确'        url_path = '/sys/dictData/page/findAllByTypeCode'        mail_title_url = 'http://' + self.url + url_path        request_method = 'get'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code']),r.json()['data'][1]['createUserName']],                                      ['code=200',exp_createusername],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        self.assertEqual(r.json()['data'][1]['createUserName'], exp_createusername)        # 基础设置查询，错误    def test_system_settting_search_wrong(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        # print(self.case_paramt_ini)        data = self.cf.getini_by_section(self.case_paramt_ini, '基础设置查询,错误')        # data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))        get_parameter = dict_to_get_parameter(data)        url = 'http://' + self.url + '/sys/dictData/page/findAllByTypeCode?' + get_parameter        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token        }        r = self.get(url, headers)        log.info(r.text)        exp_data = []        res = r.json()['code'] == 200 and r.json()['data'] == exp_data        case_section = '基础设置查询,错误'        url_path = '/sys/dictData/page/findAllByTypeCode'        mail_title_url = 'http://' + self.url + url_path        request_method = 'get'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code']), r.json()['data']],                                      ['code=200', exp_data],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        self.assertEqual(r.json()['data'], exp_data)    #基础设置修改，正确    def test_system_settting_update_right(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        # print(self.case_paramt_ini)        data = self.cf.getini_by_section(self.case_paramt_ini, '基础设置修改,正确')        data1 = json.dumps(json.loads('['+str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')+']'))        get_parameter = dict_to_get_parameter(data)        url = 'http://' + self.url + '/sys/dictData/page/list/batchSaveDictData'        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token        }        r = self.post(url,data1, headers)        log.info(r.text)        res = r.json()['code'] == 200        case_section = '基础设置修改,正确'        url_path = '/sys/dictData/page/list/batchSaveDictData'        mail_title_url = 'http://' + self.url + url_path        request_method = 'post'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code'])],                                      ['code=200'],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        # self.assertEqual(r.json()['data'], [])    #基础设置修改，错误    def test_system_settting_update_wrong1(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        # print(self.case_paramt_ini)        data = self.cf.getini_by_section(self.case_paramt_ini, '基础设置修改,错误')        data1 = json.dumps(json.loads('['+str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')+']'))        get_parameter = dict_to_get_parameter(data)        url = 'http://' + self.url + '/sys/dictData/page/list/batchSaveDictData'        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token        }        r = self.post(url,data1, headers)        log.info(r.text)        exp_mes = "字典名称不存在"        res = r.json()['code'] == 101102 and r.json()['message'] == exp_mes        case_section = '基础设置修改,错误'        url_path = '/sys/dictData/page/list/batchSaveDictData'        mail_title_url = 'http://' + self.url + url_path        request_method = 'post'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code']),r.json()['message']],                                      ['code=101102',exp_mes],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 101102)        self.assertEqual(r.json()['message'], exp_mes)        # self.assertEqual(r.json()['data'], [])    #基础设置修改，未传    def test_system_settting_update_wrongkey(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        data = self.cf.getini_by_section(self.case_paramt_ini, '基础设置修改,未传')        data1 = json.dumps(json.loads('['+str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')+']'))        get_parameter = dict_to_get_parameter(data)        url = 'http://' + self.url + '/sys/dictData/page/list/batchSaveDictData'        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token        }        r = self.post(url,data1, headers)        log.info(r.text)        res = r.json()['code'] == 200        case_section = '基础设置修改,未传'        url_path = '/sys/dictData/page/list/batchSaveDictData'        mail_title_url = 'http://' + self.url + url_path        request_method = 'post'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code'])],                                      ['code=200'],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], "成功")        # self.assertEqual(r.json()['data'], [])    #基础设置修改，字典类型错误值    def test_system_settting_update_wrongkey1(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        data = self.cf.getini_by_section(self.case_paramt_ini, '基础设置修改,字典类型错误值')        data1 = json.dumps(json.loads('['+str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')+']'))        get_parameter = dict_to_get_parameter(data)        url = 'http://' + self.url + '/sys/dictData/page/list/batchSaveDictData'        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token        }        r = self.post(url,data1, headers)        log.info(r.text)        exp_mes = '字典类型错误'        res = r.json()['code'] == 101104 and r.json()['message'] == exp_mes        case_section = '基础设置修改,字典类型错误值'        url_path = '/sys/dictData/page/list/batchSaveDictData'        mail_title_url = 'http://' + self.url + url_path        request_method = 'post'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code']),r.json()['message']],                                      ['code=101104',exp_mes],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 101104)        self.assertEqual(r.json()['message'], exp_mes)        # self.assertEqual(r.json()['data'], [])