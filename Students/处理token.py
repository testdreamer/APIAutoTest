import requests
import unittest
class ApiTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.url = ''
    @classmethod
    def tearDownClass(cls):
        pass

    def write_token(self):
        '''将token信息写入到token.md文件中'''
        data = {'username':'','password':''}
        headers = {"Content-Type": "application/json;charset=UTF-8"}
        r = requests.post(url=self.url,json=data,headers=headers)

        with open('token.md','w') as f:
            f.write(r.json()['token'])

    def read_token(self):
        '''读取token.md中的token信息'''
        with open('token,md','r') as f:
            return f.read()

if __name__ == '__main__':
    unittest.main
