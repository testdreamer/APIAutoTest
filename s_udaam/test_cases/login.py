#-- coding: utf-8 --

#@Time : 2022/10/20 13:22

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : login.py

#@Software: PyCharm
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
cf = Conf
def test_login():
    hp = Helper()
    config_ini = sys.path[-1] + '/data/UST_config.ini'
    username = cf.getini_by_option(config_ini,'用户名和密码','username')
    password = cf.getini_by_option(config_ini, '用户名和密码', 'password')
    url = cf.getini_by_option(config_ini, '服务器地址', 'url')
    image_verifications = sys.path[-1] + '/image_verification/image_verifications.jpg'
    rsa_code = encrpt(password)
    get_times = get_time()
    # 先访问验证码接口
    url_yanzhengma = 'http://' + url + '/udaam-ui/sys/authorization/captcha?key=' + str(get_times)
    data_yanzhengma = {}
    r = requests.get(url_yanzhengma, data_yanzhengma)
    # 保存验证码图片
    save_image_verification(image_verifications, r)
    # 获取验证码图片的验证码
    image_verification_code = get_image_verification(uname='liany', pwd='zpt123456789', img=image_verifications,
                                                     typeid=3)
    # image_verification_code = get_image_verification(self.image_verifications)
    print(image_verification_code)

    # 获取ini中用例
    # data = self.cf.getini_by_section(self.case_paramt_ini,'客户端用户登录,登录成功')
    data = {'grant_type': 'password', 'username': username, 'code': image_verification_code, 'orgId': '',
            'secret': rsa_code, 'key': get_times}
    # data1 = json.dumps(json.loads(str(data).replace("'", "\"").replace('"null"', 'null').replace('"true"', 'true')))
    url = 'http://' + url + '/sys/authorization/oauth/token'
    print('客户端用户登录,登录成功接口URL:' + url)
    print('请求方法:post')
    print('参数值:' + json.dumps(data, indent=1, ensure_ascii=False))
    headers = {'Authorization': 'Basic Y2xpZW50SWQ6Y2xlbnRfc2VjcmV0'}
    r = hp.post(url, data, headers)
    print('返回值:' + json.dumps(r.json(), indent=1, ensure_ascii=False))
    # log.info(r.text)
    token = r.json()['data']['access_token']
    return token