#-- coding: utf-8 --

#@Time : 2022/12/6 14:25

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : operation_jsonpath.py

#@Software: PyCharm
import jsonpath
def get_json_assign_field(respones,assign_key,json_path):
    """
    通过jsonpath返回指定的值
    :param respones: 返回的json
    :param assign_key: 指定的key
    :param json_path: json_path
    :return: 指定的key的value
    """
    json_path = json_path.replace("'",'"')
    json_path = '$.'+json_path.split('[]')[0]+'[?(@.'+json_path.split('[]')[1]+')]'
    return_json = jsonpath.jsonpath(respones.json(), json_path)
    return return_json[0][assign_key]
