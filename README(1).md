<div align="center">
<br/>
<br/>
  <h1 align="center">
    联影自动化框架
  </h1>
  <h4 align="center">
    开 箱 即 用 的 自 动 化 框 架
  </h4> 


<p align="center">
    <a href="#">
        <img src="https://img.shields.io/badge/Python-3.8+-green.svg" alt="Python Version">
    </a>
</p>

#### 框架简介
联影自动化框架，基于Requests,Jmeter,绿盟等工具的自动化测试框架,拥抱应用广泛的python语言，通过使用本框架，即可快速构建你的功能业务

项目旨在为测试人员提供一个使用,拓展的框架，可以快速使用,构建自己的测试业务。

联影自动化框架分为接口自动化,性能自动化,安全自动化.

接口自动化通过云帮构建,开发可以通过配置文件选择项目模块,选择执行对应被测系统,读取配置文件,执行测试用例,禅道自动化提交bug,发送bug邮件,发送测试报告邮件.

性能自动化通过云帮构建,选择执行对应被测系统,读取配置文件,执行测试用例,禅道自动化提交bug,发送bug邮件,发送测试报告邮件.					

安全自动化通过云帮构建,选择执行对应被测系统,读取配置文件,执行测试用例,禅道自动化提交bug,发送bug邮件,发送测试报告邮件.

####  内置功能

- [x] 接口请求：接口部分,通过requests，对被测接口进行入参调用。
- [x] jemter压测：性能部分，远程调用服务器，进行jmeter压测。
- [x] 绿盟扫描：安全部分,调用绿盟Api进行安全扫描。
- [x] 提交禅道bug：接口自动化,性能自动化,安全自动化运行中如有异常或者bug,会自动提交到禅道。
- [x] 邮件发送：接口自动化,性能自动化,安全自动化运行中如有异常或者bug,会自动发送bug邮件,运行结束会自动发送测试报告邮件。

####  项目结构

```
联影自动化框架
├─reliangApiTest  # 应用
│  ├─a_udaam  # 接口自动化项目模块
│  │  ├─ data  # 接口自动化文件配置模块
│  │  │   ├─ case_parameters.ini  # 接口自动化用例配置文件
│  │  │   ├─ mail_config.yaml  # 接口自动化邮件配置文件
│  │  │   ├─ practical_select_run.yaml  # 接口自动化接口模块选择对比配置文件
│  │  │   ├─ run_cases.yaml  # 接口自动化接口模块实际运行配置文件
│  │  │   ├─ select_run_cases.yaml  # 接口自动化接口模块选择运行配置文件
│  │  │   ├─ select_address.yaml  # 接口自动化被测系统服务器地址配置文件
│  │  │   ├─ token.yaml  # 接口自动化被测系统token配置文件
│  │  ├─ image_verification  # 接口自动化验证码模块
│  │  ├─ reports  # 接口自动化测试结果模块
│  │  ├─ TestCases  # 接口自动化测试用例模块
│  ├─Basepage  # 接口自动化requests重构模块
│  ├─Log  # 日志模型
│  │  ├─ log.txt  # 日志输出文件
│  ├─p_udemr  # 性能自动化项目模块
│  │  ├─ data  # 性能自动化文件配置模块
│  │  │   ├─ udemr  # 性能自动化被测系统文件配置模块
│  │  │   │   ├─ jmeter_script_config.ini  # 被测系统jmeter脚本参数配置文件
│  │  │   │   ├─ mail_config.yaml  # 被测系统邮件配置文件
│  │  ├─ image_verification  # 性能自动化验证码模块
│  │  ├─ reports  # 性能自动化测试结果模块
│  │  ├─ test_cases  # 性能自动化测试用例模块
│  │  │   ├─ udemr  # 性能自动化被测系统用例模块
│  │  │   │   ├─ login.py  # 被测系统登录文件
│  │  │   │   ├─ udemr_concurrent_testing.jmx  # 被测系统jmeter脚本
│  ├─s_udaam  # 安全自动化项目模块
│  │  ├─ data  # 性能自动化文件配置模块
│  │  │   ├─ udaam  # 性能自动化被测系统文件配置模块
│  │  │   │   ├─ config.xml  # 绿盟扫描配置文件
│  │  │   │   ├─ mail_config.yaml  # 被测系统邮件配置文件
│  │  ├─ image_verification  # 安全自动化验证码模块
│  │  ├─ reports  # 安全自动化测试结果模块
│  │  ├─ test_cases  # 安全自动化测试用例模块
│  │  │   ├─ operation_rsas_by_xml.py  # 安全自动化调用绿盟Api模块
│  └─Utils  # 公共方法模块
│     ├─ all_style_template.py  # 邮件模板公共方法
│     └─ cennect_mysql_zentao.py  # 连接禅道数据库公共方法
│     └─ conf.py  # 读取ini文件重构公共方法
│     └─ connectMysql.py  # 连接被测系统数据库公共方法
│     └─ copy_and_clear_file.py  # 文件复制,清空公共方法
│     └─ create_random.py  # 生成随机数公共方法
│     └─ currenttime.py  # 生成当前时间公共方法
│     └─ dicttogetparameter.py  # 把dict转换成get参数形式公共方法
│     └─ encrypt.py  # Rsa加密公共方法
│     └─ get_html_data.py  # 操作html公共方法
│     └─ getImageverification.py  # 获取验证码公共方法
│     └─ judge_os.py  # 获取当前操作系统公共方法
│     └─ log.py  # 日志公共方法
│     └─ operation_jmeter_alone.py  # 读取配置文件远程现在文件公共方法
│     └─ operation_minio.py  # 操作minio公共方法
│     └─ operation_pdf.py  # 操作pdf公共方法
│     └─ operation_remote_server.py  # 操作远程服务器公共方法
│     └─ operation_word.py  # 操作word公共方法
│     └─ operation_xml.py  # 操作xml公共方法
│     └─ operation_zentao_mysql.py  # 操作禅道数据库公共方法
│     └─ operationini.py  # 操作ini文件公共方法
│     └─ operationyaml.py  # 操作yaml文件公共方法
│     └─ page.py  # 重构requests请求公共方法
│     └─ performance_result_assertion.py  # 性能数据对比公共方法
│     └─ send_email.py  # 邮件发送公共方法
│     └─ zip_file.py  # 文件压缩公共方法
├─ Dockerfile  # 云帮Docker启动文件
├─ HTMLTestRunner.py  # 测试报告模板文件
├─ requirement.txt  # 依赖文件
├─ runMain_all.py # 项目总启动文件
├─ runMain_udemr_a.py # 被测系统接口自动化启动文件
├─ runMain_udemr_p.py # 性能自动化启动文件
└─ runMain_udemr_s.py # 安全自动化启动文件


```

#### 项目安装

```bash
# 下 载
svn checkout https://192.168.13.50:55000/svn/TEST/auto_test/reliangApiTest

# 安 装
pip install -r requirement.txt

```

#### 修改配置

```python
# MySql配置信息
MYSQL_HOST=XXX
MYSQL_PORT=XXX
MYSQL_DATABASE=XXX
MYSQL_USERNAME=XXX
MYSQL_PASSWORD=XXX

# 密钥配置
SECRET_KEY=XXX

# 邮箱配置
bug_mail_addressee=XXX
bug_mail_cc=XXX
result_mail_addressee=XXX 
result_mail_cc=XXX

```

#### 运行项目

```bash
# 云帮启动
云帮build
http://192.168.13.159:10000/#/team/5wn7eic2/region/CLUSTER-56/components/grf49b0a/overview
或者
python runMain_all.py

```
