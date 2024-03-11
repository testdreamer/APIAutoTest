#-- coding: utf-8 --

#@Time : 2022/11/23 11:02

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : test_basic_info_query.py

#@Software: PyCharm
from Utils.page import *
import jsonpath
from Utils.dicttogetparameter import *
from Basepage.unittestChushihua import TestApi
from Utils.operationyaml import *
from Utils.operationini import Conf
from Utils.operationini import *
from Utils.log import *
from Utils.currenttime import *
import json
from Utils.send_email import *
from Utils.encrypt import *
from Utils.currenttime import *
from Utils.connectMysql import ConnectMysql
from Utils.operation_zentao_mysql import *
from Utils.all_style_template import *
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
class BasicInfoQuery(TestApi,Helper):
    # 获取服务器地址,,,
    url = read_yaml(sys.path[-1] + '/data/server_address.yaml', 'url')
    case_paramt_yaml = sys.path[-1] + '/data/case_parameters.yaml'
    mail_config = sys.path[-1] + '/data/mail_config.yaml'
    zentao_bug_commit = read_yaml(mail_config, 'zentao_bug_commit')
    zentao_bug_assign = read_yaml(mail_config, 'zentao_bug_assign')
    bug_mail_addressee = read_yaml(mail_config, 'bug_mail_addressee')
    bug_mail_cc = read_yaml(mail_config, 'bug_mail_cc')

    cf = Conf
    '''
           CSAM医院信息查询,正确
    '''
    def test_hospital_info_query(self):
        # 获取ini中用例
        para_dict = read_yaml_no_key(self.case_paramt_yaml)['CSAM医院信息查询,正确']
        data = json.dumps(json.loads(str(para_dict).replace('None','""').replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        url_path = '/csam-service-bpma/webapi?m=HB001&un=chppwechat&uk=636870702d7765636861742d323031393033'
        url = 'https://' + self.url + url_path
        headers = {'Content-Type': 'application/json'}
        r = self.post(url,data, headers)
        log.info(r.text)

        sources = []
        for i in range(len(r.json()['result']['data'])):
            sources.append(r.json()['result']['data'][i]['orgId'])
        org_id = [20,21,101,103,283]
        res = r.json()['code'] == '000000' and set(org_id) <= set(sources)

        case_section = '[接口自动化bug] ' + '-号源池 ' +'CSAM医院信息查询,正确'
        mail_title_url = 'https://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'', '').replace('"', ''), self.zentao_bug_assign, self.zentao_bug_commit)
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']), sources],
                                      ['code=000000', org_id],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email(self.bug_mail_addressee, title_mail, mail_temp,self.bug_mail_cc)
        self.assertTrue(res)
        if 582 in sources:
            # 将orgId写到[CSAM科室信息查询,正确][CSAM排班信息查询,正确]orgId中
            case = read_yaml_no_key(self.case_paramt_yaml)
            case['CSAM科室信息查询,正确']['orgId'] = 582
            case['CSAM排班信息查询,正确']['orgId'] = 582
            case['CSAM全院科室排班信息查询,正确']['orgId'] = 582
            case['CSAM号源信息查询,正确']['orgId'] = 582
            case['CSAM预约申请,正确']['orgId'] = 582
            case['CSAM预约订单取消,正确']['orgId'] = 582
            case['CSAM医生预约订单查询,正确']['orgId'] = 582

            write_yaml(self.case_paramt_yaml,case)
        log.info('CSAM医院信息查询,正确')
        time.sleep(1)



    '''
           CSAM科室信息查询,正确
    '''
    def test_departments_info_query(self):
        # 获取ini中用例
        para_dict = read_yaml_no_key(self.case_paramt_yaml)['CSAM科室信息查询,正确']
        data = json.dumps(json.loads(str(para_dict).replace('None','""').replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        url_path = '/csam-service-bpma/webapi?m=HB002&un=chppwechat&uk=636870702d7765636861742d323031393033'
        url = 'https://' + self.url + url_path
        headers = {'Content-Type': 'application/json'}
        r = self.post(url,data, headers)
        log.info(r.text)
        # json_res = jsonpath.jsonpath(r.json(), '$.result.data[?(@.deptId==660)]')
        # print(json_res)
        sources = []
        for i in range(len(r.json()['result']['data'])):
            sources.append(r.json()['result']['data'][i]['deptId'])
        org_id = [646,655,759,762,786]
        res = r.json()['code'] == '000000' and set(org_id) <= set(sources)
        print(res)
        case_section = '[接口自动化bug] ' + '-号源池 ' +'CSAM科室信息查询,正确'
        mail_title_url = 'https://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'', '').replace('"', ''), self.zentao_bug_assign, self.zentao_bug_commit)
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']), sources],
                                      ['code=000000', org_id],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email(self.bug_mail_addressee, title_mail, mail_temp,self.bug_mail_cc)
        self.assertTrue(res)
        if 660 in sources:
            # 将orgId写到[CSAM科室信息查询,正确]orgId中
            case = read_yaml_no_key(self.case_paramt_yaml)
            case['CSAM排班信息查询,正确']['deptId'] = 660
            case['CSAM号源信息查询,正确']['deptId'] = 660
            case['CSAM预约申请,正确']['deptId'] = 660
            case['CSAM预约订单取消,正确']['orgDeptId'] = 660
            case['CSAM医生预约订单查询,正确']['deptId'] = 660

            write_yaml(self.case_paramt_yaml, case)
        log.info('CSAM科室信息查询,正确')
        time.sleep(1)

    '''
                   CSAM科室信息查询,orgId必填项为空
            '''

    def test_departments_info_query_orgid_empty(self):
        # 获取ini中用例
        para_dict = read_yaml_no_key(self.case_paramt_yaml)['CSAM科室信息查询,orgId必填项为空']
        data = json.dumps(json.loads(
            str(para_dict).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace('"true"',
                                                                                                      'true')))
        url_path = '/csam-service-bpma/webapi?m=HB002&un=chppwechat&uk=636870702d7765636861742d323031393033'
        url = 'https://' + self.url + url_path
        headers = {'Content-Type': 'application/json'}
        r = self.post(url, data, headers)
        log.info(r.text)
        res = r.json()['code'] != '000000'

        case_section = '[接口自动化bug] ' + '-号源池 ' + 'CSAM科室信息查询,orgId必填项为空'
        mail_title_url = 'https://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'', '').replace('"', ''), self.zentao_bug_assign,
                      self.zentao_bug_commit)
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=000000'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email(self.bug_mail_addressee, title_mail, mail_temp, self.bug_mail_cc)
        self.assertTrue(res)
        log.info('CSAM科室信息查询,orgId必填项为空')
        time.sleep(1)

    '''
                       CSAM科室信息查询,orgId为0（全局科室)
                '''

    def test_departments_info_query_orgid_zero(self):
        # 获取ini中用例
        para_dict = read_yaml_no_key(self.case_paramt_yaml)['CSAM科室信息查询,orgId为0（全局科室)']
        data = json.dumps(json.loads(
            str(para_dict).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace('"true"',
                                                                                                      'true')))
        url_path = '/csam-service-bpma/webapi?m=HB002&un=chppwechat&uk=636870702d7765636861742d323031393033'
        url = 'https://' + self.url + url_path
        headers = {'Content-Type': 'application/json'}
        r = self.post(url, data, headers)
        log.info(r.text)
        len_asser= r.json()['result']['dataLen'] == 448
        res = r.json()['code'] == '000000' and len_asser

        case_section = '[接口自动化bug] ' + '-号源池 ' + 'CSAM科室信息查询,orgId为0（全局科室)'
        mail_title_url = 'https://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'', '').replace('"', ''), self.zentao_bug_assign,
                      self.zentao_bug_commit)
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['result']['dataLen']],
                                      ['code=000000',448],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email(self.bug_mail_addressee, title_mail, mail_temp, self.bug_mail_cc)
        self.assertTrue(res)
        self.assertTrue(len_asser,'dataLen字段不正确')
        log.info('CSAM科室信息查询,orgId为0（全局科室)')
        time.sleep(1)

    '''
                           CSAM科室信息查询,123为不存在的医院ID
                    '''

    def test_departments_info_query_orgid_error(self):
        # 获取ini中用例
        para_dict = read_yaml_no_key(self.case_paramt_yaml)['CSAM科室信息查询,123为不存在的医院ID']
        data = json.dumps(json.loads(
            str(para_dict).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace('"true"',
                                                                                                      'true')))
        url_path = '/csam-service-bpma/webapi?m=HB002&un=chppwechat&uk=636870702d7765636861742d323031393033'
        url = 'https://' + self.url + url_path
        headers = {'Content-Type': 'application/json'}
        r = self.post(url, data, headers)
        log.info(r.text)
        len_asser = r.json()['result']['dataLen'] == 0
        res = r.json()['code'] == '000000' and len_asser

        case_section = '[接口自动化bug] ' + '-号源池 ' + 'CSAM科室信息查询,123为不存在的医院ID'
        mail_title_url = 'https://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'', '').replace('"', ''), self.zentao_bug_assign,
                      self.zentao_bug_commit)
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']), r.json()['result']['dataLen']],
                                      ['code=000000', 0],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email(self.bug_mail_addressee, title_mail, mail_temp, self.bug_mail_cc)
        self.assertTrue(res)
        self.assertTrue(len_asser, 'dataLen字段不正确')
        log.info('CSAM科室信息查询,123为不存在的医院ID')
        time.sleep(1)

    '''
                               CSAM科室信息查询,660为中医科,orgId必填项为空
                        '''

    def test_departments_info_query_orgid_empty_deptid_correct(self):
        # 获取ini中用例
        para_dict = read_yaml_no_key(self.case_paramt_yaml)['CSAM科室信息查询,660为中医科,orgId必填项为空']
        data = json.dumps(json.loads(
            str(para_dict).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace('"true"',
                                                                                                      'true')))
        url_path = '/csam-service-bpma/webapi?m=HB002&un=chppwechat&uk=636870702d7765636861742d323031393033'
        url = 'https://' + self.url + url_path
        headers = {'Content-Type': 'application/json'}
        r = self.post(url, data, headers)
        log.info(r.text)
        # len_asser = r.json()['result']['dataLen'] == 0
        res = r.json()['code'] != '000000'

        case_section = '[接口自动化bug] ' + '-号源池 ' + 'CSAM科室信息查询,660为中医科,orgId必填项为空'
        mail_title_url = 'https://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'', '').replace('"', ''), self.zentao_bug_assign,
                      self.zentao_bug_commit)
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code'])],
                                      ['code=000000'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email(self.bug_mail_addressee, title_mail, mail_temp, self.bug_mail_cc)
        self.assertTrue(res)
        log.info('CSAM科室信息查询,660为中医科,orgId必填项为空')
        time.sleep(1)

    '''
            CSAM科室信息查询,582为龙岗人民医院ID,660为中医科
    '''
    def test_departments_info_query_orgid_empty_deptid_longgangrenminhospital(self):
        # 获取ini中用例
        para_dict = read_yaml_no_key(self.case_paramt_yaml)['CSAM科室信息查询,582为龙岗人民医院ID,660为中医科']
        data = json.dumps(json.loads(
            str(para_dict).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace('"true"',
                                                                                                      'true')))
        url_path = '/csam-service-bpma/webapi?m=HB002&un=chppwechat&uk=636870702d7765636861742d323031393033'
        url = 'https://' + self.url + url_path
        headers = {'Content-Type': 'application/json'}
        r = self.post(url, data, headers)
        log.info(r.text)
        deptname = r.json()['result']['data'][0]['deptName'] == '中医科'
        res = r.json()['code'] == '000000' and deptname
        case_section = '[接口自动化bug] ' + '-号源池 ' + 'CSAM科室信息查询,582为龙岗人民医院ID,660为中医科'
        mail_title_url = 'https://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'', '').replace('"', ''), self.zentao_bug_assign,
                      self.zentao_bug_commit)
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['result']['data'][0]['deptName']],
                                      ['code=000000','中医科'],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email(self.bug_mail_addressee, title_mail, mail_temp, self.bug_mail_cc)
        self.assertTrue(res)
        self.assertTrue(deptname,'deptName不是中医科')
        log.info('CSAM科室信息查询,582为龙岗人民医院ID,660为中医科')
        time.sleep(1)

    '''
                CSAM科室信息查询,orgId必填项为-1
        '''

    def test_departments_info_query_orgid_minus(self):
        # 获取ini中用例
        para_dict = read_yaml_no_key(self.case_paramt_yaml)['CSAM科室信息查询,orgId必填项为-1']
        data = json.dumps(json.loads(
            str(para_dict).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace('"true"',
                                                                                                      'true')))
        url_path = '/csam-service-bpma/webapi?m=HB002&un=chppwechat&uk=636870702d7765636861742d323031393033'
        url = 'https://' + self.url + url_path
        headers = {'Content-Type': 'application/json'}
        r = self.post(url, data, headers)
        log.info(r.text)
        len_asser = r.json()['result']['dataLen'] == 0
        res = r.json()['code'] == '000000' and len_asser

        case_section = '[接口自动化bug] ' + '-号源池 ' + 'CSAM科室信息查询,orgId必填项为-1'
        mail_title_url = 'https://' + self.url + url_path
        request_method = 'post'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'', '').replace('"', ''), self.zentao_bug_assign,
                      self.zentao_bug_commit)
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['result']['dataLen']],
                                      ['code=000000',0],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email(self.bug_mail_addressee, title_mail, mail_temp, self.bug_mail_cc)
        self.assertTrue(res)
        self.assertTrue(len_asser,'返回值不是空值')
        log.info('CSAM科室信息查询,orgId必填项为-1')
        time.sleep(1)

    '''
                CSAM科室信息查询,orgId必填项超长
        '''

    def test_departments_info_query_orgid_overlength(self):
        # 获取ini中用例
        para_dict = read_yaml_no_key(self.case_paramt_yaml)['CSAM科室信息查询,orgId必填项超长']
        data = json.dumps(json.loads(
            str(para_dict).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace('"true"',
                                                                                                      'true')))
        url_path = '/csam-service-bpma/webapi?m=HB002&un=chppwechat&uk=636870702d7765636861742d323031393033'
        url = 'https://' + self.url + url_path
        headers = {'Content-Type': 'application/json'}
        r = self.post(url, data, headers)
        log.info(r.text)
        len_asser = r.json()['result']['dataLen'] == 0
        # print(r.json()['code'])
        # res = r.json()['code'] == '000000' and len_asser
        #
        # case_section = '[接口自动化bug] ' + '-号源池 ' + 'CSAM科室信息查询,orgId必填项超长'
        # mail_title_url = 'https://' + self.url + url_path
        # request_method = 'post'
        # print(result_buginfo_template(case_section, url, request_method, data, r))
        # title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        # content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        # bug_to_zentao(res, title, content.replace('\'', '').replace('"', ''), self.zentao_bug_assign,
        #               self.zentao_bug_commit)
        # bug_id = from_zentaotitle_get_zentaoid(title)
        # title_mail = 'BUG #' + str(bug_id) + ' ' + title
        # mail_temp = bug_mail_template(str(bug_id), title, content,
        #                               ['code=' + str(r.json()['code']),r.json()['result']['dataLen']],
        #                               ['code=000000',0],
        #                               new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        # if res == False:
        #     send_email(self.bug_mail_addressee, title_mail, mail_temp, self.bug_mail_cc)
        # self.assertTrue(res)
        # self.assertTrue(len_asser,'返回值不是空值')
        # log.info('CSAM科室信息查询,orgId必填项超长')
        # time.sleep(1)
