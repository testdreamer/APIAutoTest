#-- coding: utf-8 --

#@Time : 2022/12/7 13:58

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : register_case.py

#@Software: PyCharm
import xlrd
from HTMLTestRunner import HTMLTestRunner
import requests
import json
import openpyxl
from Utils.getImageverification import *
import pytest
import unittest
from Utils.create_random import *
from Utils.page import *
from Utils.currenttime import *
from Utils.operationyaml import *
from Utils.log import *
from Utils.operation_jsonpath import *
import ddt
import configparser
from Utils.encrypt import *
from Utils.all_style_template import *
from Utils.operation_zentao_mysql import *
from Utils.send_email import *
import sys,os
#excel,获取excel数据
def get_excel_data():

    file_name=sys.path[0] + '/a_CSAM/TestCases/号源池接口脚本用例 - 副本.xls'
#     lst_data_wb = xlrd.open_workbook(file_name)
#     lst_data_sheet = lst_data_wb.sheet_by_index(2)
#     lst_data_sheet_nrow = lst_data_sheet.nrows
#
#     lst_data_sheet_ncol = lst_data_sheet.ncols
#     test_excel_data = []
#     for row in range(lst_data_sheet_nrow):
#         for col in range(lst_data_sheet_ncol):
#             test_excel_data_every = lst_data_sheet.cell_value(row,col)
#             # print(test_excel)
#             test_excel_data.append(test_excel_data_every)
#     return test_excel_data
#
# @test_pytest.mark.parametrize('name',get_excel_data())
# def testc_json(name):
#     print('本次打印的内容：%s'%name)
#

def Read_Excel():
    system_under_test_yaml = sys.path[-1] + '/api_auto_excel/data/system_under_test.yaml'
    system_under_test = read_yaml(system_under_test_yaml,'被测系统')
    # filename = 'http://192.168.13.148:63805/udaam/'+system_under_test+'接口用例脚本.xlsx'
    original_file = sys.path[-1] + '/api_auto_excel/test_cases/'+system_under_test+'接口用例脚本.xlsx'
    # from_wget_download_file(filename, original_file)
    file_name = original_file
    file_name = 'C:\\Users\\Administrator\\Desktop\\号源池接口用例脚本.xlsx'
    book = xlrd.open_workbook(file_name)
    # 通过下标方法读取sheet值
    sheet = book.sheet_by_name('接口用例')
    # 循环读取每行数据
    return [dict(zip(sheet.row_values(0), sheet.row_values(row))) for row in range(1, sheet.nrows)]

def write_excel(rows,values):
    system_under_test_yaml = sys.path[-1] + '/api_auto_excel/data/system_under_test.yaml'
    system_under_test = read_yaml(system_under_test_yaml, '被测系统')
    # filename = 'http://192.168.13.148:63805/udaam/'+system_under_test+'接口用例脚本.xlsx'
    original_file = sys.path[-1] + '/api_auto_excel/test_cases/' + system_under_test + '接口用例脚本.xlsx'
    # from_wget_download_file(filename, original_file)
    file_name = original_file
    file_name = 'C:\\Users\\Administrator\\Desktop\\号源池接口用例脚本.xlsx'
    book = openpyxl.load_workbook(file_name)
    sheet = book['接口用例']
    sheet.cell(rows+1,28 , values)
    book.save(file_name)
    book.close()

def Read_Excel_config():
    system_under_test_yaml = sys.path[-1] + '/api_auto_excel/data/system_under_test.yaml'
    system_under_test = read_yaml(system_under_test_yaml,'被测系统')
    # filename = 'http://192.168.13.148:63805/udaam/'+system_under_test+'接口用例脚本.xlsx'
    original_file = sys.path[-1] + '/api_auto_excel/test_cases/'+system_under_test+'接口用例脚本.xlsx'
    # from_wget_download_file(filename, original_file)
    file_name = original_file
    file_name = 'C:\\Users\\ud\\Desktop\\号源池接口用例脚本.xlsx'
    book = xlrd.open_workbook(file_name)
    # 通过下标方法读取sheet值
    sheet = book.sheet_by_name('配置')
    bug_mail_addressee = sheet.cell_value(1, 1)
    if sheet.cell_value(1, 2) != '':
        bug_mail_cc = sheet.cell_value(1, 2)
    else:
        bug_mail_cc = None
    # 循环读取每行数据
    return bug_mail_addressee,bug_mail_cc

#清除文件
def clear_yaml(self):
    with open(os.getcwd()+"/extract.yaml",mode='w',encoding='utf-8') as f:
        f.truncate()

def bug_mail_and_to_zentao(case_section,mail_title_url,request_method,url,data,response,res,bug_res,mail_addressee,mail_cc):
    print(result_buginfo_template(case_section, url, request_method, data, response))
    title = mail_buginfo_template(case_section, mail_title_url, request_method, data, response)[0]
    content = mail_buginfo_template(case_section, mail_title_url, request_method, data, response)[1]
    bug_to_zentao(res, title, content.replace('\'', '').replace('"', ''), 'zhaop', 'xiaojc')
    bug_id = from_zentaotitle_get_zentaoid(title)
    title_mail = 'BUG #' + str(bug_id) + ' ' + title
    mail_temp = bug_mail_template_no_compare(str(bug_id), title, content, bug_res,
                                  new_time().split(' ')[0], new_time().split(' ')[1], '禅道管理')
    if res == False:
        send_email(mail_addressee, title_mail, mail_temp,cc=mail_cc)
# class Test_01:
#     def Requests_result(self, item):
#         # 封装请求
#         response = requests.request(
#         method=item['请求类型'],
#         url=item['接口地址'],
#         data=json.loads(item['请求参数'])
#         )
#         result = response.text
#         print(result)
#         return result == item['后置处理器']
#
# @test_pytest.mark.parametrize('item', Read_Excel())
# def test_01(self, item):
#     response_result = self.Requests_result(item)
#     # 断言请求返回的结果是否为True
#     assert response_result == True




@ddt.ddt

class Test_01(unittest.TestCase):
    get_times = get_time()
    image_verifications = sys.path[-1] + '/api_auto_excel/image_verification/image_verifications.jpg'
    variable_storage_yaml = sys.path[-1] + '/api_auto_excel/data/variable_storage.yaml'
    result_yaml = sys.path[-1] + '/api_auto_excel/data/resul.yaml'
    clear_yaml(variable_storage_yaml)
    # 定义写入用例文件结果的list,首先写到resul_yamll中
    result_dict = {}
    exec_result_list = []
    mail_addressee = Read_Excel_config()[0]
    mail_cc = Read_Excel_config()[1]
    bug_mail_addressee = str(mail_addressee).split(',')

    if mail_cc != None:
        bug_mail_cc = str(mail_cc).split(',')
    else:
        bug_mail_cc = None
    def requests_result(self, item):
        # 封装请求
        if item['是否执行'] == '是' and item['用例标题'] == '登录,正确':
            data = json.dumps(json.loads(
                str(item['请求参数']).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace('"true"',
                                                                                                     'true')))

            # 获取验证码
            url_yanzhengma = str(item['验证码接口']).replace('get_times',str(self.get_times))
            r = requests.request(method='get',url=url_yanzhengma, data={})
            # # 保存验证码图片
            save_image_verification(self.image_verifications, r)
            # 获取验证码图片的验证码
            # image_verification_code = get_image_verification(uname='liany', pwd='zpt123456789',
            #                                                  img=self.image_verifications, typeid=3)
            image_verification_code = get_image_verification_dddd(self.image_verifications)

            # 密码加密
            rsa_code = encrpt(str(item["登录用户名和密码(','分割)"]).split(',')[1])

            data = eval(str(item['请求参数']).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace(
                    '"true"',
                    'true').replace('验证码',str(image_verification_code)).replace('rsa加密',str(rsa_code)).replace('时间戳',str(self.get_times)))
            headers = eval(item['请求头'])
            response = requests.request(
            method=item['请求类型'],
            url=item['接口地址'],
            data=data,
            headers=headers
            )
            result = response.text
            # 通过['返回的token层级']获取token,并写到配置文件
            # 直接把字符串当做代码运行
            token = eval(item['返回的token层级'])
            project_name = str(item['功能模块']).split('_')[0]
            token_data = {project_name+'token': token}
            write_yaml(self.variable_storage_yaml, token_data)
            log.info("token写入yaml成功")
            # 断言,首先判断断言类型
            verify_field_list = str(item['校验字段']).split(',')
            verify_field_result_list = []
            verify_value_list = str(item['校验值']).split(',')
            true_false_list = []

            if item['断言类型'] == '相等':
                for a in range(0,len(verify_field_list)):
                    verify_field_result_list.append(str(eval(verify_field_list[a])))
                    true_false_list.append(verify_field_result_list[a] == verify_value_list[a])
                if False not in true_false_list:
                    # self.exec_result_list.append({item['用例编号']:'通过'})
                    write_excel(int(item['序列号']), '通过')
                    return True
                else:
                    # 通过true_false_list中False的位置找到校验字段中是哪个返回值
                    false_cause = verify_field_list[true_false_list.index(False)] + '返回值与预期值不相等!'
                    # 将值添加到dict中
                    write_excel(int(item['序列号']),'不通过--'+false_cause)
                    false_cause_mail = '断言类型:相等' + false_cause + '(实际结果:' + str(
                        eval(verify_field_list[true_false_list.index(False)])) + ',预期结果:' + str(
                        verify_value_list[true_false_list.index(False)])+')'
                    bug_mail_and_to_zentao(item['用例标题'],item['接口地址'].split('?')[0],item['请求类型'],item['接口地址'],data,response,False,false_cause_mail,self.bug_mail_addressee,self.bug_mail_cc)
                    return False

            elif item['断言类型'] == '不相等':
                for a in range(0,len(verify_field_list)):
                    verify_field_result_list.append(str(eval(verify_field_list[a])))
                    true_false_list.append(verify_field_result_list[a] != verify_value_list[a])
                if False not in true_false_list:
                    # self.exec_result_dict.update({item['用例编号']:'通过'})
                    write_excel(int(item['序列号']), '通过')
                    return True
                else:
                    # 通过true_false_list中False的位置找到校验字段中是哪个返回值
                    false_cause = verify_field_list[true_false_list.index(False)] + '返回值与预期值相等!'
                    # 将值添加到dict中
                    # self.exec_result_dict.update({item['用例编号']: '不通过--'+false_cause})
                    write_excel(int(item['序列号']), '不通过--' + false_cause)
                    false_cause_mail = '断言类型:不相等' + false_cause + '(实际结果:' + str(
                        eval(verify_field_list[true_false_list.index(False)])) + ',预期结果:' + str(
                        verify_value_list[true_false_list.index(False)])+')'
                    bug_mail_and_to_zentao(item['用例标题'], item['接口地址'].split('?')[0], item['请求类型'], item['接口地址'], data,
                                           response, False, false_cause_mail, self.bug_mail_addressee, self.bug_mail_cc)
                    return False
            elif item['断言类型'] == '包含':
                verify_scope = str(eval(item['校验字段']))
                verify_value = str(item['校验值']).split(',')
                for a in range(0,len(str(item['校验值']).split(','))):
                    true_false_list.append(str(verify_value[a]).replace("'",'').replace('"','').replace(' ','') in verify_scope.replace("'",'').replace('"','').replace(' ',''))

                if False not in true_false_list:
                    # self.exec_result_dict.update({item['用例编号']:'通过'})
                    write_excel(int(item['序列号']), '通过')

                    return True
                else:
                    # 将值添加到dict中
                    # self.exec_result_dict.update({item['用例编号']: '不通过--返回值中不包含预期值!'})
                    write_excel(int(item['序列号']), '不通过--返回值中不包含预期值!')
                    false_cause_mail = '断言类型:包含.返回值中不包含预期结果:' + str(
                        verify_value_list[true_false_list.index(False)])+')'
                    bug_mail_and_to_zentao(item['用例标题'], item['接口地址'].split('?')[0], item['请求类型'], item['接口地址'], data,
                                           response, False, false_cause_mail, self.bug_mail_addressee, self.bug_mail_cc)
                    return False
            elif item['断言类型'] == '不包含':
                verify_scope = str(eval(item['校验字段']))
                verify_value = str(item['校验值']).split(',')
                for a in range(0, len(str(item['校验值']).split(','))):
                    true_false_list.append(str(verify_value[a]).replace("'", '').replace('"', '').replace(' ',
                                                                                                          '') not in verify_scope.replace(
                        "'", '').replace('"', '').replace(' ', ''))

                if False not in true_false_list:
                    # self.exec_result_dict.update({item['用例编号']: '通过'})
                    write_excel(int(item['序列号']), '通过')

                    return True
                else:
                    # 将值添加到dict中
                    # self.exec_result_dict.update({item['用例编号']: '不通过--返回值中不包含预期值!'})
                    write_excel(int(item['序列号']), '不通过--返回值中包含预期值!')
                    false_cause_mail = '断言类型:不包含.返回值中包含预期结果:' + str(
                        verify_value_list[true_false_list.index(False)])+')'
                    bug_mail_and_to_zentao(item['用例标题'], item['接口地址'].split('?')[0], item['请求类型'], item['接口地址'], data,
                                           response, False, false_cause_mail, self.bug_mail_addressee, self.bug_mail_cc)
                    return False
            else:
                return '断言类型中只能输入"相等","不相等","包含","不包含",四个值!'

            # return token
            # return result
            # result = item['后置处理器']
            # return result == item['后置处理器']
        elif item['是否执行'] == '是' and item['用例标题'] != '登录,正确':
            # 获取token
            project_name = str(item['功能模块']).split('_')[0]
            size = os.path.getsize(self.variable_storage_yaml)
            if size != 0:
                token = read_yaml(self.variable_storage_yaml,project_name+'token')
            else:
                token = ''
            # 获取随机数位数
            english_random_num = eval(item['随机数位数和日期格式'])['字母随机数']
            chinese_random_num = eval(item['随机数位数和日期格式'])['汉字随机数']
            num_random_num = eval(item['随机数位数和日期格式'])['数字随机数']
            chn_eng_random_num = eval(item['随机数位数和日期格式'])['汉字字母混合随机数']
            eng_num_random_num = eval(item['随机数位数和日期格式'])['字母数字混合随机数']
            # 根据位数获取验证码
            english_random = create_letter(int(english_random_num))
            chinese_random = create_chinese(int(chinese_random_num))
            num_random = create_num(int(num_random_num))
            chn_eng_random = create_chn_eng(int(chn_eng_random_num))
            eng_num_random = create_eng_num(int(eng_num_random_num))
            # 获取日期格式
            current_date_format = eval(item['随机数位数和日期格式'])['当前日期']
            before_date_format = eval(item['随机数位数和日期格式'])['以前日期']
            after_date_format = eval(item['随机数位数和日期格式'])['以后日期']
            # 根据日期格式获取日期
            current_date = time.strftime(current_date_format)
            after_one_day = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime(after_date_format)
            before_one_day = (datetime.datetime.now() - datetime.timedelta(days=1)).strftime(before_date_format)

            # 参数替换
            if item['请求参数'] != '' and item['请求参数值引用'] == '':
                data = json.dumps(json.loads(str(item['请求参数']).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace(
                        '"true"','true').replace('token',str(token)).replace('字母随机数',english_random).replace('汉字随机数',chinese_random)
                                             .replace('数字随机数',num_random).replace('汉字字母混合随机数',chn_eng_random)
                                             .replace('字母数字混合随机数',eng_num_random).replace('时间戳',str(self.get_times))
                                             .replace('当前日期',str(current_date)).replace('以前日期',str(before_one_day))
                                             .replace('以后日期',str(after_one_day))))
            elif item['请求参数'] != '' and item['请求参数值引用'] != '':
                data = json.dumps(json.loads(
                    str(item['请求参数']).replace('None', '""').replace("'", "\"").replace('"null"', 'null').replace(
                        '"true"', 'true').replace('token', str(token)).replace('字母随机数', english_random).replace('汉字随机数',
                                                                                                           chinese_random)
                    .replace('数字随机数', num_random).replace('汉字字母混合随机数', chn_eng_random)
                    .replace('字母数字混合随机数', eng_num_random).replace('时间戳', str(self.get_times))
                    .replace('当前日期', str(current_date)).replace('以前日期', str(before_one_day))
                    .replace('以后日期', str(after_one_day))))
                data = json.loads(data)
                parameter_reference_dict = json.loads(item['请求参数值引用'])
                for key in parameter_reference_dict:

                    # 循环读取对应的值
                    var_val = read_yaml(self.variable_storage_yaml, project_name + '_'+str(parameter_reference_dict[key]))
                    data[key] = str(var_val)
                data = json.dumps(json.loads(
                    str(data).replace('None', '"null"').replace("'", "\"").replace('"null"', 'null').replace(
                        'True', '"true"').replace(
                        'False', '"false"')))
            else:
                data = {}
            if item['请求头'] != '':
                headers = eval(str(item['请求头']).replace('token',str(token)))
            else:
                headers = {}
            if item['接口地址参数引用'] != '':
                url = str(item['接口地址'])
                parameter_reference_dict = json.loads(item['接口地址参数引用'])
                for key in parameter_reference_dict:
                    # 循环读取对应的值
                    var_val = read_yaml(self.variable_storage_yaml, project_name + '_'+str(parameter_reference_dict[key]))
                    url = url.replace(str(key),str(var_val))


            else:
                url = str(item['接口地址'])
            response = requests.request(
                method=item['请求类型'],
                url=url,
                data=data,
                headers=headers
            )
            result = response.text

            # 判断是否有后置处理器
            if item['后置处理器'] != '':
                # 如果有就存到variable_storage.yaml文件中
                project_name = str(item['功能模块']).split('_')[0]
                case_num = str(item['用例编号'])
                # 解析后置处理器内容
                post_processor_dict = {}
                for key in json.loads(item['后置处理器']):
                    if 'response.json()' in json.loads(item['后置处理器'])[key]:
                        post_processor_dict.update({project_name+'_'+item['用例编号']+'_'+key: eval(json.loads(item['后置处理器'])[key])})
                    elif '精确查找' in key:
                        assign_key = str(json.loads(item['后置处理器'])[key]).split('@')[0]
                        json_path = str(json.loads(item['后置处理器'])[key]).split('@')[1]
                        # 获取指定位置的返回值
                        assign_return = get_json_assign_field(response,assign_key,json_path)
                        post_processor_dict.update(
                            {project_name + '_' + item['用例编号'] + '_' + assign_key: assign_return})
                    else:
                        post_processor_dict.update(
                            {project_name + '_' + item['用例编号'] + '_' + key: str(json.loads(item['后置处理器'])[key])})

                # case = read_yaml_no_key(self.variable_storage_yaml)
                # post_processor_dict_title = {project_name + '后置处理器': post_processor_dict}
                # case[project_name + '后置处理器'][project_name+'_'+item['用例编号']+'_'+key] = eval(json.loads(item['后置处理器'])[key])
                write_yaml_add(self.variable_storage_yaml, post_processor_dict)

            # return result
            # 断言,首先判断断言类型
            verify_field_list = str(item['校验字段']).split(',')
            verify_field_result_list = []
            verify_value_list = str(item['校验值']).split(',')
            true_false_list = []

            if item['断言类型'] == '相等':
                for a in range(0, len(verify_field_list)):
                    verify_field_result_list.append(str(eval(verify_field_list[a])))
                    true_false_list.append(verify_field_result_list[a] == verify_value_list[a])

                if False not in true_false_list:
                    # self.exec_result_dict.update({item['用例编号']: '通过'})
                    write_excel(int(item['序列号']), '通过')

                    return True

                else:
                    # 通过true_false_list中False的位置找到校验字段中是哪个返回值
                    false_cause = verify_field_list[true_false_list.index(False)] + '返回值与预期值不相等!'
                    # 将值添加到dict中
                    # self.exec_result_dict.update({item['用例编号']: '不通过--' + false_cause})
                    write_excel(int(item['序列号']), '不通过--' + false_cause)
                    false_cause_mail = '断言类型:相等' + false_cause + '(实际结果:' + str(
                        eval(verify_field_list[true_false_list.index(False)])) + ',预期结果:' + str(
                        verify_value_list[true_false_list.index(False)])+')'
                    bug_mail_and_to_zentao(item['用例标题'], item['接口地址'].split('?')[0], item['请求类型'], item['接口地址'], data,
                                           response, False, false_cause_mail, self.bug_mail_addressee, self.bug_mail_cc)
                    return False

            elif item['断言类型'] == '不相等':
                for a in range(0, len(verify_field_list)):
                    verify_field_result_list.append(str(eval(verify_field_list[a])))
                    true_false_list.append(verify_field_result_list[a] != verify_value_list[a])
                if False not in true_false_list:
                    # self.exec_result_dict.update({item['用例编号']: '通过'})
                    write_excel(int(item['序列号']), '通过')

                    return True
                else:
                    # 通过true_false_list中False的位置找到校验字段中是哪个返回值
                    false_cause = verify_field_list[true_false_list.index(False)] + '返回值与预期值相等!'
                    # 将值添加到dict中
                    # self.exec_result_dict.update({item['用例编号']: '不通过--' + false_cause})
                    write_excel(int(item['序列号']), '不通过--' + false_cause)
                    false_cause_mail = '断言类型:不相等' + false_cause + '(实际结果:' + str(
                        eval(verify_field_list[true_false_list.index(False)])) + ',预期结果:' + str(
                        verify_value_list[true_false_list.index(False)])+')'
                    bug_mail_and_to_zentao(item['用例标题'], item['接口地址'].split('?')[0], item['请求类型'], item['接口地址'], data,
                                           response, False, false_cause_mail, self.bug_mail_addressee, self.bug_mail_cc)
                    return False
            elif item['断言类型'] == '包含':
                verify_scope = str(eval(item['校验字段']))
                verify_value = str(item['校验值']).split(',')
                for a in range(0, len(str(item['校验值']).split(','))):
                    true_false_list.append(
                        str(verify_value[a]).replace("'", '').replace('"', '').replace(' ', '') in verify_scope.replace(
                            "'", '').replace('"', '').replace(' ', ''))

                if False not in true_false_list:
                    # self.exec_result_dict.update({item['用例编号']: '通过'})
                    write_excel(int(item['序列号']), '通过')

                    return True
                else:
                    # 将值添加到dict中

                    # self.exec_result_dict.update({item['用例编号']: '不通过--返回值中不包含预期值!'})
                    write_excel(int(item['序列号']), '不通过--返回值中不包含预期值!')
                    false_cause_mail = '断言类型:包含.返回值中不包含预期结果:' + str(
                        verify_value_list[true_false_list.index(False)])+')'
                    bug_mail_and_to_zentao(item['用例标题'], item['接口地址'].split('?')[0], item['请求类型'], item['接口地址'], data,
                                           response, False, false_cause_mail, self.bug_mail_addressee, self.bug_mail_cc)
                    return False
            elif item['断言类型'] == '不包含':
                verify_scope = str(eval(item['校验字段']))
                verify_value = str(item['校验值']).split(',')
                for a in range(0, len(str(item['校验值']).split(','))):
                    true_false_list.append(str(verify_value[a]).replace("'", '').replace('"', '').replace(' ',
                                                                                                          '') not in verify_scope.replace(
                        "'", '').replace('"', '').replace(' ', ''))

                if False not in true_false_list:
                    # self.exec_result_dict.update({item['用例编号']: '通过'})
                    write_excel(int(item['序列号']), '通过')

                    return True
                else:
                    # 将值添加到dict中
                    # self.exec_result_dict.update({item['用例编号']: '不通过--返回值中不包含预期值!'})
                    write_excel(int(item['序列号']), '不通过--返回值中包含预期值!')
                    false_cause_mail = '断言类型:不包含.返回值中包含预期结果:' + str(
                        verify_value_list[true_false_list.index(False)])+')'
                    bug_mail_and_to_zentao(item['用例标题'], item['接口地址'].split('?')[0], item['请求类型'], item['接口地址'], data,
                                           response, False, false_cause_mail, self.bug_mail_addressee, self.bug_mail_cc)
                    return False
            else:
                return '断言类型中只能输入"相等","不相等","包含","不包含",四个值!'

        else:
            return item['用例编号'] + '不执行'
# 通过ddt进行读取数据

    @ddt.data(*Read_Excel())

    def test_01(self, data):
        # print('hhhhh'+str(data))
        response_result = self.requests_result(data)
        #
        self.assertTrue(response_result)
        print(response_result)
# if __name__ == '__main__':
#     sdir = sys.path[0] + '/api_auto_excel/business/'
#     testlist = unittest.defaultTestLoader.discover(start_dir=sdir, pattern='register_case.py')
#     now = time.strftime("%Y-%m-%d_%H:%M:%S")
#     # filename = 'result.html'
#     # filename = test_report + "\\" + now +'result.html'
#     filename = sys.path[-1] + "/" + 'result.html'
#     fp = open(filename, 'wb')
#
#     runner = HTMLTestRunner(
#         stream=fp,  # 文件
#         verbosity=2,
#         title="身份认证系统接口自动化测试报告",  # 标题
#         description=u"系统环境：Liunx 用例执行情况："  # 描述
#     )
#     runner.run(testlist)  # 启动测试套件
#     fp.close()
