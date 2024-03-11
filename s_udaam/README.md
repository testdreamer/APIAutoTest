# 安全自动化使用指南

### 一 项目分类

1.安全自动化的所有项目都在s_udaam包中   
2.s_udaam包中分为data包,image_verification包,reports包,test_cases包  
3.data存放配置文件,image_verification包存放验证码图片,reports包存放测试结果,test_cases包存放测试用例或者controller  
4.data包中分每个被测项目包,例如:有两个被测项目,udaam和udemr,那就会在data包中存在udaam包和udemr包各自存放配置文件  
5.reports包中的被测项目包自动生成  
6.image_verification包因为只存放验证码,所以不需要分项目  
7.test_cases包存放共用controller,所以不需要分项目  

### 二 配置文件

1.data包中的配置文件有邮件配置文件和绿盟配置文件  
2.邮件配置文件中包括bug邮件配置,测试报告邮件配置  
3.绿盟配置文件是绿盟扫描加载的文件  

### 三 启动机制

1.项目的启动文件为根目录的runMain_all.py和runMain_udemr_s.py文件  
2.runMain_all文件为主启动文件,执行此文件,首先获取被测系统的名称,根据名称调用runMain_udemr_s.py文件,runMain_udemr_s.py文件再根据名称选择对应的系统配置文件进行扫描  

### 四 云帮配置

1.云帮中需要自动化测试的被测系统组件要开通联影自动化测试插件  
  进入被测系统*组件-->插件-->未开通*,点击开通**联影自动化测试**插件  
2.重启组件

### 五 操作流程

1.按照规定配置好项目结构,例如:有新被测系统,则在data包中增加项目包   
2.配置对应项目的邮件配置文件和对应的绿盟配置文件,绿盟配置文件中只修改任务名称和扫描目标  
3.云帮构建执行自动化
