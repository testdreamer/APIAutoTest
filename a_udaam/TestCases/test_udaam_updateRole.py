# -*- coding: utf-8 -*-
"""
@Time ： 2022/5/27 15:09
@Auth ： tianxh
@File ：test_udaam_updateRole.py
@IDE ：PyCharm
@Motto：No Bug No Error
"""
from Basepage.unittestChushihua import TestApi
from Utils.page import Helper
from Utils.operationyaml import read_yaml
from Utils.log import log
from Utils.operationini import Conf
from Utils.connectMysql import ConnectMysql
import sys
import time


class UpdateRole(TestApi, Helper):
    def __init__(self):
        # 超继承父类的初始化函数
        super(TestApi, self).__init__()
        self.ip = read_yaml(sys.path[1] + "/a_udaam/data/server_address.yaml", "uddam_url")
        self.url = 'http://' + self.ip + '/soap/synchronousData'
        self.headers = {'Content-Type': 'application/xml'}
        self.parameters_path = sys.path[1] + "/a_udaam/data/case_udaam_parameters.ini"
        self.connect = ConnectMysql()
        self.cf = Conf
        self.ruleId = '327fcaf43364d6dc5f6e3bc98e779d63'
        self.name = 'xxlRoleupdate'

    '''初始化环境创建'''
    def setUp(self):
        del_sql = "delete from tb_role_type where name ='xxlRoleupdate'"
        self.connect.change_data(del_sql)
        insert_sql = "INSERT INTO `udaam - admin - v3 - demo`.`tb_role_type` " \
                     "( `id`, `name`, `en_name`, `description`, `pid`, `seq_num`, `status`,  )" \
                     "VALUES( %s, %s, NULL, NULL, NULL, NULL, '1',  );" % (self.ruleId, self.name)
        self.connect.change_data(insert_sql)
    '''角色类型同步，正常入参'''
    def test_update_role_type_right(self):
        # 初始化
        self.setUp()
        # 获取init中的测试用例
        # print("=============="+self.parameters_path)
        datas = self.cf.getini_by_option(self.parameters_path, '角色类型修改-参数正确', 'v1')
        # data = json.dumps(dataDist).strip("{'}")
        # get_parameter = dict_to_get_parameter(data)
        log.info('角色类型同步参数正确:' + self.url)
        r = self.post(self.url, headers=self.headers, data=datas)
        log.info('请求头:' + str(self.headers))
        log.info('传入参数:' + datas)
        sql = "select name,en_name,description,pid,seq_num,updateTime,updateUserId,updateUserName" \
              " from tb_role_type where name ='xxlRoleupdate'"
        results = self.connect.get_select_data(sql)
        # print(results)
        for row in results:
            name = row[0]
            en_name = row[1]
            description = row[2]
            pid = row[3]
            seq_num = row[4]
            updateTime = row[5]
            updateUserId = row[6]
            updateUserName = row[7]

        self.assertIn('&lt;retDesc&gt;同步成功&lt;', r.text)
        self.assertEqual(name, 'xxlRoleupdate')
        self.assertEqual(en_name, 'xxlRoleEnNameupdate')
        self.assertEqual(description, 'xxlEdesc')
        self.assertEqual(pid, '123')
        self.assertEqual(pid, '123')
        log.info('返回值：' + r.text)
        time.sleep(2)

if __name__ == '__main__':
    c = UpdateRole
    c.padg()