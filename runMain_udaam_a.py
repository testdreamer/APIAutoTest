#coding:utf-8

#@Time : 2022/6/2 18:41

#@Author : tianxh

#@Email : 729560832@qq.com

#@File : runMain_udaam_a.py

#@Software: PyCharm
import sys,os
sys.path.append((os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))))
# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(r"E:/pyobject/seleniumTest/testCases")
from a_udaam.TestCases.test_udaam_login import *
from a_udaam.TestCases.test_udaam_applicationclassification import *
from a_udaam.TestCases.test_udaam_resourcemanagement import *
from a_udaam.TestCases.test_udaam_vendormanagement import *
from a_udaam.TestCases.test_udaam_applicationroles import *
from a_udaam.TestCases.test_udaam_internalapplication import *
from a_udaam.TestCases.test_udaam_thirdpartyapplications import *
from a_udaam.TestCases.test_udaam_menumanagement import *
from a_udaam.TestCases.test_udaam_platrole import *
from a_udaam.TestCases.test_udaam_applicationroles import *
from a_udaam.TestCases.test_udaam_personnelmanagement import *
from a_udaam.TestCases.test_udaam_useraccountmanagement import *
from a_udaam.TestCases.test_udaam_organmanmge import *
from a_udaam.TestCases.test_udaam_divisionmanagement import *
from a_udaam.TestCases.test_udaam_loginlog import *
from a_udaam.TestCases.test_udaam_reportforms import *
from a_udaam.TestCases.test_udaam_system_setting import *
from a_udaam.TestCases.test_udaam_sysresourcesconfig import *
from a_udaam.TestCases.test_udaam_logout import *
from Utils.copy_and_clear_file import *
from Utils.get_html_data import *
# from Utils.operation_pdf import *
from Utils.operation_remote_server import *
import time
import unittest
import yagmail
from HTMLTestRunner import HTMLTestRunner
from Utils.log import *
from Utils.operationyaml import *

def new_file(test_dir):
    result_dir = test_dir
    lists = os.listdir(result_dir)     #print(lists)   #列出测试报告目录下的所有文件
    lists.sort()                                       #从小到大排序 文件
    file = [x for x in lists if x.endswith('.html')]   #for循环遍历以.html格式的测试报告
    file_path = os.path.join(result_dir,file[-1])      #找到测试报告目录下最新的测试报告
    return file_path

if __name__ == '__main__':
    base_dir = os.path.dirname(os.path.realpath(__file__))                    #获取文件所在路径
    pro_dir = os.path.dirname(os.path.realpath(__file__)).split('seleniumTest')[0]               #项目所在路径
    test_dir = os.path.join(base_dir)                                                #测试用例所在目录
    test_report = os.path.join(pro_dir,'Reports')   #测试报告所在目录
    log.info(sys.path[-1])
    # test_report = test_dir+'\\result.html'

    # test_report = sys.path[-1]
    # test_report = sys.path[-19]+'\Reports'
    '''跑testCases包下的所有测试用例'''
    # testlist = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')
    '''跑指定文件下的测试用例'''
    testlist = unittest.TestSuite()
    #记录用例执行前的时间
    get_times_start = get_time()
    get_times_start_ymd = new_time()
    #从中间服务器中下载配置文件到本地(中间服务器的配置文件用于开发编辑使用)
    # file_download_linux('192.168.13.197','root','UDtest@1234','/usr/local/udaamAutoTestConfigfile/select_run_cases.yaml',sys.path[-1] + '/a_udaam/data/select_run_cases.yaml')
    # filename = 'http://192.168.13.148:63805/udaam/udaam-apiauto-runcase-config.yaml?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAIOSFODNN7EXAMPLE%2F20220812%2F%2Fs3%2Faws4_request&X-Amz-Date=20220812T090855Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Signature=e0c6a3051f97566ad53e10328e602c741f4c553c946014157a1eb36baadfa97d'
    # 从云帮平台中下载配置文件到本地(中间服务器的配置文件用于开发编辑使用)
    # filename = 'http://192.168.13.148:63805/udaam/udaam-apiauto-runcase-config.yaml'
    # original_file = sys.path[-1] + '/a_udaam/data/select_run_cases.yaml'
    # from_wget_download_file(filename,original_file)
    # #获取开发编辑的配置文件地址,获取对比文件地址,获取实际运行的文件地址
    # original_file = sys.path[-1] + '/a_udaam/data/select_run_cases.yaml'
    # copy_file = sys.path[-1] + '/a_udaam/data/practical_select_run.yaml'
    # run_file = sys.path[-1] + '/a_udaam/data/run_cases.yaml'
    # #读取开发编辑的配置文件&读取对比文件
    # select_s = read_yaml_no_key(original_file)
    # practical_s = read_yaml_no_key(copy_file)
    # #通过对比开发编辑的配置文件和对比文件判断是否有增加配置,如果有把新增加的部分写到实际运行的配置文件中
    # if len(select_s)-len(practical_s)!=0:
    #     write_yaml(run_file,select_s[len(practical_s)::1])
    # else:
    #     pass
    # #复制开发编辑的配置文件内容到对比文件
    # copyfile_yaml(original_file, copy_file)
    #读取实际运行的配置文件
    # s = read_yaml_no_key(run_file)
    s = ['菜单管理','平台角色','部门管理','登录日志','统计分析','系统资源配置','基础设置']
    # s = ['登录日志']
    print(s)
    if '资源管理'in s or '厂商管理'in s or '应用分类'in s or '内部应用'in s or '第三方应用'in s or '菜单管理'in s:

        #登录
        testlist.addTest(Login("test_login"))
        # #资源系统管理-资源管理
        testlist.addTest(ResourceManagement("test_query_resource_list"))
        testlist.addTest(ResourceManagement("test_example_query_system_resource_list"))
        # #资源系统管理-厂商管理
        testlist.addTest(VendorManagement("test_query_all_vendor"))
        testlist.addTest(VendorManagement("test_new_vendors"))
        testlist.addTest(VendorManagement("test_vendor_list"))
        testlist.addTest(VendorManagement("test_update_vendor"))
        testlist.addTest(VendorManagement("test_vendor_disable_enable"))
        #资源系统管理-应用分类
        testlist.addTest(ApplicationClassification("test_app_classify_tree_query"))
        testlist.addTest(ApplicationClassification("test_app_classifi_insert"))
        testlist.addTest(ApplicationClassification("test_app_classifi_query"))
        testlist.addTest(ApplicationClassification("test_app_classifi_update"))
        #资源系统管理-内部应用
        testlist.addTest(InternalApplication("test_resource_discovery"))
        # testlist.addTest(InternalApplication("test_insert_internal_app"))
        # testlist.addTest(InternalApplication("test_internalapp_Info"))
        # testlist.addTest(InternalApplication("test_internalapp_update"))
        # testlist.addTest(InternalApplication("test_resource_discovery"))
        # testlist.addTest(InternalApplication("test_many_institutions_app_list"))
        # testlist.addTest(InternalApplication("test_many_org_list"))
        # #资源系统管理-第三方应用
        testlist.addTest(ThirdPartyApplications("test_insert_third_part_app"))
        testlist.addTest(ThirdPartyApplications("test_query_third_party_app_classifi"))
        testlist.addTest(ThirdPartyApplications("test_query_third_party_app"))
        testlist.addTest(ThirdPartyApplications("test_update_third_party_app"))
        # #资源系统管理-菜单管理
        testlist.addTest(MenuManagement("test_query_all_system_resources"))
        testlist.addTest(MenuManagement("test_insert_module_dir"))
        testlist.addTest(MenuManagement("test_insert_module_menu"))
        testlist.addTest(MenuManagement("test_insert_module_btn"))
        testlist.addTest(MenuManagement("test_query_system_resources"))
        testlist.addTest(MenuManagement("test_update_module"))
        testlist.addTest(MenuManagement("test_disable_menu"))
        testlist.addTest(MenuManagement("test_disable_btn"))
        # 菜单管理-删除组件按钮
        testlist.addTest(MenuManagement("test_delete_module_btn"))
        # 菜单管理-删除组件菜单
        testlist.addTest(MenuManagement("test_delete_module_menu"))
        # 菜单管理-删除组件目录
        testlist.addTest(MenuManagement("test_delete_module_dir"))
        # 第三方应用-删除第三方应用
        testlist.addTest(ThirdPartyApplications("test_delete_third_party_app"))
        # 内部应用-删除第内部应用
        testlist.addTest(InternalApplication("test_internal_app_delete"))
        # 应用分类-应用分类删除
        testlist.addTest(ApplicationClassification("test_app_classifi_delete"))
        # 厂商管理-厂商删除
        testlist.addTest(VendorManagement("test_vendor_delete"))
    if '平台角色'in s or '应用角色'in s or '人员管理'in s or '用户账号管理'in s:

        # 登录
        testlist.addTest(Login("test_login"))
        # 人员权限管理-平台角色
        testlist.addTest(PlatRoles("test_add_plat_role_types"))
        testlist.addTest(PlatRoles("test_query_plat_role_types"))
        testlist.addTest(PlatRoles("test_query_loadpermission_tree"))
        testlist.addTest(PlatRoles("test_add_plat_role"))
        testlist.addTest(PlatRoles("test_query_plat_role"))
        testlist.addTest(PlatRoles("test_update_plat_role"))
        testlist.addTest(PlatRoles("test_query_platrole_perm"))
        # 人员权限管理-应用角色
        testlist.addTest(ApplicationRoles("test_query_app_list"))
        testlist.addTest(ApplicationRoles("test_query_role_by_system"))
        testlist.addTest(ApplicationRoles("test_arpcqpoars"))
        testlist.addTest(ApplicationRoles("test_arpqrprs"))
        testlist.addTest(ApplicationRoles("test_app_list"))
        # testlist.addTest(ApplicationRoles("test_batch_role_auth_orization"))
        # 人员权限管理-人员管理
        testlist.addTest(PersonnelManagement("test_create_userinfo"))
        testlist.addTest(PersonnelManagement("test_staffconditionenquir_byname"))
        testlist.addTest(PersonnelManagement("test_query_all_role_sandtypes"))
        testlist.addTest(PersonnelManagement("test_query_user_grant_org"))
        testlist.addTest(PersonnelManagement("test_user_role_auth_org"))
        testlist.addTest(PersonnelManagement("test_user_role_auth_role"))
        testlist.addTest(PersonnelManagement("test_query_user_bound_org_list"))
        testlist.addTest(PersonnelManagement("test_query_org_div_list"))
        testlist.addTest(PersonnelManagement("test_query_own_role"))
        testlist.addTest(PersonnelManagement("test_query_org_list"))
        testlist.addTest(PersonnelManagement("test_query_own_resource"))
        testlist.addTest(PersonnelManagement("test_isattr_query_sys_list"))
        testlist.addTest(PersonnelManagement("test_update_role_auth"))
        testlist.addTest(PersonnelManagement("test_user_data_auth_query_sys_list"))
        testlist.addTest(PersonnelManagement("test_user_data_auth_org_list"))
        testlist.addTest(PersonnelManagement("test_user_data_auth_relation_org"))
        testlist.addTest(PersonnelManagement("test_user_data_auth_query_div_list"))
        testlist.addTest(PersonnelManagement("test_account_control_query_sys_list"))
        testlist.addTest(PersonnelManagement("test_user_data_auth_query_sys_list"))
        testlist.addTest(PersonnelManagement("test_user_data_auth_org_list"))
        testlist.addTest(PersonnelManagement("test_user_data_auth_relation_org"))
        testlist.addTest(PersonnelManagement("test_user_data_auth_query_div_list"))
        testlist.addTest(PersonnelManagement("test_account_control_query_sys_list"))
        testlist.addTest(PersonnelManagement("test_user_grant_org_delete"))
        testlist.addTest(PersonnelManagement("test_user_info"))
        # 人员权限管理-用户账号管理
        testlist.addTest(UserAccountManagement("test_selectusercondition_byname"))
        testlist.addTest(UserAccountManagement("test_insert_username"))
        testlist.addTest(UserAccountManagement("test_select_account"))
        testlist.addTest(UserAccountManagement("test_account_details"))
        testlist.addTest(UserAccountManagement("test_account_stop"))
        testlist.addTest(UserAccountManagement("test_account_start"))
        testlist.addTest(UserAccountManagement("test_account_lock"))
        testlist.addTest(UserAccountManagement("test_update_account"))
        testlist.addTest(UserAccountManagement("test_reset_password"))
        # 人员权限管理-用户账号管理-删除用户账号
        testlist.addTest(UserAccountManagement("test_delete_useraccount"))
        # 人员权限管理-人员管理-删除用户信息
        testlist.addTest(PersonnelManagement("test_delete_userinfo"))
        # 人员权限管理-平台角色-删除平台角色
        testlist.addTest(PlatRoles("test_delete_plat_role"))
        # 人员权限管理-平台角色-删除平台角色类型
        testlist.addTest(PlatRoles("test_delete_plat_role_type"))


    if '部门管理' in s or '机构管理' in s:

        # 登录
        testlist.addTest(Login("test_login"))
        # 基础数据管理-机构管理
        testlist.addTest(OrgManagement("test_insert_org"))
        testlist.addTest(OrgManagement("test_query_org_tree"))
        testlist.addTest(OrgManagement("test_query_org_list"))
        testlist.addTest(OrgManagement("test_org_close"))
        testlist.addTest(OrgManagement("test_org_open"))
        testlist.addTest(OrgManagement("test_order_details"))
        testlist.addTest(OrgManagement("test_order_details"))

        # 基础数据管理-部门管理
        testlist.addTest(DivisionManagement("test_query_org_tree"))
        testlist.addTest(DivisionManagement("test_insert_division"))
        testlist.addTest(DivisionManagement("test_query_division_list"))
        # testlist.addTest(DivisionManagement("test_update_division"))
        testlist.addTest(DivisionManagement("test_org_close"))
        testlist.addTest(DivisionManagement("test_org_open"))
        testlist.addTest(DivisionManagement("test_query_division_list"))
        # 基础数据管理-删除部门
        testlist.addTest(DivisionManagement("test_delete_division"))
        # 基础数据管理-删除机构
        testlist.addTest(OrgManagement("test_org_close"))
        testlist.addTest(OrgManagement("test_delete_org"))

    if '登录日志' in s:

        # 登录
        testlist.addTest(Login("test_login"))
        # 系统监控 登录日志
        testlist.addTest(Test_Loginlog("test_loginloglist_right"))
        testlist.addTest(Test_Loginlog("test_loginloglist_noallid1"))
        testlist.addTest(Test_Loginlog("test_loginloglist_noallid2"))
        testlist.addTest(Test_Loginlog("test_loginloglist_noallid3"))
        testlist.addTest(Test_Loginlog("test_menuOpLoglist_right"))
        testlist.addTest(Test_Loginlog("test_menuOpLoglist_noallid1"))
        testlist.addTest(Test_Loginlog("test_menuOpLoglist_noallid2"))
        testlist.addTest(Test_Loginlog("test_menuOpLoglist_noallid3"))
        testlist.addTest(Test_Loginlog("test_menuOpLoglist_get_all_menus"))
        testlist.addTest(Test_Loginlog("test_menuOpLoglist_query_all_org"))
        testlist.addTest(Test_Loginlog("test_menuOpLoglist_query_all_sys"))
        testlist.addTest(Test_Loginlog("test_siteAccessLoglist_right"))
        testlist.addTest(Test_Loginlog("test_siteAccessLoglist_noallid1"))
        testlist.addTest(Test_Loginlog("test_siteAccessLoglist_noallid2"))
        testlist.addTest(Test_Loginlog("test_siteAccessLoglist_noallid3"))
        testlist.addTest(Test_Loginlog("test_siteAccessLoglist_query_all_sys"))
        testlist.addTest(Test_Loginlog("test_siteAccessLoglist_query_all_org"))
        testlist.addTest(Test_Loginlog("test_grantOperationLoglist_right"))
        testlist.addTest(Test_Loginlog("test_grantOperationLoglist_noallid1"))
        testlist.addTest(Test_Loginlog("test_grantOperationLoglist_noallid2"))
        testlist.addTest(Test_Loginlog("test_grantOperationLoglist_noallid3"))
        testlist.addTest(Test_Loginlog("test_logpagelistlist_right"))
        testlist.addTest(Test_Loginlog("test_logpagelistlist_noallid1"))
        testlist.addTest(Test_Loginlog("test_logpagelist_noallid2"))
        testlist.addTest(Test_Loginlog("test_logpagelist_noallid3"))

    if '统计分析'in s:

        # 登录
        testlist.addTest(Login("test_login"))
        #统计分析
        testlist.addTest(Test_ReportForms("test_userActivity_right"))
        testlist.addTest(Test_ReportForms("test_userActivity_wrong_nobegindata"))
        testlist.addTest(Test_ReportForms("test_userActivity_wrong_noenddata"))
        testlist.addTest(Test_ReportForms("test_userActivity_wrong_nodata"))
        testlist.addTest(Test_ReportForms("test_summary_right"))
        testlist.addTest(Test_ReportForms("test_summary_query_all_org"))
        testlist.addTest(Test_ReportForms("test_summary_query_org_all_sys"))
        testlist.addTest(Test_ReportForms("test_summary_menu_use_frequency"))
        testlist.addTest(Test_ReportForms("test_summary_sys_call_frequency"))
        testlist.addTest(Test_ReportForms("test_summary_sys_user_count"))
        testlist.addTest(Test_ReportForms("test_summary_log_call_trend"))
        # testlist.addTest(Test_ReportForms("test_summary_wrong_nobegindata"))
        testlist.addTest(Test_ReportForms("test_summary_sys_call_frequency"))
        testlist.addTest(Test_ReportForms("test_summary_wrong_noenddata"))
        # testlist.addTest(Test_ReportForms("test_summary_wrong_nodata"))
        testlist.addTest(Test_ReportForms("test_summary_sys_call_frequency"))
        testlist.addTest(Test_ReportForms("test_getUserCount_right"))
        testlist.addTest(Test_ReportForms("test_getUserCount_wrong_noorgid"))
        testlist.addTest(Test_ReportForms("test_getUserCount_wrong_nosysid"))
        testlist.addTest(Test_ReportForms("test_getUserCount_wrong_noallid"))
        testlist.addTest(Test_ReportForms("test_trend_right"))
        testlist.addTest(Test_ReportForms("test_trend_wrong_noorgid"))
        testlist.addTest(Test_ReportForms("test_trend_wrong_nobeginDate"))
        testlist.addTest(Test_ReportForms("test_trend_wrong_noendDate"))
        testlist.addTest(Test_ReportForms("test_trend_wrong_noalldata"))

    if '基础设置' in s:

        # 登录
        testlist.addTest(Login("test_login"))
        # 基础设置
        testlist.addTest(Test_system_setting("test_system_settting_search_right"))
        # testlist.addTest(Test_system_setting("test_system_settting_search_wrong"))
        testlist.addTest(Test_system_setting("test_system_settting_update_right"))
        # testlist.addTest(Test_system_setting("test_system_settting_update_wrong1"))
        # testlist.addTest(Test_system_setting("test_system_settting_update_wrongkey"))
        # testlist.addTest(Test_system_setting("test_system_settting_update_wrongkey1"))

    if '系统资源配置' in s:

        # 登录
        testlist.addTest(Login("test_login"))
        # 系统资源配置
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_add_right"))
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_add_wrong1"))
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_add_wrong2"))
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_add_wrong3"))
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_search"))
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_search_wrong"))
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_search_wrong1"))
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_update_right"))
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_update_wrong"))
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_delete_right"))
        testlist.addTest(Test_sysresourcesconfig("test_sysresourcesconfig_delete_wrong"))


    # # 基础数据管理-删除部门
    # testlist.addTest(DivisionManagement("test_delete_division"))
    # # 基础数据管理-删除机构
    # testlist.addTest(OrgManagement("test_org_close"))
    # testlist.addTest(OrgManagement("test_delete_org"))
    # #人员权限管理-用户账号管理-删除用户账号
    # testlist.addTest(UserAccountManagement("test_delete_useraccount"))
    # # 人员权限管理-人员管理-删除用户信息
    # testlist.addTest(PersonnelManagement("test_delete_userinfo"))
    # # 人员权限管理-平台角色-删除平台角色
    # testlist.addTest(PlatRoles("test_delete_plat_role_type"))
    # #菜单管理-删除组件按钮
    # testlist.addTest(MenuManagement("test_delete_module_btn"))
    # # 菜单管理-删除组件菜单
    # testlist.addTest(MenuManagement("test_delete_module_menu"))
    # # 菜单管理-删除组件目录
    # testlist.addTest(MenuManagement("test_delete_module_dir"))
    # # 第三方应用-删除第三方应用
    # testlist.addTest(ThirdPartyApplications("test_delete_third_party_app"))
    # # 应用分类-应用分类删除
    # testlist.addTest(ApplicationClassification("test_app_classifi_delete"))
    # # 厂商管理-厂商删除
    # testlist.addTest(VendorManagement("test_vendor_delete"))



    # testlist.addTest(ApplicationRoles("test_queryapplicationlist"))
    # testlist.addTest(ApplicationRoles("test_queryrolebysystem"))
    # testlist.addTest(ApplicationRoles("test_arpcqpoars"))
    # testlist.addTest(ApplicationRoles("test_arpqrprs"))
    # testlist.addTest(ApplicationRoles("test_batchroleauthorization"))
    # testlist.addTest(Logout("test_logout"))
    '''跑一个类文件下的所有测试用例'''
    # testlist = unittest.TestSuite(unittest.makeSuite(TestModel))
    now = time.strftime("%Y-%m-%d_%H:%M:%S")
    # filename = 'result.html'
    # filename = test_report + "\\" + now +'result.html'
    filename = sys.path[-1] + "/" + 'result.html'
    fp = open(filename,'wb')

    runner = HTMLTestRunner(
                stream=fp,  # 文件
                verbosity=2,
                title="身份认证系统接口自动化测试报告",  # 标题
                description=u"系统环境：Liunx 用例执行情况："  # 描述
            )
    runner.run(testlist)  # 启动测试套件
    fp.close()
    #复制一份测试报告到/a_udaam/reports中
    # reports_filename = sys.path[-1] + '/a_udaam/reports/'+now+'result.html'
    # copyfile_yaml(filename,reports_filename)
    # 记录用例执行完的时间
    get_times_end = get_time()
    print('所有用例 ：'+get_html_data(filename)[5])
    print('成功用例 ：' + get_html_data(filename)[4])
    print('失败用例 ：' + get_html_data(filename)[3])
    print('错误用例 ：' + get_html_data(filename)[2])
    #计算用例执行时间
    run_time = (get_times_end-get_times_start)/1000
    print('总运行时间:'+str(run_time)+'s')
    all_time = str(run_time) + 's'

    #获取html测试报告的内容
    data = get_html_by_id_create_list(filename)
    # gf = Graphs()
    #生成pdf的测试报告
    # gf.create_pdf(get_times_start_ymd, all_time, get_html_data(filename)[4], int(get_html_data(filename)[5]), int(get_html_data(filename)[4]), int(get_html_data(filename)[3]), data)
    notice = ''
    if '"message": "服务器内部错误"' in str(read_html(filename)):
        notice = '注意!需要开发人员查看,被测系统存在服务器内部错误!'
    elif '没有到主机的路由' in str(read_html(filename)):
        notice = '注意!需要开发人员查看,被测系统存在没有到主机的路由错误!'

    report_pdf = sys.path[-1] + "/" + '身份认证系统接口自动化测试报告.pdf'
    # new_report = new_file(test_report)                                #获取最新报告文件
    yagindex = yagmail.SMTP(user={"cdzdhcs@casking.com.cn":'身份认证系统接口自动化'}, password='Chandao123', host='smtp.exmail.qq.com')
    template = """<div style="line-height: 25px;"><div style="padding: 10px 0; border: none; vertical-align: middle;"><strong style="font-size: 16px">各位领导、同事:<br/>大家好，以下为身份认证系统接口自动化项目构建信息及运行结果</br></div><div style="border-collapse: collapse; background-color: #fff; border: 1px solid #cfcfcf; box-shadow: 0 0px 6px rgba(0, 0, 0, 0.1); margin-bottom: 20px; font-size:13px;"><div style="padding: 10px; background-color: #F8FAFE; border: none; font-size: 14px; font-weight: 500; border-bottom: 1px solid #e5e5e5;">禅道地址:<a href="http://192.168.13.148:63802/bug-browse-1-0-unclosed.html"style="color: #333; text-decoration: underline;"target="_blank">http://192.168.13.148:63802/bug-browse-1-0-unclosed.html</a><br/>在线测试报告:<a href="http://192.168.13.159:63363"style="color: #333; text-decoration: underline;"target="_blank">http://192.168.13.159:63363</a></div><div style="padding: 10px; border: none;"><fieldset style="border: 1px solid #e5e5e5"><legend style="color: #114f8e">状态</legend><div style="padding:5px;"><b><font color="#0B610B">构建信息</font></b><hr size="2"width="100%"align="center"/><ul style="line-height: 20px;"><li>项目名称：身份认证系统接口自动化项目</li><li>触发原因：云帮-研发团队-统一身份认证V3</li><li>构建状态：操作成功</li><li>构建URL：<a href="http://192.168.13.159:10000/#/team/xdpvzcyl/region/CLUSTER-56/components/gr5279b8/overview">http://192.168.13.159:10000/#/team/xdpvzcyl/region/CLUSTER-56/components/gr5279b8/overview</a></li></ul><b><font color="#0B610B"style="font-size: 14px;">运行结果</font></b><hr size="2"width="100%"align="center"/><ul style="line-height: 20px;;margin-bottom: 0px;"><li>运行时长：""" + all_time + """</li><li>所有用例：""" + get_html_data(filename)[5] + """</li><li>成功用例：""" + get_html_data(filename)[4] + """</li><li>失败用例：""" + get_html_data(filename)[3] + """</li><li>错误用例：""" + get_html_data(filename)[2] + """</li></ul><div><div style="font-size: 12px;color: #ddb100;border-bottom: 1px dashed #ccc;font-weight: bold;padding-left: 6px;font-weight: normal;">备注</div><ul style="color:#ddb100;line-height:20px; font-weight: normal;"><li>失败表示被测接口问题</li><li>错误表示测试用例问题</li></ul></div></div><div style="padding: 10px; background-color: #FFF0D5"><span style="font-size: 16px; color: #F1A325">●</span>&nbsp;<span><span style="border-bottom:1px dashed #ccc;"t="5"times=" 13:55">""" + new_time().split(' ')[0] + """</span>""" + new_time().split(' ')[ 1] + """,由<strong>""" + '身份认证系统接口自动化' + """</strong>创建。</span></div></div>"""
    inscribe = """
            cdzdhcs@casking.com.cn测试部
            地址：深圳市南山区高新南七道数字技术员工程实验室大楼B座6楼  
            座机：0755-83681011
            邮箱：cdzdhcs@casking.com.cn
            官网：https://www.united-imaging-data.com.cn/
    """
    # contents1 = [template_file, yagmail.inline(sys.path[-1] +'\luokuan.jpg'), inscribe]
    # yagindex.send('zhaopengtian@lefu.cc', 'yagmail带附件主题实例', yag_contents, new_report)
    mail_config = sys.path[0] + '/a_udaam/data/mail_config.yaml'
    bug_mail_addressee = read_yaml(mail_config, 'bug_mail_addressee')
    bug_mail_cc = read_yaml(mail_config, 'bug_mail_cc')
    result_mail_addressee = read_yaml(mail_config, 'result_mail_addressee')
    result_mail_cc = read_yaml(mail_config, 'result_mail_cc')
    send_to = ['wub@casking.com.cn','tianxh@casking.com.cn']
    # yagindex.send(send_to, '身份认证系统接口自动化测试报告', contents1, test_report)
    read_html(filename)
    if 'configparser.ParsingError'not in str(read_html(filename)) and 'WinError 10048' not in str(read_html(filename)) and '"message": "未经授权"' not in str(read_html(filename)) and 'UnicodeDecodeError' not in str(read_html(filename)) and 'configparser.DuplicateOptionError' not in str(read_html(filename)):
        pass
        # yagindex.send(result_mail_addressee, new_time().split(' ')[0]+' '+new_time().split(' ')[1]+'[接口自动化]'+'-身份认证系统接口自动化测试报告', template,cc=result_mail_cc)
    # yagindex.send('3407135351@qq.com', now+'身份认证系统接口自动化测试报告',template,report_pdf)
    yagindex.send('tianxh@casking.com.cn', new_time().split(' ')[0]+' '+new_time().split(' ')[1]+'[接口自动化]'+'-身份认证系统接口自动化测试报告', template,sys.path[-1] + '/a_udaam/data/case_parameters.ini')
    # yagindex.send('wub@casking.com.cn', now + '[接口自动化]' + '-身份认证系统接口自动化测试报告', template,
    #               sys.path[-1] + '/a_udaam/data/case_parameters.ini')
    # yagindex.send(result_mail_addressee, now + '[接口自动化]' + '-身份认证系统接口自动化测试报告', template, cc=result_mail_cc)
    # yagindex.send('tianxh@casking.com.cn', now+'身份认证系统接口自动化测试报告', template, report_pdf)
    log.info('发送邮件成功')