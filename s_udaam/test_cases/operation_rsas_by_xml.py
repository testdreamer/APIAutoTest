#-- coding: utf-8 --

#@Time : 2022/11/4 13:37

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : operation_rsas_by_xml.py

#@Software: PyCharm
import requests
import sys
import zipfile, io
import urllib3
import lxml.etree
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
def rsas_create_task(config_xml):
    ##########参数部分，需要根据实际情况修改##########
    # 接口IP
    host = '192.168.8.234'

    # 全局参数配置
    username = 'admin'
    password = 'Nsf0cus@123'
    result_format = 'xml'

    # 请求参数（POST）
    # XML路径


    # 任务类型
    task_type = '8'

    # https://{device_ip}/api/{api_name}?{query_string}
    url = 'https://' + host + '/api/task/create?username=' + username + '&password=' + password + '&format=' + result_format

    bd = open(config_xml,'rb')
    file = {'config_xml':bd}
    data = {'type':'8'}

    response = requests.post(url,data,files=file,verify=False)
    print(response.text)
    task_id = response.text.split('<task_id>')[1].split('</task_id>')[0]
    print(task_id)
    return task_id

def rsas_create_report(task_id):
    # 接口IP
    host = '192.168.8.234'
    # 全局参数配置
    username = 'admin'
    password = 'Nsf0cus@123'
    result_format = 'xml'
    url = 'https://' + host + '/api/generate_report/?username=' + username + '&password=' + password + '&format=' + result_format
    # url = 'https://' + host + '/report/export'
    data = {'task_id':task_id,'report_type':'pdf,html,xls'}
    headers = {
        'Cookie': 'csrftoken=GWmUCsBfM5e339yu2V8AcqDkZdbNiAJ0H5t7tVSVasob5NdxUoS6cIBmeCVwgCPz'
    }
    files = []
    response = requests.post(url, headers=headers, data=data, files=files, verify=False)
    print(response.text)
    report_id = response.text.split('<report_id>')[1].split('</report_id>')[0]
    print(report_id)
    return report_id

def rsas_download_report_zip(report_id,report_type,repotr_path):
    # 接口IP
    host = '192.168.8.234'
    # 全局参数配置
    username = 'admin'
    password = 'Nsf0cus@123'
    result_format = 'xml'
    url = 'https://' + host + '/api/download_report/report_id/'+report_id+'/report_type/'+report_type+'?username=' + username + '&password=' + password + '&format=' + result_format
    payload = {}
    headers = {
        'Cookie': 'csrftoken=GWmUCsBfM5e339yu2V8AcqDkZdbNiAJ0H5t7tVSVasob5NdxUoS6cIBmeCVwgCPz'
    }
    response = requests.get(url, headers=headers, data=payload, verify=False)
    filename = sys.path[1] + '/s_udaam/reports/'
    z = zipfile.ZipFile(io.BytesIO(response.content))
    z.extractall(repotr_path)
    return response.status_code

if __name__ == '__main__':
    rsas_download_report_zip('14','html')