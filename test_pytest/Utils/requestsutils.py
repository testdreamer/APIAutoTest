# _*_ coding : utf_8 _*_
# @Time : 18:18 
# @Author : 田霄汉
# @File : RequestsUtils
# @Project : APIAutoTest
# @User : Administrator
import json

import requests


class RequestsUtils:

    # 类变量：通过类名访问
    session = requests.session()

    def send_request(self, method, url, data, **kwargs):
        method = str(method).lower()
        res = None
        if method == 'get':
            res = self.session.request(method, url, params=data, **kwargs)
        else:
            # data = json.dumps(data)
            res = self.session.request(method, url, data=data, **kwargs)
        return res.text


    # def sesion(self):
    #     session = requests.session()
    #     return session

    # def get(self, url, params, headers):
    #     result = self.sesion().get(url=url, params=params, headers=headers)
    #     return result
    #
    # def post(self, url, data, headers):
    #     result = self.sesion().post(url=url, data=data, headers=headers)
    #     return result