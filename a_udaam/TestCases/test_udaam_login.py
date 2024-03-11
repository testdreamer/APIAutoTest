#-- coding: utf-8 --

#@Time : 2022/5/31 10:09

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : test_udaam_login.py

#@Software: PyCharm

import unittest
from Utils.page import *
from Basepage.unittestChushihua import TestApi
from Utils.operationyaml import *
from Utils.operationini import Conf
from Utils.operationini import *
from Utils.log import *
from Utils.encrypt import *
import json
from Utils.currenttime import *
from Utils.getImageverification import *
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
class Login(TestApi,Helper):
    # 获取服务器地址,,,
    url = read_yaml(sys.path[-1]+'/data/server_address.yaml', 'url')
    case_paramt_ini = sys.path[-1] + '/data/case_parameters.ini'
    token_yaml = sys.path[-1] + '/data/token.yaml'
    image_verifications = sys.path[-1] + '/image_verification/image_verifications.jpg'
    cf = Conf
    def test_login(self):
        # pass
        rsa_code = encrpt('superAdmin')
        get_times = get_time()
        #先访问验证码接口
        url_yanzhengma = 'http://' + self.url + '/udaam-ui/sys/authorization/captcha?key='+str(get_times)
        data_yanzhengma = {}
        r = self.get(url_yanzhengma,data_yanzhengma)
        #保存验证码图片
        save_image_verification(self.image_verifications,r)
        #获取验证码图片的验证码
        image_verification_code = get_image_verification(uname='liany', pwd='zpt123456789', img=self.image_verifications, typeid=3)
        # image_verification_code = get_image_verification(self.image_verifications)
        print(image_verification_code)

        #获取ini中用例
        # data = self.cf.getini_by_section(self.case_paramt_ini,'客户端用户登录,登录成功')
        data = {'grant_type':'password','username':'superAdmin','code':image_verification_code,'orgId':'','secret':rsa_code,'key':get_times}
        # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
        url = 'http://' + self.url + '/sys/authorization/oauth/token'
        print('客户端用户登录,登录成功接口URL:' + url)
        print('请求方法:post')
        print('参数值:' + json.dumps(data, indent=1, ensure_ascii=False))
        headers = {'Authorization':'Basic Y2xpZW50SWQ6Y2xlbnRfc2VjcmV0'}
        r = self.post(url,data,headers)
        print('返回值:'+json.dumps(r.json(),indent=1,ensure_ascii=False))
        # log.info(r.text)
        self.assertEqual(r.json()['message'], '成功')
        token = r.json()['data']['access_token']



        #将token写入yaml文件
        if token:
            token_data = {'token':token}
            write_yaml(self.token_yaml,token_data)
            log.info("token写入yaml成功")
        else:
            log.info('没有token')
        log.info("客户端用户登录,登录成功")