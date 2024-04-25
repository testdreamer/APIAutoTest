# _*_ coding : utf_8 _*_
# @Time : 18:18 
# @Author : 田霄汉
# @File : RequestsUtils
# @Project : APIAutoTest
# @User : Administrator
import json

import requests


class RequestsUtils():

    # 类变量：通过类名访问
    session = requests.session()

    def send_request(self, method, url, data, **kwargs):
        method = str(method).lower()
        # res = None
        if method == 'get':
            res = self.session.request(method, url, params=data, **kwargs)
        else:
            # data = json.dumps(data)
            res = self.session.request(method, url, data=data, **kwargs)
        return res.text