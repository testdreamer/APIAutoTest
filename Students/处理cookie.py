import requests

def login():
    '''获取登录的cookie'''
    url = ''
    data = {'username': '', 'password': ''}
    headers = {"Content-Type": "application/json;charset=UTF-8"}
    r = requests.post(url=url, json=data, headers=headers)
    return r.cookies

def diaoyong_cookie():
    url = ''
    r = requests.get(url=url,cookies=login())
    return r.text

