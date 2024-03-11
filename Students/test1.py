import requests

#get请求方式
# response=requests.get("https://www.baidu.com")
# print(response.url)

#get请求方式，传递参数
# response=requests.get("https://www.baidu.com",params={'wd':'python'})
# print(response.url)


#发送json格式的post请求
token = 'eyJhbGciOiJIUzI1NiIsInppcCI6IkdaSVAifQ.5HUP/om754ZVK1Oeoyz90DAcqTd3/x0d7FcLo5mHDoe00GjYlG2TN4OuCPcRSXAap5pxPNj/qGle+eKfzP9hRiXOWyQQPKHyCjLXGV+hiXuXRRCrDuFb6n9nJmcSeGNPVyDXQi8TvoFVe2eKuDN2PRp4/4hHpsmY4J3WrvQeAR6L5cwbcB4X/B1XZPEJoxboGvQI9Pi3XUXzP0u51WZbtvtUEYEEluffBUNmDvamCxU=.0t_MiChYZ1_ygwI4F59xKOIJyHy1fTmqHa1WbZAH-aw'
#发送json格式是"Content-Type":"application/json;charset=UTF-8"
#发送Form表单格式是"Content-Type":"application/x-www-form-urlencoded"
#发送XML数据格式是"Content-Type":"text/xml"
headers = {"Content-Type":"application/json;charset=UTF-8","exchange-token":token}
url = 'http://webapi.loex.abc/exchange-web-api/v1/question/create'
payload = {'imageDataStr':'common/image/munxst1601902844462.jpg','rqDescribe':'来打广告','rqType':'1'}
r = requests.post(url=url,json=payload,headers=headers)
print(r.text)

