#-- coding: utf-8 --#@Time : 2022/6/22 13:59#@Author : tianxh#@Email : tianxh@casking.com.cn#@File : test_udaam_platrole.py#@Software: PyCharmfrom Utils.page import *from Utils.dicttogetparameter import *from Basepage.unittestChushihua import TestApifrom Utils.operationyaml import *from Utils.operationini import Conffrom Utils.operationini import *from Utils.connectMysql import ConnectMysqlfrom Utils.log import *from Utils.send_email import *from Utils.operation_zentao_mysql import *from Utils.all_style_template import *import jsonfrom Utils.encrypt import *from Utils.currenttime import *import sys,ossys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))class PlatRoles(TestApi,Helper):    # 获取服务器地址,,,    url = read_yaml(sys.path[-1] + '/data/server_address.yaml', 'url')    case_paramt_ini = sys.path[-1] + '/data/case_parameters.ini'    cf = Conf    '''    新增平台角色类型,正确    '''    def test_add_plat_role_types(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        self.cf.put_ini(self.case_paramt_ini, '新增平台角色类型,正确', 'name', str(get_time()))        # 获取ini中用例        data = self.cf.getini_by_section(self.case_paramt_ini, '新增平台角色类型,正确')        get_parameter = dict_to_get_parameter(data)        url = 'http://' + self.url + '/sys/platrole/page/plat/addRoleType?' + get_parameter        headers = {            'Authorization': 'Bearer '+token}        r = self.get(url,headers)        log.info(r.text)        res = r.json()['code'] == 200        case_section = '新增平台角色类型,正确'        url_path = '/sys/platrole/page/plat/addRoleType'        mail_title_url = 'http://' + self.url + url_path        request_method = 'get'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code'])],                                      ['code=200'],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        #将data值写到[新增平台角色,正确]roleType中,        self.cf.put_ini(self.case_paramt_ini,'新增平台角色,正确','roleType',r.json()['data'])        # 将data值写到[修改平台角色,正确]roleType中,        self.cf.put_ini(self.case_paramt_ini, '修改平台角色,正确', 'roleType', r.json()['data'])        #获取[新增平台角色类型,正确]的name值写到[修改平台角色,正确]roleTypeName中        add_platrole_type_name = self.cf.getini_by_option(self.case_paramt_ini,'新增平台角色类型,正确','name')        self.cf.put_ini(self.case_paramt_ini,'修改平台角色,正确','roleTypeName',add_platrole_type_name)        log.info('新增平台角色类型,正确')        time.sleep(1)    '''        查询平台角色类型,正确        '''    def test_query_plat_role_types(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        data = self.cf.getini_by_section(self.case_paramt_ini, '查询平台角色类型,正确')        get_parameter = dict_to_get_parameter(data)        url = 'http://' + self.url + '/sys/platrole/page/findRoleTypeAll?' + get_parameter        headers = {            'Authorization': 'Bearer ' + token}        r = self.get(url, headers)        log.info(r.text)        add_type_name = self.cf.getini_by_option(self.case_paramt_ini, '新增平台角色类型,正确', 'name')        sources = []        for i in range(len(r.json()['data'])):            sources.append(r.json()['data'][i]['name'])        res = r.json()['code'] == 200 and add_type_name in sources        case_section = '查询平台角色类型,正确'        url_path = '/sys/platrole/page/findRoleTypeAll'        mail_title_url = 'http://' + self.url + url_path        request_method = 'get'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code']),sources],                                      ['code=200',[add_type_name]],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        self.assertTrue(            add_type_name in sources        )        log.info('查询平台角色类型,正确')        time.sleep(1)    '''            查询角色权限树,正确            '''    def test_query_loadpermission_tree(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        data = self.cf.getini_by_section(self.case_paramt_ini, '查询角色权限树,正确')        get_parameter = dict_to_get_parameter(data)        url = 'http://' + self.url + '/sys/platrole/page/loadPermissionTree?' + get_parameter        headers = {            'Authorization': 'Bearer ' + token}        r = self.get(url, headers)        log.info(r.text)        res = r.json()['code'] == 200        case_section = '查询角色权限树,正确'        url_path = '/sys/platrole/page/loadPermissionTree'        mail_title_url = 'http://' + self.url + url_path        request_method = 'get'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code'])],                                      ['code=200'],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        ss = []        ss.append(r.json()['data'][0]['children'][0]['id'])        ss.append(r.json()['data'][0]['children'][0]['systemId'])        ss.append(r.json()['data'][1]['children'][0]['id'])        ss.append(r.json()['data'][1]['children'][0]['systemId'])        #把resourceId的集合写到[新增平台角色,正确]的resourceIdList中        self.cf.put_ini(self.case_paramt_ini,'新增平台角色,正确','resourceIdList',str(ss).replace("'",'"'))        log.info('查询角色权限树,正确')        time.sleep(1)    '''                新增平台角色,正确                '''    def test_add_plat_role(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        data = self.cf.getini_by_section(self.case_paramt_ini, '新增平台角色,正确')        data1 = json.dumps(json.loads(            str(data).replace("'", "\"").replace('"[', '[').replace(                ']"', ']')))        url = 'http://' + self.url + '/sys/platrole/page/plat/add'        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token}        r = self.post(url,data1, headers)        log.info(r.text)        res = r.json()['code'] == 200        case_section = '新增平台角色,正确'        url_path = '/sys/platrole/page/plat/add'        mail_title_url = 'http://' + self.url + url_path        request_method = 'post'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code'])],                                      ['code=200'],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        #获取[新增平台角色,正确]的name写到[查询应用列表,正确]sysName中        add_platrole_name = self.cf.getini_by_option(self.case_paramt_ini,'新增平台角色,正确','name')        self.cf.put_ini(self.case_paramt_ini,'查询应用列表,正确','sysName',add_platrole_name)        # 将data值写到[修改平台角色,正确]的id中        self.cf.put_ini(self.case_paramt_ini, '修改平台角色,正确', 'id', r.json()['data'])        #将data值写到[查询平台角色的权限, 正确]id中        self.cf.put_ini(self.case_paramt_ini, '查询平台角色的权限,正确', 'id', r.json()['data'])        # 将data值写到[删除平台角色,正确]id中        self.cf.put_ini(self.case_paramt_ini, '删除平台角色,正确', 'id', r.json()['data'])        log.info('新增平台角色,正确')        time.sleep(1)    '''                    查询平台角色,正确        '''    def test_query_plat_role(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        data = self.cf.getini_by_section(self.case_paramt_ini, '查询平台角色,正确')        get_parameter = dict_to_get_parameter(data)        url = 'http://' + self.url + '/sys/platrole/page/findAll?'+get_parameter        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token}        r = self.get(url, headers)        log.info(r.text)        res = r.json()['code'] == 200        case_section = '查询平台角色,正确'        url_path = '/sys/platrole/page/findAll'        mail_title_url = 'http://' + self.url + url_path        request_method = 'get'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code'])],                                      ['code=200'],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        log.info('查询平台角色,正确')        time.sleep(1)    '''                        修改平台角色,正确            '''    def test_update_plat_role(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        #获取[新增平台角色,正确]name进行修改后写到[修改平台角色,正确]的neme中        add_platrole_name = self.cf.getini_by_option(self.case_paramt_ini,'新增平台角色,正确','name')        self.cf.put_ini(self.case_paramt_ini,'修改平台角色,正确','name',add_platrole_name+'dd')        # 获取ini中用例        data = self.cf.getini_by_section(self.case_paramt_ini, '修改平台角色,正确')        get_parameter = dict_to_get_parameter(data)        data1 = json.dumps(json.loads(            str(data).replace("'", "\"").replace('"[', '[').replace(                ']"', ']').replace('"null"', 'null').replace('"true"', 'true')))        url = 'http://' + self.url + '/sys/platrole/page/plat/update'        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token}        r = self.post(url, data1,headers)        log.info(r.text)        res = r.json()['code'] == 200        case_section = '修改平台角色,正确'        url_path = '/sys/platrole/page/plat/update'        mail_title_url = 'http://' + self.url + url_path        request_method = 'post'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code'])],                                      ['code=200'],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        log.info('修改平台角色,正确')        time.sleep(1)    '''                            查询平台角色的权限,正确                '''    def test_query_platrole_perm(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        data = self.cf.getini_by_option(self.case_paramt_ini,'查询平台角色的权限,正确','id')        url = 'http://' + self.url + '/sys/platrole/page/'+data        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token}        r = self.get(url, headers)        log.info(r.text)        # 获取[修改平台角色,正确]的name进行校验        update_role_name = self.cf.getini_by_option(self.case_paramt_ini, '修改平台角色,正确', 'name')        res = r.json()['code'] == 200 and r.json()['data']['name'] == update_role_name        case_section = '查询平台角色的权限,正确'        url_path = '/sys/platrole/page/'        mail_title_url = 'http://' + self.url + url_path        request_method = 'get'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code']),r.json()['data']['name']],                                      ['code=200',update_role_name],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        self.assertEqual(r.json()['data']['name'],update_role_name)        log.info('查询平台角色的权限,正确')        time.sleep(1)    '''             删除平台角色,正确     '''    def test_delete_plat_role(self):        token_yaml = sys.path[-1] + '/a_udaam/data/token.yaml'        token = read_yaml(token_yaml, 'token')        # 获取ini中用例        data = self.cf.getini_by_option(self.case_paramt_ini, '删除平台角色,正确', 'id')        url = 'http://' + self.url + '/sys/platrole/page/plat/delete/' + data        headers = {            'Content-Type': 'application/json',            'Authorization': 'Bearer ' + token}        r = self.post(url, {},headers)        log.info(r.text)        res = r.json()['code'] == 200        case_section = '删除平台角色,正确'        url_path = '/sys/platrole/page/plat/delete/'        mail_title_url = 'http://' + self.url + url_path        request_method = 'post'        print(result_buginfo_template(case_section, url, request_method, data, r))        title = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[0]        content = mail_buginfo_template(case_section, mail_title_url, request_method, data, r)[1]        bug_to_zentao(res, title, content.replace('\'','').replace('"',''), 'zhaop', 'xiaojc')        bug_id = from_zentaotitle_get_zentaoid(title)        title_mail = 'BUG #' + str(bug_id) + ' ' + title        mail_temp = bug_mail_template(str(bug_id), title, content,                                      ['code=' + str(r.json()['code'])],                                      ['code=200'],                                      new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')        if res == False:            send_email('liny@casking.com.cn', title_mail, mail_temp)            add_roletype_name = self.cf.getini_by_option(self.case_paramt_ini, '修改平台角色,正确', 'name')            sql = "delete from tb_role where name=" + "'" + add_roletype_name + "'"            connect = ConnectMysql()            results = connect.change_data(sql)        else:            pass        self.assertEqual(r.json()['code'], 200)        self.assertEqual(r.json()['message'], '成功')        log.info('删除平台角色,正确')        time.sleep(1)    '''                 删除平台角色类型,正确         '''    def test_delete_plat_role_type(self):        # 获取[新增平台角色类型,正确]name        add_roletype_name = self.cf.getini_by_option(self.case_paramt_ini,'新增平台角色类型,正确','name')        sql = "delete from tb_role_type where name="+"'"+add_roletype_name+"'"        connect = ConnectMysql()        results = connect.change_data(sql)