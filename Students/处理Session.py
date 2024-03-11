import requests

def login():
    data = {}
    url = ''
    headers = {}

    '''requests.Session()方法表示实例化Session对象，保持后续所有发送的请求之间保持session'''
    s = requests.Session()
    r = s.post(url=url,data=data,headers=headers)
    return s


def diaoyong_session():
    data = {}
    url = ''
    headers = {}

    '''其他的接口用到session通过login().post调用session'''
    s = requests.Session()
    r = login().post(url=url, data=data, headers=headers)
    return r.text