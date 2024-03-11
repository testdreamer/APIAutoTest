#-- coding: utf-8 --

#@Time : 2022/9/2 18:01

#@Author : tianxh

#@Email : tianxh@casking.com.cn

#@File : all_style_template.py

#@Software: PyCharm
import json
def bug_mail_template(bug_id,bug_title,bug_info,pra_result,exp_result,date,time,create_user):
    """
    发送bug邮件模板
    :param bug_id: bug_id
    :param bug_title: bug标题
    :param bug_info: bug信息
    :param pra_result: 实际结果 list   实际结果个数要和期望结果一致,且第一个值必须为code
    :param exp_result: 期望结果 list   期望结果个数要和实际结果一致,且第一个值必须为code
    :param date: 创建日期
    :param time: 创建时间
    :param create_user: 创建人
    :return:
    """
    for a in range(0,len(pra_result)):
        if a==0 and pra_result[a] != exp_result[a]:
            res = '服务器错误!'
            break
        elif a!=0 and pra_result[a] != exp_result[a]:
            if type(pra_result[a]) == list and type(exp_result[a]) == list and not set(exp_result[a]) <= set(pra_result[a]):
                res = '实际返回值没有包含预期返回值!'
            else:
                res = '实际返回值与预期返回值不相等!'
            break
        else:
            res = ''
    template = """<div><div style="padding: 10px 0; border: none; vertical-align: middle;"><strong style="font-size: 16px">联影医疗数据服务有限公司-测试</div><div style="border-collapse: collapse; background-color: #fff; border: 1px solid #cfcfcf; box-shadow: 0 0px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px; font-size:13px;"><div style="padding: 10px; background-color: #F8FAFE; border: none; font-size: 14px; font-weight: 500; border-bottom: 1px solid #e5e5e5;"><a href="http://192.168.13.148:63802/bug-view-"""+bug_id+""".html"style="color: #333; text-decoration: underline;"target="_blank">BUG #"""+bug_id+""""""+bug_title+"""</a></div><div style="padding: 10px; border: none;"><fieldset style="border: 1px solid #e5e5e5"><legend style="color: #114f8e">重现步骤</legend><div style="padding:5px;"><p>[步骤]</p>"""+bug_info+"""<br><p>[结果]</p>"""+res+"""<br>"""+str(pra_result)+"""
<br><p>[期望]</p>"""+str(exp_result)+"""<br></div></fieldset></div><div style="padding: 10px; background-color: #FFF0D5"><span style="font-size: 16px; color: #F1A325">●</span>&nbsp;<span><span style="border-bottom:1px dashed #ccc;"t="5"times=" 13:55">"""+date+"""</span>&nbsp;"""+time+""", 由 <strong>"""+create_user+"""</strong>创建。</span></div></div>"""
    return template

def bug_mail_template_no_compare(bug_id,bug_title,bug_info,res,date,time,create_user):
    """
    发送bug邮件模板
    :param bug_id: bug_id
    :param bug_title: bug标题
    :param bug_info: bug信息
    :param date: 创建日期
    :param time: 创建时间
    :param create_user: 创建人
    :return:
    """

    template = """<div><div style="padding: 10px 0; border: none; vertical-align: middle;"><strong style="font-size: 16px">联影医疗数据服务有限公司-测试</div><div style="border-collapse: collapse; background-color: #fff; border: 1px solid #cfcfcf; box-shadow: 0 0px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px; font-size:13px;"><div style="padding: 10px; background-color: #F8FAFE; border: none; font-size: 14px; font-weight: 500; border-bottom: 1px solid #e5e5e5;"><a href="http://192.168.13.148:63802/bug-view-"""+bug_id+""".html"style="color: #333; text-decoration: underline;"target="_blank">BUG #"""+bug_id+""""""+bug_title+"""</a></div><div style="padding: 10px; border: none;"><fieldset style="border: 1px solid #e5e5e5"><legend style="color: #114f8e">重现步骤</legend><div style="padding:5px;"><p>[步骤]</p>"""+bug_info+"""<br><p>[结果]</p>"""+res+"""<br>
<br><p>[期望]</p><br></div></fieldset></div><div style="padding: 10px; background-color: #FFF0D5"><span style="font-size: 16px; color: #F1A325">●</span>&nbsp;<span><span style="border-bottom:1px dashed #ccc;"t="5"times=" 13:55">"""+date+"""</span> """+time+""", 由 <strong>"""+create_user+"""</strong>创建。</span></div></div>"""
    return template

def bug_mail_template_insert_accessory(href_path,href_name,bug_info,pra_result,exp_result,date,time,create_user):
    """
    发送bug邮件模板
    :param bug_id: bug_id
    :param bug_title: bug标题
    :param bug_info: bug信息
    :param pra_result: 实际结果 list   实际结果个数要和期望结果一致,且第一个值必须为code
    :param exp_result: 期望结果 list   期望结果个数要和实际结果一致,且第一个值必须为code
    :param date: 创建日期
    :param time: 创建时间
    :param create_user: 创建人
    :return:
    """
    for a in range(0,len(pra_result)):
        if a==0 and pra_result[a] != exp_result[a]:
            res = '服务器错误!'
            break
        elif a!=0 and pra_result[a] != exp_result[a]:
            if type(pra_result[a]) == list and type(exp_result[a]) == list and not set(exp_result[a]) <= set(pra_result[a]):
                res = '实际返回值没有包含预期返回值!'
            else:
                res = '实际返回值与预期返回值不相等!'
            break
        else:
            res = ''
    template = """<div><div style="padding: 10px 0; border: none; vertical-align: middle;"><strong style="font-size: 16px">联影医疗数据服务有限公司-测试</div><div style="border-collapse: collapse; background-color: #fff; border: 1px solid #cfcfcf; box-shadow: 0 0px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px; font-size:13px;"><div style="padding: 10px; background-color: #F8FAFE; border: none; font-size: 14px; font-weight: 500; border-bottom: 1px solid #e5e5e5;"><a href="""+href_path+"""style="color: #333; text-decoration: underline;"target="_blank">点击查看测试报告:"""+href_name+"""</a></div><div style="padding: 10px; border: none;"><fieldset style="border: 1px solid #e5e5e5"><legend style="color: #114f8e">重现步骤</legend><div style="padding:5px;"><p>[步骤]</p>"""+bug_info+"""<br><p>[结果]</p>"""+res+"""<br>"""+str(pra_result)+"""
<br><p>[期望]</p>"""+str(exp_result)+"""<br></div></fieldset></div><div style="padding: 10px; background-color: #FFF0D5"><span style="font-size: 16px; color: #F1A325">●</span>&nbsp;<span><span style="border-bottom:1px dashed #ccc;"t="5"times=" 13:55">"""+date+"""</span>&nbsp;"""+time+""", 由 <strong>"""+create_user+"""</strong>创建。</span></div></div>"""
    return template


def result_buginfo_template(case_section,url,request_method,data,r):
    """
    测试报告中显示bug信息的模板
    :param case_section: 测试用例的标题
    :param url: 接口地址
    :param request_method: 请求方法
    :param data: post方法接口参数值
    :param r: 接口返回response
    :return:
    """
    return case_section + '接口URL:' + url + '\n' + '请求方法:' + request_method + '\n' + '参数值:' + str(data) + '\n' + '返回值:' + json.dumps(r.json(), indent=1, ensure_ascii=False)



def mail_buginfo_template(case_section,url,request_method,data,r):
    """
        测试报告中显示bug信息的模板
        :param case_section: 测试用例的标题
        :param url: 接口地址
        :param request_method: 请求方法
        :param get_parameter: get方法接口参数值
        :param data: post方法接口参数值
        :param r: 接口返回response
        :return:
        """
    title = case_section + ":" + url

    if len(json.dumps(r.json(), indent=1, ensure_ascii=False).center(1))>20000:
        content = case_section + '接口URL:' + url + '\n请求方法:' + request_method + '\n' + '参数值:' + str(data) + '\n' + '返回值:' + json.dumps(
        r.json(), indent=1,
        ensure_ascii=False).center(1)[0:20000:1]
    else:
        content = case_section + '接口URL:' + url + '\n请求方法:' + request_method + '\n' + '参数值:' + str(data) + '\n' + '返回值:' + json.dumps(
            r.json(), indent=1,
            ensure_ascii=False).center(1)

    content1 = "<p>" + content.replace("\n", "<br />") + "</p>"
    return title,content1
