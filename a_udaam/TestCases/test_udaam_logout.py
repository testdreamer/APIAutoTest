#-- coding: utf-8 --

#@Time : 2022/6/1 13:09

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : test_udaam_logout.py

#@Software: PyCharm

from Utils.page import *
from Basepage.unittestChushihua import TestApi
from Utils.operationyaml import *
from Utils.operationini import Conf
from Utils.operationini import *
from Utils.log import *
from Utils.encrypt import *
from Utils.currenttime import *
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
class Logout(TestApi,Helper):
    # 获取服务器地址,,,
    url = read_yaml(sys.path[-1] + '/data/server_address.yaml', 'url')
    case_paramt_ini = sys.path[-1] + '/data/case_parameters.ini'
    token_yaml = sys.path[-1] + '/data/token.yaml'
    token = read_yaml(token_yaml, 'token')
    cf = Conf
    '''
    退出登录,正确
    '''
    def test_logout(self):
        url = 'http://' + self.url + '/sys/authorization/logout'
        headers = {
            'Authorization': 'Basic '+self.token}
        r = self.delete(url, headers)
        log.info(r.text)
        self.assertEqual(r.json()['code'],200)
        self.assertEqual(r.json()['status'],200)
        self.assertEqual(r.json()['message'],'成功','退出登录失败')