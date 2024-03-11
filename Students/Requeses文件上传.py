import requests

def loginshuju():
    '''定义一个data数据'''
    data = {'':'','':''}
    return data

def login():
    '''获取登录后返回cookie'''
    r = requests.post(url='',data=loginshuju(),headers={})
    return r.cookies

def uploaddata():
    '''接口参数'''
    data = {}
    return data

def uploadfile():
    '''上传文件接口'''
    r = requests.post(url='',
                      data=uploaddata(),
                      headers={},
                      files={"file":("1.jpg",open(r"C:/1.jpg","rb"),"image/jpeg",{})},
                      cookies=login())
    print(r.status_code)
    print(r.text)


uploadfile()
