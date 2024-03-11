#-- coding: utf-8 --

#@Time : 2022/9/1 14:59

#@Author : zhaopt

#@Email : zhaopt@casking.com.cn

#@File : 多线程连接ws.py

#@Software: PyCharm
import requests
import websocket
import threading
# for a in range(1,10):
    # data = {"code":"00101","access":"c","data":{"clientId":"PDY71184X@sbk001@A101@mdm2007@54467248r9ujcnfd","userId":"mdm2005","userName":"qq","userTypeCode":"A101","orgCode":"PDY71184X","deptCode":"sbk001","empType":"empType","empCode":"empCode","ipAddr":"ipAddr","macAddr":"54467248r9ujcnfd","version":"version"}}
    # r= requests.post('http://192.168.13.159:12171/collaPlat/login/in',{},data)
    # print(r.text)
# data = {"code":"00101","access":"c","data":{"clientId":"PDY71184X@sbk001@A101@mdm2001@54467248r9ujcnfd","userId":"mdm2001","userName":"qq","userTypeCode":"A101","orgCode":"PDY71184X","deptCode":"sbk001","empType":"empType","empCode":"empCode","ipAddr":"ipAddr","macAddr":"54467248r9ujcnfd","version":"version"}}
# r= requests.post('http://192.168.13.159:12171/collaPlat/login/in',{},data)
# print(r.text)
import websockets
import json
# from websocket import create_connection

###/Applications/Python\ 3.9/Install\ Certificates.command

# class WebSockets():
#     def __init__(self, url):
#         self.url = url
#         self.ws = websocket.WebSocket()
#         self.ws.connect(url)
#
#     def send_ws(self,data):
#         ws = websocket.WebSocket()
#         self.ws.send(data)
#         res = self.ws.recv()
#         res1 = self.ws.recv()
#         print(res, res1)
#
#
# if __name__ == '__main__':
#     ws = WebSockets(url='ws://192.168.13.159:12176/udrcpwebsocket?socketId=PDY71184X@sbk001@A101@mdm2005@54467248r9ujcnfd')
#     param_data = {
#
#     }
#     ws.send_ws(data=param_data)
#     ws.close()


# wws = create_connection("ws://192.168.13.159:12176/udrcpwebsocket?socketId=PDY71184X@sbk001@A101@mdm2001@54467248r9ujcnfd")
# print(wws)
# wws = websocket.WebSocketApp("ws://192.168.13.159:12176/udrcpwebsocket?socketId=PDY71184X@sbk001@A101@mdm2001@54467248r9ujcnfd")
# wws.run_forever()
# wws.r

def fun(a):
    """
    使用这个函数需要安装websocket库,websockets库,websocket-client库
    :param a: 用户参数值
    :return:
    """
    print(a)
    client_id = 'PDY71184X@sbk001@A101@mdm' + str(a) + '@54467248r9ujcnfd'
    user_id = 'mdm' + str(a)
    data = {"code": "00101", "access": "c",
            "data": {"clientId": client_id, "userId": user_id, "userName": "qq", "userTypeCode": "A101",
                     "orgCode": "PDY71184X", "deptCode": "sbk001", "empType": "empType", "empCode": "empCode",
                     "ipAddr": "ipAddr", "macAddr": "54467248r9ujcnfd", "version": "version"}}
    r = requests.post('http://192.168.13.159:12171/collaPlat/login/in', {}, data)
    print(r.text)

    ws_url = 'ws://192.168.13.159:12176/udrcpwebsocket?socketId=' + client_id
    wws = websocket.WebSocketApp(ws_url)
    wws.run_forever()


# 创建线程
if __name__ == '__main__':

    for a in range(1001,1003):
        threading.Thread(target=fun, args=(a,)).start()