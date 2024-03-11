#-- coding: utf-8 --

#@Time : 2022/6/2 19:20

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : test_udaam_personnelmanagement.py

#@Software: PyCharm
from Utils.page import *
from Utils.dicttogetparameter import *
from Basepage.unittestChushihua import TestApi
from Utils.operationyaml import *
from Utils.operationini import Conf
from Utils.operationini import *
from Utils.log import *
import json
from Utils.operation_zentao_mysql import *
from Utils.send_email import *
from Utils.all_style_template import *
from Utils.encrypt import *
from Utils.currenttime import *
from Utils.create_random import *
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
class PersonnelManagement(TestApi,Helper):
    # 获取服务器地址,,,
    url = read_yaml(sys.path[-1] + '/data/server_address.yaml', 'url')
    case_paramt_ini = sys.path[-1] + '/data/case_parameters.ini'
    cf = Conf
    '''
    创建人员信息,正确
    '''
    def test_create_userinfo(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        self.cf.put_ini(self.case_paramt_ini, '创建人员信息,正确', 'username', create_letter(8))
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '创建人员信息,正确')
        data1 = json.dumps(json.loads(str(data).replace("'","\"").replace('"null"','null').replace('"true"','true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/list/insertUser'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer '+token
        }
        r = self.post(url,data1,headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '创建人员信息,正确'
        url_path = '/sys/personManage/page/list/insertUser'
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
        log.info('创建人员信息,正确')
        time.sleep(1)

    '''
        人员条件查询,正确
    '''
    def test_staffconditionenquir_byname(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员条件查询,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/findAll?'+get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        # 获取创建人员信息的用户名
        create_personnel_name = self.cf.getini_by_option(self.case_paramt_ini, '创建人员信息,正确', 'username')
        res = r.json()['code'] == 200 and r.json()['data']['content'][0]['username'] == create_personnel_name
        case_section = '人员条件查询,正确'
        url_path = '/sys/personManage/page/findAll'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data']['content'][0]['username']],
                                      ['code=200',create_personnel_name],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        #将获取的创建人员信息的用户名和查询的用户名进行验证
        self.assertEqual(r.json()['data']['content'][0]['username'], create_personnel_name)
        # 获取创建人员信息的userid
        create_personnel_userid = r.json()['data']['content'][0]['userId']
        # 获取创建人员信息的username
        create_personnel_username = r.json()['data']['content'][0]['username']
        #将userid写入到ini文件的[人员角色 - 授予组织, 正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '人员角色-授予组织,正确', 'userId', create_personnel_userid)
        # 将userid写入到ini文件的[人员角色 - 授予角色, 正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '人员角色-授予角色,正确', 'userId', create_personnel_userid)
        # 将userid写入到ini文件的[人员角色-查询拥有角色,正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '人员角色-查询拥有角色,正确', 'userId', create_personnel_userid)
        # 将userid写入到ini文件的[人员角色-查询机构列表,正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '人员角色-查询机构列表,正确', 'userId', create_personnel_userid)
        # 将userid写入到ini文件的[特殊权限-查询系统列表,正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '特殊权限-查询系统列表,正确', 'userId', create_personnel_userid)
        # 将userid写入到ini文件的[特殊权限-修改角色权限,正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '特殊权限-修改角色权限,正确', 'userId', create_personnel_userid)
        # 将userid写入到ini文件的[人员数据权限-查询系统列表,正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '人员数据权限-查询系统列表,正确', 'userId', create_personnel_userid)
        # 将userid写入到ini文件的[人员数据权限-已配数权关系的机构,正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '人员数据权限-已配数权关系的机构,正确', 'userId', create_personnel_userid)
        # 将userid写入到ini文件的[人员组织-用户授予机构-删除,正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '人员组织-用户授予机构-删除,正确', 'userId', create_personnel_userid)
        # 将userid写入到ini文件的[用户详情, 正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '用户详情,正确', 'userId', create_personnel_userid)
        # 将userid写入到ini文件的[人员组织-人员已绑定的机构列表, 正确]的userId中
        self.cf.put_ini(self.case_paramt_ini, '人员组织-人员已绑定的机构列表,正确', 'userId', create_personnel_userid)
        #将userid写入到ini文件的[人员信息删除,正确]的id键中
        self.cf.put_ini(self.case_paramt_ini,'人员信息删除,正确','id',create_personnel_userid)
        # 将username写入到ini文件的[账号查询-按用户名,正确]的uName键中
        self.cf.put_ini(self.case_paramt_ini, '账号查询-按用户名,正确', 'uName', create_personnel_username)
        # 将username写入到ini文件的[人员条件查询-按用户名,正确]的uName键中
        self.cf.put_ini(self.case_paramt_ini, '人员条件查询-按用户名,正确', 'uName', create_personnel_username)
        log.info('人员条件查询,正确')
        time.sleep(1)

    '''
                    人员角色-查询所有角色及类型,正确
    '''
    def test_query_all_role_sandtypes(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员角色-查询所有角色及类型,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/findAllRole?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '人员角色-查询所有角色及类型,正确'
        url_path = '/sys/personManage/page/findAllRole'
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
        log.info('人员角色-查询所有角色及类型,正确')
        time.sleep(1)

    '''
                    2022-08-12新增
                    人员组织-查询当前用户可授予的机构,正确
        '''

    def test_query_user_grant_org(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员组织-查询当前用户可授予的机构,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/getOrgsByUserOrg?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        #获取[人员组织-查询当前用户可授予的机构,正确]的orgName进行校验
        grantorg_orgname = self.cf.getini_by_option(self.case_paramt_ini, '人员组织-查询当前用户可授予的机构,正确','orgName')
        res = r.json()['code'] == 200 and r.json()['data'][0]['name'] == grantorg_orgname
        case_section = '人员组织-查询当前用户可授予的机构,正确'
        url_path = '/sys/personManage/page/getOrgsByUserOrg'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data'][0]['name']],
                                      ['code=200',grantorg_orgname],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data'][0]['name'],grantorg_orgname)
        log.info('人员组织-查询当前用户可授予的机构,正确')
        time.sleep(1)



    '''
            人员角色-授予组织,正确
    '''
    def test_user_role_auth_org(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取当前时间
        get_times = get_time()
        dangqian_time = get_times
        timeArray1 = time.localtime(dangqian_time / 1000)
        new_time1 = time.strftime("%Y-%m-%d %H:%M:%S", timeArray1)

        # 获取以后时间
        yihou_time = get_times + 1000000000
        timeArray2 = time.localtime(yihou_time / 1000)
        out_time = time.strftime("%Y-%m-%d %H:%M:%S", timeArray2)
        #将当前时间写到[人员角色-授予组织,正确]的entryTime中
        self.cf.put_ini(self.case_paramt_ini,'人员角色-授予组织,正确','entryTime',new_time1)
        # 将当前时间写到[人员角色-授予组织,正确]的outTime中
        self.cf.put_ini(self.case_paramt_ini, '人员角色-授予组织,正确', 'outTime', out_time)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员角色-授予组织,正确')
        data1 = json.dumps(json.loads(str(data).replace("'[","[").replace("]'","]").replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true').replace('userType": "0"','userType": 0')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/usersOrg/saveUserOrg'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '人员角色-授予组织,正确'
        url_path = '/sys/personManage/page/usersOrg/saveUserOrg'
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
        log.info('人员角色-授予组织,正确')
        time.sleep(1)

    '''
                人员角色-授予角色,正确
    '''
    def test_user_role_auth_role(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')

        #请求人员角色-查询所有角色及类型接口获取roleId,roleName
        url = 'http://' + self.url + '/sys/personManage/page/findAllRole'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        allroletypes_roleId = r.json()['data'][0]['roleList'][0]['roleId']
        allroletypes_roleName = r.json()['data'][0]['roleList'][0]['roleName']
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员角色-授予角色,正确')

        #获取的用例的usersRolesDTOList部分去掉头尾"[""]"部分,转成dict,获取roleName值
        usersroleslist_dict = json.loads(data['usersRolesDTOList'][:-1][1:])
        usersroleslist_dict['roleName'] = allroletypes_roleName
        usersroleslist_dict['roleId'] = allroletypes_roleId
        #将usersroleslist_dict转成str,前后增加"[","]",再把值改成data的usersRolesDTOList中
        usersroleslist_str = '['+str(usersroleslist_dict)+']'
        data['usersRolesDTOList'] = usersroleslist_str

        data1 = json.dumps(json.loads(
            str(data).replace('"[', "[").replace(']"', "]").replace("'", "\"").replace('"null"', 'null').replace(
                '"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/usersRoles/update'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url, data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '人员角色-授予角色,正确'
        url_path = '/sys/personManage/page/usersRoles/update'
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
        log.info('人员角色-授予角色,正确')
        time.sleep(1)

    '''
                2022-08-12新增
                    人员组织-人员已绑定的机构列表,正确
        '''

    def test_query_user_bound_org_list(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员组织-人员已绑定的机构列表,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/userId?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        #获取[人员角色-授予角色,正确]的orgId进行校验
        grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini,'人员角色-授予角色,正确','orgId')
        res = r.json()['code'] == 200 and r.json()['data'][0]['orgId'] == grant_org_orgid
        case_section = '人员组织-人员已绑定的机构列表,正确'
        url_path = '/sys/personManage/page/userId'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data'][0]['orgId']],
                                      ['code=200',grant_org_orgid],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data'][0]['orgId'],grant_org_orgid)
        log.info('人员组织-人员已绑定的机构列表,正确')
        time.sleep(1)

    '''
                    2022-08-12新增
                        人员组织-查询机构下的部门列表,正确
            '''

    def test_query_org_div_list(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员组织-查询机构下的部门列表,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/deptList?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '人员组织-查询机构下的部门列表,正确'
        url_path = '/sys/personManage/page/deptList'
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
        log.info('人员组织-查询机构下的部门列表,正确')
        time.sleep(1)

    '''
                        2022-08-12新增
                            人员角色-查询拥有角色,正确
                '''

    def test_query_own_role(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[人员角色-授予角色,正确]的orgId写到[人员角色-查询拥有角色,正确]的orgId
        grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini, '人员角色-授予角色,正确', 'orgId')
        self.cf.put_ini(self.case_paramt_ini,'人员角色-查询拥有角色,正确','orgId',grant_org_orgid)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员角色-查询拥有角色,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/usersRolesListByUserId?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        url_as = 'http://' + self.url + '/sys/personManage/page/findAllRole'
        r_as = self.get(url_as, headers)
        sources = []
        for i in range(len(r_as.json()['data'])):
            for y in range(len(r_as.json()['data'][i]['roleList'])):
                sources.append(r_as.json()['data'][i]['roleList'][y]['roleName'])
        print(sources)
        res = r.json()['code'] == 200 and r.json()['data'][0]['roleName'] in sources
        case_section = '人员角色-查询拥有角色,正确'
        url_path = '/sys/personManage/page/usersRolesListByUserId'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),[r.json()['data'][0]['roleName']]],
                                      ['code=200',sources],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertTrue(res)
        log.info('人员角色-查询拥有角色,正确')
        time.sleep(1)

    '''
                                    2022-08-12新增
                                        人员角色-查询机构列表,正确
                            '''

    def test_query_org_list(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员角色-查询机构列表,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/getOrgIntersection?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        if self.url == '192.168.13.159:10041':
            self.assertEqual(r.json()['code'], 200)
            self.assertEqual(r.json()['message'], '成功')
        else:
            res = r.json()['code'] == 200 and r.json()['data'][0]['orgName']=='深圳联影'
            case_section = '人员角色-查询机构列表,正确'
            url_path = '/sys/personManage/page/getOrgIntersection'
            mail_title_url = 'http://' + self.url + url_path
            request_method = 'get'
            print(result_buginfo_template(case_section, url, request_method, data, r))
            title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
            content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
            bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
            bug_id = from_zentaotitle_get_zentaoid(title)
            title_mail = 'BUG #' + str(bug_id) + ' ' + title
            mail_temp = bug_mail_template(str(bug_id), title, content,
                                          ['code=' + str(r.json()['code']),r.json()['data'][0]['orgName']],
                                          ['code=200','深圳联影'],
                                          new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
            if res == False:
                send_email('liny@casking.com.cn', title_mail, mail_temp)
            self.assertEqual(r.json()['code'], 200)
            self.assertEqual(r.json()['message'], '成功')
            self.assertEqual(r.json()['data'][0]['orgName'],'深圳联影')
        log.info('人员角色-查询机构列表,正确')
        time.sleep(1)

    '''
                2022-08-12新增
                    人员角色-查询拥有的资源,正确
         '''

    def test_query_own_resource(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[人员角色-授予角色,正确]的orgId写到[人员角色-查询拥有角色,正确]的orgId
        grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini, '人员角色-授予角色,正确', 'orgId')
        self.cf.put_ini(self.case_paramt_ini, '人员角色-查询拥有的资源,正确', 'orgId', grant_org_orgid)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员角色-查询拥有的资源,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'[", "[").replace("]'", "]").replace("'", "\"").replace('"null"', 'null').replace(
                '"true"', 'true').replace('userType": "0"', 'userType": 0')))
        # get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/getPermissionByRoleList'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '人员角色-查询拥有的资源,正确'
        url_path = '/sys/personManage/page/getPermissionByRoleList'
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
        # self.assertEqual(r.json()['data'][0]['name'], '区域协同')
        # self.assertEqual(r.json()['data'][1]['name'], '患者360')
        log.info('人员角色-查询拥有的资源,正确')
        time.sleep(1)

    '''
                2022-08-12新增
                    特殊权限-查询系统列表,正确
    '''

    def test_isattr_query_sys_list(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[人员角色-授予角色,正确]的orgId写到[人员角色-查询拥有角色,正确]的orgId
        grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini, '人员角色-授予角色,正确', 'orgId')
        self.cf.put_ini(self.case_paramt_ini, '特殊权限-查询系统列表,正确', 'orgId', grant_org_orgid)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '特殊权限-查询系统列表,正确')
        # data1 = json.dumps(json.loads(
        #     str(data).replace("'[", "[").replace("]'", "]").replace("'", "\"").replace('"null"', 'null').replace(
        #         '"true"', 'true').replace('userType": "0"', 'userType": 0')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/getUsersSystemByUserId?'+ get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '特殊权限-查询系统列表,正确'
        url_path = '/sys/personManage/page/getUsersSystemByUserId'
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
        # self.assertEqual(r.json()['data'][0]['permissionName'], '区域协同')
        # self.assertEqual(r.json()['data'][1]['permissionName'], '患者360')
        log.info('特殊权限-查询系统列表,正确')
        time.sleep(1)

    '''
                    2022-08-12新增
                        特殊权限-修改角色权限,正确
        '''

    def test_update_role_auth(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[人员角色-授予角色,正确]的orgId写到[特殊权限-修改角色权限,正确]的orgId
        grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini, '人员角色-授予角色,正确', 'orgId')
        self.cf.put_ini(self.case_paramt_ini, '特殊权限-修改角色权限,正确', 'orgId', grant_org_orgid)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '特殊权限-修改角色权限,正确')
        data1 = json.dumps(json.loads(
            str(data).replace("'[", "[").replace("]'", "]").replace("'", "\"").replace('"null"', 'null').replace(
                '"true"', 'true').replace('userType": "0"', 'userType": 0')))
        # get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/usersSystem/update'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data1, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '特殊权限-修改角色权限,正确'
        url_path = '/sys/personManage/page/usersSystem/update'
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
        log.info('特殊权限-修改角色权限,正确')
        time.sleep(1)

    '''
                        2022-08-12新增
                            账号对照-查询系统列表,正确
            '''

    def test_account_control_query_sys_list(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[人员角色-授予角色,正确]的orgId写到[账号对照-查询系统列表,正确]的orgId
        # grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini, '人员角色-授予角色,正确', 'orgId')
        # self.cf.put_ini(self.case_paramt_ini, '账号对照-查询系统列表,正确', 'orgId', grant_org_orgid)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '账号对照-查询系统列表,正确')
        # data1 = json.dumps(json.loads(
        #     str(data).replace("'[", "[").replace("]'", "]").replace("'", "\"").replace('"null"', 'null').replace(
        #         '"true"', 'true').replace('userType": "0"', 'userType": 0')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/finSystemInfos?'+ get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        sources = []
        for i in range(len(r.json()['data'])):
            sources.append(r.json()['data'][i]['name'])
        print(sources)
        result = ('40三应用' in sources and
                  'rap2第三方应用' in sources and
                  '40第三方需要插件exe' in sources and
                  '40三应用0614' in sources
                  )
        res = r.json()['code'] == 200
        case_section = '账号对照-查询系统列表,正确'
        url_path = '/sys/personManage/page/finSystemInfos'
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
        log.info('账号对照-查询系统列表,正确')
        time.sleep(1)

    '''
                    2022-08-12新增
                        人员数据权限-查询系统列表,正确
         '''

    def test_user_data_auth_query_sys_list(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[人员角色-授予角色,正确]的orgId写到[账号对照-查询系统列表,正确]的orgId
        grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini, '人员角色-授予角色,正确', 'orgId')
        self.cf.put_ini(self.case_paramt_ini, '人员数据权限-查询系统列表,正确', 'orgId', grant_org_orgid)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员数据权限-查询系统列表,正确')
        # data1 = json.dumps(json.loads(
        #     str(data).replace("'[", "[").replace("]'", "]").replace("'", "\"").replace('"null"', 'null').replace(
        #         '"true"', 'true').replace('userType": "0"', 'userType": 0')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/dataPerSystemList?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '人员数据权限-查询系统列表,正确'
        url_path = '/sys/personManage/page/dataPerSystemList'
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
        # self.assertEqual(r.json()['data'][0]['name'], '区域协同')
        # self.assertEqual(r.json()['data'][1]['name'], '患者360')
        log.info('人员数据权限-查询系统列表,正确')
        time.sleep(1)

    '''
                2022-08-12新增
                人员数据权限-机构列表,正确
    '''

    def test_user_data_auth_org_list(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[人员角色-授予角色,正确]的orgId写到[账号对照-查询系统列表,正确]的orgId
        # grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini, '人员角色-授予角色,正确', 'orgId')
        # self.cf.put_ini(self.case_paramt_ini, '人员数据权限-机构列表,正确', 'orgId', grant_org_orgid)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员数据权限-机构列表,正确')
        # data1 = json.dumps(json.loads(
        #     str(data).replace("'[", "[").replace("]'", "]").replace("'", "\"").replace('"null"', 'null').replace(
        #         '"true"', 'true').replace('userType": "0"', 'userType": 0')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/orgList?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        orglist_name = self.cf.getini_by_option(self.case_paramt_ini, '人员数据权限-机构列表,正确','name')
        res = r.json()['code'] == 200 and r.json()['data']['content'][0]['name'] == orglist_name
        case_section = '人员数据权限-机构列表,正确'
        url_path = '/sys/personManage/page/orgList'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data']['content'][0]['name']],
                                      ['code=200',orglist_name],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data']['content'][0]['name'], orglist_name)
        log.info('人员数据权限-机构列表,正确')
        time.sleep(1)

    '''
                    2022-08-12新增
                    人员数据权限-已配数权关系的机构,正确
        '''

    def test_user_data_auth_relation_org(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[人员角色-授予角色,正确]的orgId写到[账号对照-查询系统列表,正确]的orgId
        grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini, '人员角色-授予角色,正确', 'orgId')
        self.cf.put_ini(self.case_paramt_ini, '人员数据权限-已配数权关系的机构,正确', 'orgId', grant_org_orgid)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员数据权限-已配数权关系的机构,正确')
        # data1 = json.dumps(json.loads(
        #     str(data).replace("'[", "[").replace("]'", "]").replace("'", "\"").replace('"null"', 'null').replace(
        #         '"true"', 'true').replace('userType": "0"', 'userType": 0')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/dataPerOrgList?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '人员数据权限-已配数权关系的机构,正确'
        url_path = '/sys/personManage/page/dataPerOrgList'
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
        log.info('人员数据权限-已配数权关系的机构,正确')
        time.sleep(1)

    '''
                        2022-08-12新增
                        人员数据权限-查询部门列表,正确
            '''

    def test_user_data_auth_query_div_list(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[人员角色-授予角色,正确]的orgId写到[账号对照-查询系统列表,正确]的orgId
        grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini, '人员角色-授予角色,正确', 'orgId')
        self.cf.put_ini(self.case_paramt_ini, '人员数据权限-查询部门列表,正确', 'orgId', grant_org_orgid)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员数据权限-查询部门列表,正确')
        # data1 = json.dumps(json.loads(
        #     str(data).replace("'[", "[").replace("]'", "]").replace("'", "\"").replace('"null"', 'null').replace(
        #         '"true"', 'true').replace('userType": "0"', 'userType": 0')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/loadDeptTree?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '人员数据权限-查询部门列表,正确'
        url_path = '/sys/personManage/page/loadDeptTree'
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
        log.info('人员数据权限-查询部门列表,正确')
        time.sleep(1)

    '''
                            2022-08-12新增
                                人员组织-用户授予机构-删除,正确
                    '''

    def test_user_grant_org_delete(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取[人员角色-授予角色,正确]的orgId写到[人员角色-查询拥有角色,正确]的orgId
        grant_org_orgid = self.cf.getini_by_option(self.case_paramt_ini, '人员角色-授予角色,正确', 'orgId')
        self.cf.put_ini(self.case_paramt_ini, '人员角色-查询拥有角色,正确', 'orgId', grant_org_orgid)
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员组织-用户授予机构-删除,正确')
        data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        # get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/deleteUserOrg'
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,data1,headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '人员组织-用户授予机构-删除,正确'
        url_path = '/sys/personManage/page/deleteUserOrg'
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
        log.info('人员组织-用户授予机构-删除,正确')
        time.sleep(1)



    '''
            用户详情,正确
    '''
    def test_user_info(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '用户详情,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = dict_to_get_parameter(data)
        url = 'http://' + self.url + '/sys/personManage/page/queryById?' + get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.get(url, headers)
        log.info(r.text)
        # 获取[用户详情,正确]的id值和返回的userId值校验
        userdetails_id = self.cf.getini_by_option(self.case_paramt_ini, '用户详情,正确', 'userId')
        # 获取[创建人员信息,正确]的id值和返回的username值校验
        userdetails_username = self.cf.getini_by_option(self.case_paramt_ini, '创建人员信息,正确', 'username')
        res = r.json()['code'] == 200 and r.json()['data']['userId']==userdetails_id and r.json()['data']['username']==userdetails_username
        case_section = '用户详情,正确'
        url_path = '/sys/personManage/page/queryById'
        mail_title_url = 'http://' + self.url + url_path
        request_method = 'get'
        print(result_buginfo_template(case_section, url, request_method, data, r))
        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]
        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]
        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')
        bug_id = from_zentaotitle_get_zentaoid(title)
        title_mail = 'BUG #' + str(bug_id) + ' ' + title
        mail_temp = bug_mail_template(str(bug_id), title, content,
                                      ['code=' + str(r.json()['code']),r.json()['data']['userId'],r.json()['data']['username']],
                                      ['code=200',userdetails_id,userdetails_username],
                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
        if res == False:
            send_email('liny@casking.com.cn', title_mail, mail_temp)
        self.assertEqual(r.json()['code'], 200)
        self.assertEqual(r.json()['message'], '成功')
        self.assertEqual(r.json()['data']['userId'],userdetails_id)
        self.assertEqual(r.json()['data']['username'], userdetails_username)
        log.info('用户详情,正确')
        time.sleep(1)



    '''
            人员信息删除,正确
    '''
    def test_delete_userinfo(self):
        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'
        token = read_yaml(token_yaml, 'token')
        # 获取ini中用例
        data = self.cf.getini_by_section(self.case_paramt_ini, '人员信息删除,正确')
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        get_parameter = self.cf.getini_by_option(self.case_paramt_ini,'人员信息删除,正确','id')
        url = 'http://' + self.url + '/sys/personManage/page/list/delete/'+get_parameter
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token
        }
        r = self.post(url,{},headers)
        log.info(r.text)
        res = r.json()['code'] == 200
        case_section = '人员信息删除,正确'
        url_path = '/sys/personManage/page/list/delete/'
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
        log.info('人员信息删除,正确')
        time.sleep(1)