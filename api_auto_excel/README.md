<div align="center">
<br/>
<br/>
  <h1 align="center">
    Excel+ddt接口自动化框架
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
Excel+ddt接口自动化框架，基于Requests,Ddt,Excel等工具的自动化测试框架,拥抱应用广泛的python语言，通过使用本框架，即可快速构建你的功能业务

项目旨在为测试人员提供一个使用,拓展的框架，可以快速使用,构建自己的测试业务。

####  内置功能

- [x] 接口请求：通过requests,对被测接口进行入参调用。
- [x] bug写入禅道：接口通过请求后,对bug进行断言,如果有不通过的bug自动写入禅道。
- [x] bug邮件发送：接口通过请求后,对bug进行断言,如果有不通过的bug自动发送邮件给相关人员。
- [x] 测试报告邮件发送：运行完成后,整体测试结果和附件自动发送邮件给相关人员。

####  项目结构

```
Excel+ddt接口自动化框架
├─reliangApiTest  # 应用
│  ├─api_auto_excel  # 接口自动化项目模块
│  │  ├─ data  # 接口自动化文件配置模块
│  │  │   ├─ system_under_test.yaml  # 接口自动化检测当前项目的配置文件
│  │  │   ├─ variable_storage.yaml  # 接口自动化存储变量的配置文件
│  │  ├─ image_verification  # 接口自动化验证码模块
│  │  ├─ reports  # 接口自动化结果模块
│  │  ├─ TestCases  # 接口自动化用例模块
│  │  ├─ business  # 接口自动化核心业务处理模块
│  │  │   ├─ register_case.py  # 接口自动化核心业务处理文件
│  ├─Basepage  # 接口自动化requests重构模块
│  ├─Log  # 日志模型
│  │  ├─ log.txt  # 日志输出文件
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
└─ runMain_excel.py # 安全自动化启动文件


```

#### 配置&使用

```bash
1.云帮配置
  哪个项目需要自动化测试,相关测试人员就在哪个研发环境的项目组件中的插件中
  的未开通中选择联影自动化测试插件v1.1开通,已经开通的在已开通中有显示.
  配置好后,重启项目.
  (切记:每个项目的项目名前缀不能重复,这个需要相关测试人员需要检查,如有重复和运维沟通)
2.Excel用例配置
  Excel表名的项目名起名要和云帮项目前缀名一样,例如:云帮项目的前缀名是"udaam",那么表名
  叫"udaam'接口用例脚本.xlsx",udaam后的名字固定.Excel用例的规范参考Excel中每
  个字段的批注,如有不懂可以提出.sheet中的用例部分固定名称"接口用例",配置部分固定名称"配置"
3.用例上传
  用例编写好以后,上传到MinIO Browser(地址:http://192.168.13.148:63805/minio/udaam/.
  用户名:AKIAIOSFODNN7EXAMPLE.密码:wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY).
  就上传到udaam目录中就可以.以后每次更新用例,就直接上传就可以.
  (切记:MinIO Browser中的用例文件名不能重复)
4.邮件配置
  邮件配置在Excel用例文件中配置,按照字段批注规范填写

```

#### 运行

```bash
# 云帮启动
云帮构建
http://192.168.13.159:10000/#/team/5wn7eic2/region/CLUSTER-56/components/grf49b0a/overview
被测项目构建成功后会自动构建接口自动化项目
```
