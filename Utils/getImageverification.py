#-- coding: utf-8 --

#@Time : 2022/7/11 10:43

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : getImageverification.py

#@Software: PyCharm
import base64
import json
import requests
import sys,os
import ddddocr
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))

def save_image_verification(image,r):
    """
    保存验证码图片
    :param image: 保存验证码的url
    :param r: requests.models.Response
    :return: No
    """
    with open(image, 'wb') as fw:
        fw.write(r.content)
#
# '''
# 获取图片验证码
# image为图片的url
# '''
def get_image_verification_dddd(image):
    ocr = ddddocr.DdddOcr()
    with open(image, 'rb') as f:
        img_bytes = f.read()
        res = ocr.classification(img_bytes)
    return (res)




def get_image_verification(uname, pwd, img, typeid):
    """
    :param uname: 网站用户名
    :param pwd: 网站密码
    :param img: 图片url
    :param typeid: 图片类型
    :return: 验证码
    """
    # 一、图片文字类型(默认 3 数英混合)：
    # 1 : 纯数字
    # 1001：纯数字2
    # 2 : 纯英文
    # 1002：纯英文2
    # 3 : 数英混合
    # 1003：数英混合2
    #  4 : 闪动GIF
    # 7 : 无感学习(独家)
    # 11 : 计算题
    # 1005:  快速计算题
    # 16 : 汉字
    # 32 : 通用文字识别(证件、单据)
    # 66:  问答题
    # 49 :recaptcha图片识别
    # 二、图片旋转角度类型：
    # 29 :  旋转类型
    #
    # 三、图片坐标点选类型：
    # 19 :  1个坐标
    # 20 :  3个坐标
    # 21 :  3 ~ 5个坐标
    # 22 :  5 ~ 8个坐标
    # 27 :  1 ~ 4个坐标
    # 48 : 轨迹类型
    #
    # 四、缺口识别
    # 18 : 缺口识别（需要2张图 一张目标图一张缺口图）
    # 33 : 单缺口识别（返回X轴坐标 只需要1张图）
    # 五、拼图识别
    # 53：拼图识别
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "typeid": typeid, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/predict", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]
